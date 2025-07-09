from classification.train_a_model import train_a_model


class check_data:

    def __init__(self,dict_result, to_check: dict):
        self.dict_result = dict_result
        self. to_check = to_check

    def tests(self):
        temp = 1
        dict_probability = {}
        for group, group_dict in self.dict_result.items():
            for dic, parm in self.to_check.items():
                if parm in group_dict.get(dic, {}):
                    temp *= group_dict[dic][parm]
                    dict_probability[group] = temp
                else:
                    raise "error"
        best_group = max(dict_probability, key=dict_probability.get)
        best_prob = dict_probability[best_group]
        return self.dict_result, dict_probability, best_group, best_prob