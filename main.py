from scraper import Scraper
from output import Output

def run_module():
    scrape_data = Scraper('input/people_gscholar.xls').scrape()
    op = Output()
    clean_data = op.clean_data(scrape_data)
    op.xlsoutput(clean_data, 'output/publications.xlsx')


if __name__ == "__main__":
    run_module()