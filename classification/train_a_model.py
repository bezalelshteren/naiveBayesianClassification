import logging
import loger.logs_for_server


class train_a_model:
    def __init__(self,data_table):
        self.dict_result = {}
        self.data_table = data_table



    def check_statistics(self,column = -1):
        try:
            data_table_grouped = self.data_table.groupby(column)

            for name_uniq, dfuniq in data_table_grouped:
                self.dict_result[name_uniq] = {}

                for colume in self.data_table.columns:
                    if colume == column:
                        continue
                    else:
                        count = dfuniq[colume].value_counts(normalize=True).to_dict()
                        self.dict_result[name_uniq][colume] = count
                        logging.info("check_statistics")

            return self.dict_result,column
        except Exception as e:
            logging.error(f"check_statistics {e}")
