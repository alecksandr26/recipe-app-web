import pandas as pd
import math
from db import *
import re

pattern = r"([A-Za-z ]+) (\d+)(mg|g)"

def main():
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv('../backups/recipes.csv')

    db = DB("recipe", "postgres")

    # For cateogries
    """                          
    categories = {}
    for index, row in df.iterrows():
        category = row['cuisine_path'].split('/')[1]
        if category == "Mexican":
            print(row['url'])
        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1

    for category in categories:
        print(category, categories[category])
        db['category'].insert({"name" : category})
    """
    
        

    """
        for index, row in df.iterrows():
        data = {}
        if isinstance(row['prep_time'], str):
            data['preptime'] = row['prep_time']

        if isinstance(row['cook_time'], str):
            data['cooktime'] = row['cook_time']

        # Not null cases
        data['ingredients'] = row['ingredients']
        data['instructions'] = row['directions']
        data['url'] = row['url']
        data['name'] = row['recipe_name']
        data['portions'] = row['servings']
        
        # Extract cateory
        category = row['cuisine_path'].split('/')[1]
        id_category, category_name = db['category'].get_where({"name" : category})
        data['idcategory'] = id_category
        db['recipe'].insert(data)
    """

    for index, row in df.iterrows():
        print(index)
        for nutrin in row['nutrition'].split(', '):
            match = re.match(pattern, nutrin)
            name = match.group(1)
            grams = match.group(2)
            unit = match.group(3)
            row = db['nutritional_ele'].get_where({"name" : name, "idrecipe" : index + 1})
            if row != []:
                print(row)
            else:
                db['nutritional_ele'].insert({
                    "name" : name,
                    "amount" : grams,
                    "unit" : unit,
                    "idrecipe" : index + 1
                })
        
        
        
             
        
if __name__ == "__main__":
    main()
