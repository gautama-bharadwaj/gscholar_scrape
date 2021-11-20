import pandas as pd
import json

class Validate:

    def __init__(self, path):
        self.path = path
        self.df = pd.read_excel(self.path)
        with open('config/validate_config.json') as f:
            self.valid_params = json.load(f)

    def xls_format(self):
        if (list(self.df.columns) != self.valid_params['col_order']):
            print('Invalid formatting of the column names in ' + self.path + '\n')
            exit()
        return True

    def user_id(self, user_id, person):
        if (isinstance(user_id, float) and pd.isna(user_id)):
            print('User id for ' + person + 'does not exist. Skipping scrape..')
            return False
        return True
