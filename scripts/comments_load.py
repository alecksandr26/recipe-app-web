from db import *
import pandas as pd

def main():
    db = DB("recipe", "postgres")
    df = pd.read_csv('./comments.csv')
    for index, row in df.iterrows():
        row_recipe = db['recipe'].get_where({"name" : row["name"]})[0]
        if isinstance(row_recipe, tuple):
            idrecipe = row_recipe[0]
        else:
            idrecipe = row_recipe
            
        for comment in eval(row['comments']):
            db['comments'].insert({
                "comment" : comment.strip(),
                "idrecipe" : idrecipe
            })
            print("made it", idrecipe)
                      

if __name__ == "__main__":
    main()





