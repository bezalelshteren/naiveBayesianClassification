from data_manage.dal import Dal
from classification.check_data import Check_data
from classification.train_a_model import train_a_model
from data_manage.cleaner import clean_data
import loger.logs_for_server
import logging
logging.info("גקכעאיחלצ")


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
            # column = self.del_data.choose_which_column()
            print(1)
            column = "buys_computer"
            logging.info("choose_which_column by controler")
            return column
        except Exception as e:
            logging.error(f"make_all_desition{e}")

    def colum(self,column):
        try:
            self.cleaner = clean_data(self.data_table_from_dal)
            logging.info("make a instance for cleaner")
            train, test_dict, self.score_dict = self.cleaner.run_all(column)
            logging.info("make all ready to prediction")
            self.train_a_model = train_a_model(train)
            print(2)
            logging.info("train the model")
            return column
        except Exception as e:
            logging.error(f"the train in the controller {e}")
    #
    # def column(self):
    #     print(6)
    #     column = self.train_a_model.choose_which_column()
    #     return column

    def cuntinue(self,column):
        try:
            self.data_to_the_tests,p = self.train_a_model.check_statistics(column)
            logging.info("train successfully ")
            self.check_data = Check_data( self.data_to_the_tests,column)
            logging.info("instance of check_data")
            print(3)
            self.col = column
        except Exception as e:
            logging.error(f"make all test in controller {e}")


    def chose_whet_param(self,chose:int,dict_to_pradict={'age': ">40", 'income': "medium", 'student': "yes", 'credit_rating': "fair"}):
        try:
            if chose == 1:
                self.Tests = self.check_data.tests(dict_to_pradict)
                print(4)
                logging.info("check_data of 1 dict")
            if chose == 2:
                self.check_data = Check_data(self.data_to_the_tests,self.col)
                print(5)
                self.Tests = self.check_data.check_all_data(self.score_dict)
                self.mount = self.check_data.test_whe_mach_corectly()
                logging.info("test_whe_mach_correctly in all data !!")
            print(f"wwwwwwwwwwwwwwwwwwwwwwwwwwwww {self.Tests}")
            return self.Tests
        except Exception as e:
            logging.error(f"make prediction {e}")


    def __repr__(self):
        print("ראפר מופעל")
        return f"Test results: {self.Tests}"


# if __name__ == "__main__":
#     controler1 = controler12()
#     p = controler1.make_all_desition()
#     controler1.colum(p)
#     # p = controler1.column()
#     controler1.cuntinue(p)
#     controler1.chose_whet_param(1)
#     print(controler1)

    print("\nPrediction Results Summary:\n")

    # results = controler1.Tests
    # if isinstance(results, tuple):
    #     results = [results]
    #
    # for i, res in enumerate(results):
    #     prediction = res[0]  # מה המודל ניבא
    #     score = res[1]  # מה הייתה ההסתברות (לוג)
    #     print(f"Test {i + 1}: Predicted = {prediction}, Score = {score:.4f}")

    # {'age': ">40", 'income': "medium", 'student': "yes", 'credit_rating': "fair"}
#     {'age': ">40", 'income': "medium", 'student': "yes", 'credit_rating': "fair"}

