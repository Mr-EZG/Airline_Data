import os
import csv

class Config(object):
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.database_dir = os.path.join(self.base_dir, "Big_DATA.csv")

    def __str__(self):
        return "test?"

    def reset_database(self):
        os.remove(self.database_dir)

    def database_exist(self):
        return os.path.exists(self.database_dir)

if __name__ == '__main__':
    config = Config()
    print("Test...")
    print("config:", config)
    print("base_dir:", config.base_dir)
