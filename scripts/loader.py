# Extact the comments 

import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
import csv
from selenium.webdriver.firefox.options import Options

# Global variables
firefox_options = Options()
firefox_options.headless = True

def render_page(url):
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(url)
    time.sleep(3)
    r = driver.page_source
    driver.quit()
    return r

def main():
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv('../backups/recipes.csv')
    
    file_comments = open("comments.csv", "w", newline='')
    writer = csv.DictWriter(file_comments, fieldnames=["name", "comments"])
    writer.writeheader()
        
    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        comments = {"name" : row['recipe_name'], "comments" : []}
        r_page = render_page(row['url'])
        soup = BeautifulSoup(r_page, 'html.parser')
        comments_div = soup.find('div', {'class': 'feedback-list__items'})
        if comments_div != None:
            for comment in comments_div.find_all('div', {'class': 'feedback-list__item'}):
                comment_str = comment.text.strip().split('\n')[3]
                comments["comments"].append(comment_str)

            comments['comments'] = str(comments['comments'])
        else:
            print(row['url'])
        print(index)
        writer.writerow(comments)



if __name__ == "__main__":
    main()
