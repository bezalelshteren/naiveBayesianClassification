from classification.train_a_model import train_a_model


class check_data:
    def __init__(self):
        self.dict_result =
    def p(dict_result: dict, to_check: dict):
        temp = 1
        dict_probability = {}
        for group, group_dict in dict_result.items():
            for dic, parm in to_check.items():
                if parm in group_dict.get(dic, {}):
                    temp *= group_dict[dic][parm]
                    dict_probability[group] = temp
                else:
                    raise "error"
        best_group = max(dict_probability, key=dict_probability.get)
        best_prob = dict_probability[best_group]
        return dict_result, dict_probability, best_group, best_prob