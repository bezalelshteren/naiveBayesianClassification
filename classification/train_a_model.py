

class train_a_model:
    def __init__(self):
        self.dict_result = {}

    def check_statistics(self,colume_purpose, data_table, x):
        data_table_grouped = data_table.groupby(colume_purpose)
        for name_uniq, dfuniq in data_table_grouped:
            self.dict_result[name_uniq] = {}
            for colume in data_table.columns:
                if colume == colume_purpose:
                    continue
                else:
                    count = dfuniq[colume].value_counts(normalize=True).to_dict()
                    self.dict_result[name_uniq][colume] = count
        return self.dict_result