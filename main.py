from functions.scraper import Scraper
from functions.output import Output
from datetime import datetime
import json

def run_module():
    with open('config/output_file.json') as f:
        file_path = json.load(f)
    scrape_data = Scraper('input/people_gscholar.xls').scrape()
    op = Output()
    clean_data = op.clean_data(scrape_data)
    op.xlsoutput(clean_data, file_path['path'])


if __name__ == "__main__":
    start_time = datetime.now()
    run_module()
    end_time = datetime.now()
    print('Task execution time: {}'.format(end_time - start_time))
