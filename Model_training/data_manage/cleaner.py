import logging


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
