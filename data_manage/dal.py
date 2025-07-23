import pandas as pd
import loger.logs_for_server
import logging
from pathlib import Path


class Dal:
    def __init__(self):
        self.data_table = None
        self.data_table_read = None
        self.CSV_PATH = None


    def the_csv_path(self):
        BASE_DIR = Path(__file__).parent.parent
        self.CSV_PATH = BASE_DIR / "the-csv-file" / "buy_computer_data.csv"

        # with open(LOG_PATH, "a") as f:
        #     f.write("Log started...\n")


    def which_data(self):
        try:
            self.the_csv_path()
            data = self.CSV_PATH
        except Exception as e:
            data = input("enter the url of your data thet you want to work with")
            logging.info("choose of which data to do predict")
        return data


    def choose_which_column(self):
        column = input("choose which column").strip().strip('"').strip("'")
        logging.info("choose of which column to do prediction")
        return column

    def read_the_csv_to_df(self):
        the_csv_file = self.which_data()
        self.data_table_read = pd.read_csv(the_csv_file)
        logging.info("read the csv file")
        self.data_table = pd.DataFrame(self.data_table_read)
        print("Available columns:", self.data_table)

        return self.data_table
# del1 = Dal()
# del1.read_the_csv_to_df()

 # = r"C:\Users\User\Downloads\phishing.csv"
# r"C:\Users\User\Downloads\buy_computer_data.csv"

