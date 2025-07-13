import math



class Check_data:

    def __init__(self,dict_result1,col):
        self.dict_result = dict_result1
        self.list = []
        self.column = col


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

        return   best_group, best_prob

    def check_all_data(self, dic_all_data):
        self.true_labels = []
        for dic in dic_all_data:
            true_label = dic.get(self.column)
            self.true_labels.append(true_label)
            ret = self.tests(dic)
            self.list.append(ret)
        return self.list

    def test_whe_mach_corectly(self):
        correct = 0
        total = len(self.list)

        for i in range(total):
            predicted_label = self.list[i][0]
            true_label = self.true_labels[i]

            if predicted_label == true_label:
                correct += 1

        accuracy = correct / total
        return accuracy
