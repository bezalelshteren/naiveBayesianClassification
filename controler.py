from data_manage.dal import Dal
from classification.check_data import check_data
from classification.train_a_model import train_a_model
# from data_manage.cleaner import clean_data

class controler:
    def __init__(self):
        self.del_data = Dal()
        self.check_data = check_data()
        self.train_a_model = train_a_model()