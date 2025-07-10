

class clean_data:
    def __init__(self,data_table):
        self.data_table = data_table
        self.train_set = None
        self.test_set = None

    def remove_none(self):
        self.data_table = self.data_table.dropna()
        return self.data_table

    def cat_data(self):
        index,column = self.data_table.shape
        end = int(index*70/100)
        self.train_set = self.data_table.iloc[:end]
        self.test_set = self.data_table.iloc[end:]
        return self.train_set,self.test_set

    def