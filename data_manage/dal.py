import pandas as pd
import loger.logs_for_server
import logging


class Dal:
    def __init__(self):
        self.data_table = None
        self.data_table_read = None


    def which_data(self):
        data = input("enter the url of your data thet you want to work with")
        logging.info("choose of which data to do predict")
        return data


    def choose_which_column(self):
        column = input("choose which column").strip().strip('"').strip("'")
        logging.info("choose of which column to do prediction")
        return column

    def read_the_csv_to_df(self,the_csv_file=r"C:\Users\User\Downloads\buy_computer_data.csv"):
        if the_csv_file is None:
            the_csv_file = self.which_data()
        self.data_table_read = pd.read_csv(the_csv_file)
        logging.info("read the csv file")
        self.data_table = pd.DataFrame(self.data_table_read)
        print("Available columns:", self.data_table)

        return self.data_table

 # = r"C:\Users\User\Downloads\phishing.csv"
# r"C:\Users\User\Downloads\buy_computer_data.csv"

