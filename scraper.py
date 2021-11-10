from scholarly import scholarly, ProxyGenerator
from pathlib import Path
import pandas as pd
import json
from validate import Validate

class Scraper:
    def __init__(self, path):
        self.path = path

    def read_user_id(self):
        validate = Validate(self.path)
        user_ids = []
        user_ids_dict = {}
        if(validate.xls_format()):
            people_data = pd.read_excel(self.path)
            for index, row in people_data.iterrows():
                if(validate.user_id(row['user_id'], row['people'])):
                    user_ids_dict[row['user_id']] = row['people']
                    user_ids.append(row['user_id'])
            return user_ids_dict

    def scrape(self):
        user_ids = self.read_user_id()
        df = pd.DataFrame()
        for id in user_ids.keys():
            print('Scraping data for ' + user_ids[id])
            search_query = scholarly.search_author_id(id)
            author = scholarly.fill(search_query, sections=['publications'])
            i = 0
            for pub in author['publications']:
                df = df.append(scholarly.fill(pub), ignore_index=True)
                if(i == 1):
                    break
                i += 1
        return df
