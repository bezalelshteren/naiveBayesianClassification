from data_manage.dal import Dal
from classification.check_data import check_data
from classification.train_a_model import train_a_model
from data_manage.cleaner import clean_data

class controler:
    def __init__(self):
        self.del_data = Dal()
        self.data_table = self.del_data.read_the_csv_to_df()
        self.cleaner = clean_data(self.data_table)
        self.data_cat = self.cleaner.cat_data()
        self.train_a_model = train_a_model(self.data_cat[0])
        self.train_a_model.check_statistics()
        self.check_data = check_data(self.train_a_model,self.data_cat[0])
        self.Tests = check_data.tests()



if __name__ == __name__:
    controler = controler()