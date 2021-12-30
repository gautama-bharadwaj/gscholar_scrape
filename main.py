from functions.scraper import Scraper
from functions.output import Output
from datetime import datetime
import json
import argparse
import sys
from datetime import date


class DefaultParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write("error: {}\n".format(message))
        self.print_help()
        sys.exit(2)


class Parser:
    usage = "Generate reports based on input arguments"

    # noinspection PyTypeChecker
    def create_parser(self):
        parser = DefaultParser(
            description="%(prog)s",
            formatter_class=argparse.RawTextHelpFormatter,
            add_help=False,
            prog="Crunch Reports",
            usage=self.usage,
        )
        self.add_arguments(parser)
        return parser

    @staticmethod
    def add_arguments(parser):

        # Add optional options
        optional_opts = parser.add_argument_group("Optional Arguments")
        optional_opts.add_argument(
            "-y", "--year", type=int, help="Enter year as integer"
        )
        help_ = parser.add_argument_group("help")
        help_.add_argument("-h", "--help", action="help",
                           help="Show usage info and exit")

    def get_kwargs(self):
        argv = sys.argv[1:] if sys.argv else ["--help"]
        count = 1
        for count, entry in enumerate(argv):
            if entry.startswith("-") or entry.startswith("--"):
                break
        parser = self.create_parser()
        args = parser.parse_args(argv[count:])

        # convert file formats to a list
        # args.file_format = [item for item in args.file_format.split(",")]

        return dict(
            year=args.year
        ).items()


def run_module(year):
    with open('config/output_file.json') as f:
        file_path = json.load(f)
    scrape_data = Scraper('input/people_gscholar.xls').scrape(year)
    op = Output()
    clean_data = op.clean_data(scrape_data)
    op.xlsoutput(clean_data, file_path['path'])


if __name__ == "__main__":
    keyword_args = dict(Parser().get_kwargs())
    start_time = datetime.now()
    if(keyword_args['year']!=None):
        year = keyword_args['year']
    else:
        year = date.today().year
    run_module(year)
    end_time = datetime.now()
    print('Task execution time: {}'.format(end_time - start_time))
