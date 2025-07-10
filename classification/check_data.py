import math
from imghdr import tests


class check_data:

    def __init__(self,dict_result1):
        self.dict_result = dict_result1


    def tests(self,to_check):
        dict_probability = {}

        for group, group_dict in self.dict_result.items():
            log_sum = 0
            for dic, parm in to_check.items():
                prob = group_dict.get(dic, {}).get(parm, 1e-10)
                if prob == 0:
                    prob = 1e-10

                log_sum += math.log(prob)

            dict_probability[group] = log_sum

        best_group = max(dict_probability, key=dict_probability.get)
        best_prob = dict_probability[best_group]

        return self.dict_result, dict_probability, best_group, best_prob


    def check_all_data(self,dic_all_data):
        list = []
        for dic in dic_all_data:
            ret = self.tests(dic)
            list.append(ret)
        return list