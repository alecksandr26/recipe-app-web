import psycopg2

"""
TODO: Create a row instance to be able to enpack the rows with an easy manipulation
TODO: Create a model instance to be able to create tables and more
"""

class Table:
    # __init__: To catch the name of a table
    def __init__(self, name : str, conn, test : bool):
        self.conn = conn
        self.__name = name
        self.__columns = {}
        self.__columns_constraints = {}  # Work with columns constra
        self.__test = test
        
        cur = conn.cursor()
        # fetch all the columns from the table
        cur.execute("SELECT column_name, data_type "
                    "FROM information_schema.columns "
                    f"WHERE table_schema = 'public' AND table_name = '{name}';")
        for pair in cur.fetchall():
            column, datatype = pair
            self.__columns[column] = datatype
        cur.close()

    # __str__: To return the name
    def __str__(self):
        return f"<Table \"{self.__name}\">"

    # __len__: Return the amount of rows inside of a table
    def __len__(self) -> int:
        cur = self.conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM {self.__name};")
        data, = cur.fetchall()[0]  #  Unpack the tuple
        cur.close()
        return data

    # __getitem__: To fetch the column datatype by its name or fetch some row by its index in the table.
    def __getitem__(self, column_name_index : str or int) -> str or tuple:
        if isinstance(column_name_index, str):
            return self.__columns[column_name_index]
        
        assert isinstance(column_name_index, int)
        fields_str = ", ".join(str(val) for val in self.__columns.keys())
        cur = self.conn.cursor()
        cur.execute(f"WITH cte_{self.__name} AS "
                    f"(SELECT *, row_number() OVER (ORDER BY id) AS rnum FROM {self.__name} ORDER BY id) "
                    f"SELECT {fields_str} FROM cte_{self.__name} WHERE rnum = {column_name_index + 1};")
        data = cur.fetchall()
        cur.close()
        if data == []:          #  Index doesn't exist
            raise IndexError('table index out of range')
        return data[0]

    # get_columns_name: To fetch the column names
    def get_columns_name(self) -> [str]:
        return list(self.__columns.keys())

    # get_columns_datatype: To fecth the data type of each column
    def get_columns_datatype(self) -> [str]:
        return list(self.__columns.values())

    # insert: New data to the table by putting the keys 
    def insert(self, values : dict or [dict]):
        assert len(values) > 0
        assert isinstance(values, list) or isinstance(values, dict)  #  values needs to be a dict or a list
        cur = self.conn.cursor()
        
        #  Try to insert the values
        if isinstance(values, list):
            assert isinstance(values[0], dict)  # The elements from the list needs to be a dictionarys
            fields_str = ", ".join(str(val) for val in values[0].keys())
            values_str = '%s, ' * (len(values[0]) - 1) + '%s'
            values = tuple(tuple(d.values()) for d in values)
        else:
            fields_str = ", ".join(str(val) for val in values.keys())
            values = tuple(values.values())
            values_str = '%s, ' * (len(values) - 1) + '%s'
            
        # To insert many elements
        cur.executemany(f"INSERT INTO {self.__name} ({fields_str}) "
                        f"VALUES ({values_str})", values)
        cur.close()
        
        # To be able to do operations without commiting the changes creating tests
        if not self.__test:     
            self.conn.commit()


    # del_all: To delete all the rows from the table
    def del_all(self):
        cur = self.conn.cursor()
        cur.execute(f"DELETE FROM {self.__name} CASCADE;")
        cur.close()
        if not self.__test:
            self.conn.commit()

    # del_where: To delete some rows from a column
    def del_where(self, values : dict):
        cur = self.conn.cursor()
        query = f"DELETE FROM {self.__name} WHERE " + " AND ".join(f"{val} = %s" for val in values.keys())
        cur.execute(query + ";", tuple(values.values()))
        cur.close()
        
        if not self.__test:
            self.conn.commit()

    # get_all: To fetch all the data
    def get_all(self) -> tuple or [tuple]:
        cur = self.conn.cursor()

        cur.execute(f"SELECT * FROM {self.__name};")
        data = cur.fetchall()
        cur.close()
        if data == []:
            return data
        return data if len(data) > 1 else data[0]

    # get_where: To fecth the data with some columns defined like 
    def get_where(self, values : dict) -> tuple or [tuple]:
        cur = self.conn.cursor()
        query = f"SELECT * FROM {self.__name} WHERE " + " AND ".join(f"{val} = %s" for val in values.keys())
        cur.execute(query + ";", tuple(values.values()))
        data = cur.fetchall()
        cur.close()
        if data == []:
            return data
        return data if len(data) > 1 else data[0]

    # update_where: To update the rows where.
    def update_where(self, values : dict, where : dict):
        cur = self.conn.cursor()
        values_str = ", ".join(f"{column} = %s" for column in values.keys())
        values_where = " AND ".join(f"{column} = %s" for column in where.keys())
        query = f"UPDATE {self.__name} SET {values_str} WHERE {values_where}"
        query_values = tuple(val for val in values.values())
        query_values = query_values + tuple(val for val in where.values())
        cur.execute(query, query_values)
        cur.close()
        self.conn.commit()


class DB:
    # __init__: Connect to the data base
    def __init__(self, dbname : str, user : str, test : bool = False):
        self.conn = psycopg2.connect(f"dbname = {dbname} user = {user}")
        self.__tables = {}
        self.__test = test
        cur = self.conn.cursor()
        
        # Fetch all the tables names
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        for tuple_table_name in cur.fetchall():
            (table_name, ) = tuple_table_name  # Unpack the tuple
            self.__tables[table_name] = Table(table_name, self.conn, test = test)
            
        cur.close()

    # __del__: To close the connection
    def __del__(self):
        self.conn.close()

    # __getitem__: To fetch a table.
    def __getitem__(self, table_name_or_index : str or int):
        if isinstance(table_name_or_index, int):
            return self.__tables[list(self.__tables.keys())[table_name_or_index]]
        else:
            assert isinstance(table_name_or_index, str)
            return self.__tables[table_name_or_index]

    # __len__: Return the amount of tables inside of the object
    def __len__(self):
        return len(self.__tables)

    # __ite__: To start the iteration of the object
    def __ite__(self):
        self.index = 0
        return self
    
    # __next__: To iterate to the next element
    def __next__(self):
        self.index += 1
        # To finish the iteration
        if self.index == len(self.__tables):
            raise StopIteration
        return list(self.__tables.keys())[self.index - 1]
    
    # get_tables_name: To fetch the tables
    def get_tables_name(self):
        return [*self.__tables]   # Unpack a keys

    # del_all: To delete all the tables but it didn't work yet
    def del_all(self):
        # Delete all the tables
        for table_name in self.__tables:
            self.__tables[table_name].del_all()
