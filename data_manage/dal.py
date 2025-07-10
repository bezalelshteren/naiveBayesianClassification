import pandas as pd



class Dal:
    def __init__(self,):
        self.data_table = None


    def read_the_csv_to_df(self):
        self.data_table_read = pd.read_csv(r"C:\Users\User\Downloads\buy_computer_data.csv")
        self.data_table = pd.DataFrame(self.data_table_read)
        return self.data_table

