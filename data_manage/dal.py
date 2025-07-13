import pandas as pd



class Dal:
    def __init__(self):
        self.data_table = None
        self.data_table_read = None


    def which_data(self):
        data = input("enter the url of your data thet you want to work with")
        return data

    def read_the_csv_to_df(self,the_csv_file = r"C:\Users\User\Downloads\phishing.csv"):
        if the_csv_file is None:
            the_csv_file = self.which_data()
        self.data_table_read = pd.read_csv(the_csv_file)
        # print(self.data_table_read)
        self.data_table = pd.DataFrame(self.data_table_read)
        print("Available columns:", self.data_table)

        return self.data_table

