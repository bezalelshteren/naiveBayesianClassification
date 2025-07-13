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
    return chose_whet_param()

@app.get("/params")
def chose_whet_param(choose:int):
    controler1.chose_whet_param(choose)

@app.get("/readCsv")
def get_csv_file(path: str = r"C:\Users\User\Downloads\buy_computer_data.csv"):
    return {"index of data": path}

@app.get("/parm")
def get_parm_to_check():
    pass

@app.get("/dfprediction")
def prediction_to_df():
    pass


if __name__ == "__main__":
    controler1 = controler()
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
    print(controler1)