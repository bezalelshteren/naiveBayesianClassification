from data_manage.dal import Dal
from classification.check_data import Check_data
from classification.train_a_model import train_a_model
from data_manage.cleaner import clean_data

class controler:
    def __init__(self):
        self.del_data = Dal()
        # מחזיר לי את הדאטה שקראתי מהCSV
        self.data_table_from_dal = self.del_data.read_the_csv_to_df()
        self.cleaner = clean_data(self.data_table_from_dal)
        train, test_dict, score_dict = self.cleaner.run_all()
        print(train, test_dict, score_dict)
        self.train_a_model = train_a_model(train)
        dict_result = self.train_a_model.check_statistics()
        self.data_to_the_tests,p = self.train_a_model.check_statistics()
        self.check_data = Check_data(dict_result)
        # self.Tests = self.check_data.tests({'age': ">40", 'income': "medium", 'student': "yes", 'credit_rating': "fair"})
        self.check_data = Check_data(self.data_to_the_tests)
        self.Tests = self.check_data.check_all_data(score_dict)



    def __repr__(self):
        return f"Test results: {self.Tests}"


if __name__ == "__main__":
    controler1 = controler()
    print(controler1)

    print("\nPrediction Results Summary:\n")
    for i, res in enumerate(controler1.Tests):
        prediction = res[2]       # מה המודל ניבא
        score = res[3]            # מה הייתה ההסתברות (לוג)
        print(f"Test {i + 1}: Predicted = {prediction}, Score = {score:.4f}")

    # {'age': ">40", 'income': "medium", 'student': "yes", 'credit_rating': "fair"}