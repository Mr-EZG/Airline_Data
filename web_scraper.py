from relative_file_paths import Config
import pandas as pd
from bs4 import BeautifulSoup
import urllib

base_columns = ["flight", "date", "price", "occupancy", "from", "to"]
base_url = ""

def get_doc(url):
    f = urllib.request.urlopen(url)
    file = f.read()
    return file

class DataBase(object):

    def __init__(self, config):
        print("Setting up configurations...")
        self.config = config
        if config.database_exist():
            print("database found, attempting to recover database...")
            self.df = pd.read_csv(self.config.database_dir)
            print("database recovered!")
        else:
            print("attempting to create database...")
            self.df = self.initialize_csv()

    def initialize_csv(self):
        base_columns_dict = dict()
        for thing in base_columns:
            base_columns_dict[thing] = []
        file_name = self.config.database_dir
        df = pd.DataFrame(base_columns_dict)
        df.to_csv(file_name)
        return df

    def reset(self):
        self.config.reset_database()
        self.initialize_csv()

    def save(self):
        self.df.to_csv(self.config.database_dir)

    # stats is a dictionary similar to containing values for base_columns
    # name is the flight number
    def update_row(self, name, stats):
        self.df[name] = stats

class Webscraper(object):

    def __init__(self):
        self.something = None
        self.url = "https://www.google.com/flights?hl=en#flt=/m/030qb3t.CRP.2019-07-08;c:USD;e:1;px:8;sd:1;t:f;tt:o"
        # try:
        self.html_file = get_doc(self.url)
        # except:
        # print(failed to get contents)
        self.soup = BeautifulSoup(self.html_file, "html.parser")
    # except:
        print("init failed, please see what went wrong")


    def print(self):
        print(self.soup.get_text())
        print("------------------")
        print(self.soup.prettify())



if __name__ == '__main__':
    config = Config()
    print("Test:", config)
    # config.reset_database()
    print("Checking for database...")
    # try:
    db = DataBase(config)
    print("DB Instantiated...")
    ws = Webscraper()
    ws.print()
    # except:
    #     print("Oof")


