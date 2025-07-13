from data_manage.dal import Dal
from classification.check_data import Check_data
from classification.train_a_model import train_a_model
from data_manage.cleaner import clean_data

class controler:
    def __init__(self):
        self.make_all_desition()


    def make_all_desition(self):
        self.del_data = Dal()
        # מחזיר לי את הדאטה שקראתי מהCSV
        print(1)
        self.data_table_from_dal = self.del_data.read_the_csv_to_df()
        print(2)
        self.cleaner = clean_data(self.data_table_from_dal)
        print(3)
        train, test_dict, self.score_dict = self.cleaner.run_all()
        print(4)
        # print(train, test_dict, self.score_dict)
        print(5)
        self.train_a_model = train_a_model(train)

    def column(self):
        print(6)
        column = self.train_a_model.choose_which_column()
        return column

    def cuntinue(self,column):
        self.data_to_the_tests,p = self.train_a_model.check_statistics(column)
        print(7)
        self.check_data = Check_data( self.data_to_the_tests,column)
        print(8)
        self.col = column


    def chose_whet_param(self,chose:int):
        # chose = int(input("your choose"))
        if chose == 1:
            self.Tests = self.check_data.tests({'age': ">40", 'income': "medium", 'student': "yes", 'credit_rating': "fair"})
        if chose == 2:
            self.check_data = Check_data(self.data_to_the_tests,self.col)
            self.Tests = self.check_data.check_all_data(self.score_dict)
            self.mount = self.check_data.test_whe_mach_corectly()
        return self.Tests


    def __repr__(self):
        return f"Test results: {self.Tests}"


if __name__ == "__main__":
    controler1 = controler()
    p = controler1.column()
    controler1.cuntinue(p)
    controler1.chose_whet_param(2)
    print(controler1)

    print("\nPrediction Results Summary:\n")

    results = controler1.Tests
    if isinstance(results, tuple):
        results = [results]

    for i, res in enumerate(results):
        prediction = res[0]  # מה המודל ניבא
        score = res[1]  # מה הייתה ההסתברות (לוג)
        print(f"Test {i + 1}: Predicted = {prediction}, Score = {score:.4f}")

    # {'age': ">40", 'income': "medium", 'student': "yes", 'credit_rating': "fair"}

