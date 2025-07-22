from controler import controler12
from pydantic import BaseModel
# import uvicorn
from fastapi import FastAPI
import logging
from loger import logs_for_server

app = FastAPI()


@app.get("/")
def enter_page():
    # p = "welcome to the naivi baice project !"
    # return p,which_column()
    logging.info("Welcome to the Naive Bayes project!")
    return {"message": "Welcome to the Naive Bayes project!"}

@app.get("/column")
def which_column(column:str):
    p = column
    controler1 = controler12()
    controler1.make_all_desition()
    controler1.colum(p)
    controler1.chose_whet_param(1)
    logging.info(f"message column '{column}' processed successfully")
    return{"message": f"column '{column}' processed successfully."}


@app.get("/readCsv")
def get_csv_file(path: str = r"C:\Users\User\Downloads\buy_computer_data.csv"):
    return {"index of data": path}


# # מודל לקליטת הפרמטרים מהגוף (JSON)
class PredictionRequest(BaseModel):
    column:str = "buys_computer"
    choose:int = 1
    age:str= ">40"
    income:str= "medium"
    student:str= "yes"
    credit_rating:str= "fair"
#
# @app.post("/predict_all")
def full_prediction(request: PredictionRequest):
    logging.info("Received prediction request")

    # שליפת הפרמטרים
    column = request.column
    choose = request.choose
    params = {
        'age': request.age,
        'income': request.income,
        'student': request.student,
        'credit_rating': request.credit_rating
    }

    # פעולות על המודל
    controler1 = controler12()
    controler1.make_all_desition()
    controler1.colum(column)
    controler1.cuntinue(column)
    prediction = controler1.chose_whet_param(choose,params)
    # prediction = controler1.check_data.tests(params)
    print(">>> התחזית שהתקבלה:", prediction)
    logging.info(f"Prediction completed for {params}")

    return {
        "input_parameters": params,
        "selected_column": column,
        "chosen_option": choose,
        "full_prediction": prediction
    }




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
    logging.info("server is run")
    print("server is run")


#     {'age': ">40", 'income': "medium", 'student': "yes", 'credit_rating': "fair"}

