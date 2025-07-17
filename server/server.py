from controler import controler
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def enter_page():
    p = "welcome to the naivi baice project !"
    return p,which_column()

@app.get("/column")
def which_column(column:str):
    controler1.cuntinue(column)
    return

@app.get("/params")
def chose_whet_param(choose:int):
    controler1.chose_whet_param(choose)
    return

@app.get("/readCsv")
def get_csv_file(path: str = r"C:\Users\User\Downloads\buy_computer_data.csv"):
    return {"index of data": path}

@app.get("/parm")
def get_parm_to_check():
    pass

@app.get("/dfprediction")
def prediction_to_df():
    pass

@app.get("/predict_all")
def full_prediction(
    column: str,
    choose: int,
    params:dict
    # age: str,
    # income: str,
    # student: str,
    # credit_rating: str
):
    controler1.cuntinue(column)
    controler1.chose_whet_param(choose)
    # params = {
        # 'age': age,
        # 'income': income,
        # 'student': student,
        # 'credit_rating': credit_rating
    # }
    prediction = controler1.check_data.tests(params)
    return {"full_prediction": prediction}



if __name__ == "__main__":
    controler1 = controler()
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
    print(controler1)
