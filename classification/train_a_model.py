

class train_a_model:
    def __init__(self,data_table):
        self.dict_result = {}
        self.data_table = data_table


    def choose_which_column(self):
        column = input("choose which column").strip().strip('"').strip("'")
        return column

    def check_statistics(self,column):
        # self.column = self.choose_which_column()
        data_table_grouped = self.data_table.groupby(column)

        for name_uniq, dfuniq in data_table_grouped:
            self.dict_result[name_uniq] = {}

            for colume in self.data_table.columns:
                if colume == column:
                    continue
                else:
                    count = dfuniq[colume].value_counts(normalize=True).to_dict()
                    self.dict_result[name_uniq][colume] = count

        return self.dict_result,column