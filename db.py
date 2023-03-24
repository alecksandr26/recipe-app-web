import psycopg2

"""
TODO: Create a row instance to be able to enpack the rows with an easy manipulation
"""

class Table:
    # __init__: To catch the name of a table
    def __init__(self, name : str, conn, test : bool):
        self.conn = conn
        self.__name = name
        self.__columns = {}
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
        return self.name

    # __len__: Return the amount of rows inside of a table
    def __len__(self) -> int:
        cur = self.conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM {self.__name};")
        data, = cur.fetchall()[0]  #  Unpack the tuple
        cur.close()
        return data

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
        return data if len(data) > 1 else data[0]

    # get_where: To fecth the data with some columns defined like 
    def get_where(self, values : dict) -> tuple or [tuple]:
        cur = self.conn.cursor()
        query = f"SELECT * FROM {self.__name} WHERE " + " AND ".join(f"{val} = %s" for val in values.keys())
        cur.execute(query + ";", tuple(values.values()))
        data = cur.fetchall()
        cur.close()
        return data if len(data) > 1 else data[0]

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
    def __getitem__(self, table_name : str):
        return self.__tables[table_name]

    # __len__: Return the amount of tables inside of the object
    def __len__(self):
        return len(self.__tables)
    
    # get_tables_name: To fetch the tables
    def get_tables_name(self):
        return [*self.__tables]   # Unpack a keys
