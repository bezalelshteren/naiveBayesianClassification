

class clean_data:
    def __init__(self,data_table):
        self.data_table = data_table
        self.score_of_test = None
        self.train_set = None
        self.test_set = None
        self.test_set_cut = None

    def remove_none(self):
        self.data_table = self.data_table.dropna()
        return self.data_table

    def cat_data(self):
        index,column = self.data_table.shape
        end = int(index*70/100)
        self.train_set = self.data_table.iloc[:end]
        self.test_set = self.data_table.iloc[end:]
        return self.train_set,self.test_set

    def chaing_from_df_to_dict(self):
        self.score_of_test,self.test_set = self.cat_data()
        self.test_set_cut = self.test_set.loc[0:-1]
        self.test_set = self.test_set.to_dict(orient='index')
        return self.test_set_cut,self.score_of_test
