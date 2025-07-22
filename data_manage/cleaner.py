import logging
import loger.logs_for_server


class clean_data:
    def __init__(self,data_table):
        self.data_table = data_table
        self.score_of_test = None
        self.train_set = None
        self.test_set = None
        self.test_set_cut = None

    def remove_none(self):
        self.data_table = self.data_table.dropna()
        logging.info("remove if filed = None")
        return self.data_table

    def cat_data(self):
        index,column = self.data_table.shape
        end = int(index*70/100)
        self.train_set = self.data_table.iloc[:end]
        self.test_set = self.data_table.iloc[end:]
        logging.info("cat data to 70, 30")
        return self.train_set,self.test_set

    def chaing_data_from_test_to_check(self, data_to_check,column):
        self.test_set_cut = data_to_check.drop(columns=[column])
        logging.info("changing data from test to check")
        return self.test_set_cut

    def chaing_from_df_to_dict(self,data):
        self.test_set = data.to_dict(orient='records')
        logging.info("chaing from df to dict")
        return self.test_set


    def run_all(self,column = -1):
        data_to_train,data_to_test = self.cat_data()#את data_to_test צריך לשלוח לבדיקה כמה אחוזים היא הצליחה ועוד עותק להוריד את השורה של התשובה ולשלוח לטסטים
        data_to_score = self.chaing_data_from_test_to_check(data_to_test,column)
        data_to_test = self.chaing_from_df_to_dict(data_to_test)
        data_to_score = self.chaing_from_df_to_dict(data_to_score)
        return data_to_train ,data_to_test ,data_to_score

