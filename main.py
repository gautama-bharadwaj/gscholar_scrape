from scraper import Scraper
from output import Output
from datetime import datetime

def run_module():
    scrape_data = Scraper('input/people_gscholar.xls').scrape()
    op = Output()
    clean_data = op.clean_data(scrape_data)
    op.xlsoutput(clean_data, 'output/UC Davis Bicycle Research.xlsx')


if __name__ == "__main__":
    start_time = datetime.now()
    run_module()
    end_time = datetime.now()
    print('Task execution time: {}'.format(end_time - start_time))
