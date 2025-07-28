from .controler import controler12
from fastapi import FastAPI
from pydantic import BaseModel
import logging

app = FastAPI()



class ColumnRequest(BaseModel):
    column: str



@app.get("/")
def enter_page():
    logging.info("Welcome to the Naive Bayes project!")
    return {"message": "Welcome to the Naive Bayes project!"}



@app.post("/readCsv")
def get_csv_file(path: str =  r"C:\Users\User\Downloads\phishing.csv"):
    return {"index of data": path}


@app.post("/get_all_module")
def get_all_module(requsts:ColumnRequest):
    column1 = requsts.column
    print(">>> column1 =", column1)
    controler21 = controler12()
    controler21.make_all_desition()
    controler21.colum(column1)
    data_to_the_client = controler21.cuntinue(column1)
    return data_to_the_client
# {"the data returned ":