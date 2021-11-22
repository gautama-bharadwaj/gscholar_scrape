# gscholar_scrape

Gscholar_scrape is a Python module that scrapes Google Scholar for publications queried by author ids, and stores the result in an .xlsx file.

## Installation

Clone the repository. Open a terminal & cd to the directory where ```requirements.txt``` is located. 

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required python libraries.

```bash
pip install -r requirements.txt
```

## Configurations

- ### output_file.json

Copy the existing Excel sheet of publications to the output folder. (Or, create a blank Excel sheet in the output folder). In ```output_file.json```, enter the path of the Excel sheet as shown below:

```json
{
    "path": "output/UC Davis Bicycle Research.xlsx"
}
```

By default, this already exists. If the name of the Excel sheet is changed, it would have to be updated in ```output_file.json```

- ### config.ini

A file ```config.ini``` exists in the ```config``` folder. The following changes have to be made:

```ini
[EMAILKEYS]
password=password_to_the_bot_account
to=email_to_which_the_updates_should_go
from=gscholar.scrape.bot@gmail.com
```

Change the ```password``` and ```to``` keys in the file. Replace ```password_to_the_bot_account``` with the actual password and replace ```email_to_which_the_updates_should_go``` with the email id you would like to receive the updates to

# Usage

In order to run the module, run

```bash
python3 main.py
```

## Working

The entire module takes input from ```people_gscholar.xls``` file present in the ```input``` folder. This file contains the list of people and their associated user ids on Google Scholar. An example of ```people_gscholar.xls``` is shown below: 

|people	| user_id|
| ------ | ------- |
|Dillon Fitch	 | UZsQFKEAAAAJ|
|Susan Handy	 | UANPBv8AAAAJ|
|Lisa Aultman-Hall	 | FpdZ3dgAAAAJ|
|Jesus M Barajas	 | HqvaWWEAAAAJ|
|Austin Brown	 | 3jzqjVEAAAAJ|
|Giovanni Circella	 | 1LqIMYwAAAAJ|
|Tatsuya Fukushige	 | 4_Ty81YAAAAJ|
|Miguel Jaller	 | l0AOJokAAAAJ|
|Alan Jenn	 | h-2TvzUAAAAJ|
|Amy Lee	 | xiFq5cYAAAAJ|
|Hossain Mohiuddin	 | uVKaSqcAAAAJ|
|Jason K. Moore	 | i9c-QOYAAAAJ
|Xiaodong Qian	 | ZsT2os0AAAAJ|
|Angela Sanguinetti	C | AzS0UsAAAAJ|
|Jamey Volker	 | bHr8CMQAAAAJ|
|Kailai Wang	 | Bop0MYsAAAAJ|

The module loops through the authors, searches for publications, and appends any new publication that is not already included in the output excel file into the excel file.
