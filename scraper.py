from scholarly import scholarly, ProxyGenerator
from pathlib import Path
import pandas as pd
import math
from validate import Validate
from datetime import date

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
        year = date.today().year
        user_ids = self.read_user_id()
        df = pd.DataFrame()
        for id in user_ids.keys():
            print('Scraping data for ' + user_ids[id])
            search_query = scholarly.search_author_id(id=id, filled=True, sortby="year")
            author = scholarly.fill(search_query, sections=['publications'])
            for pub in author['publications']:
                filled_pub = scholarly.fill(pub)
                if (not math.isnan(filled_pub['bib']['pub_year'])):
                    if (int(filled_pub['bib']['pub_year']) == year):
                        print("publication scraped..")
                        df = df.append(filled_pub, ignore_index=True)
                    elif (int(filled_pub['bib']['pub_year']) > year):
                        continue
                    else:
                        break
        return df
