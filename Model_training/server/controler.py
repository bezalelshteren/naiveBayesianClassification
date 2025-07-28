from Model_training.data_manage.dal import Dal
from Model_training.classification.train_a_model import train_a_model
from Model_training.data_manage.cleaner import clean_data
import logging


class controler12:
    def __init__(self):
        # self.make_all_desition()
        # self.Tests =None
        pass

    def make_all_desition(self):
        try:
            self.del_data = Dal()
            logging.info(" מחזיר לי את הדאטה שקראתי מהCSV")
            self.data_table_from_dal = self.del_data.read_the_csv_to_df()
            print(1)
            logging.info("choose_which_column by controler")
        except Exception as e:
            logging.error(f"make_all_desition{e}")


    def colum(self,column):
        try:
            train = clean_data(self.data_table_from_dal)
            logging.info("make a instance for cleaner")
            # train = self.cleaner.data_table
            print(train)
            logging.info("make all ready to prediction")
            self.train_a_model = train_a_model(train)
            print(2)
            logging.info("train the model")
            print("============")
        except Exception as e:
            logging.error(f"the train in the controller {e}")


    def cuntinue(self,column):
        try:
            print(3)
            data_to_the_tests = self.train_a_model.check_statistics(column)
            logging.info("train successfully ")
            # print(data_to_the_tests,"פפפפפפפ")
            return data_to_the_tests
        except Exception as e:
            logging.error(f"make all test in controller {e}")


