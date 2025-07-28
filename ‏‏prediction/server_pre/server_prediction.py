from fastapi import FastAPI
import logging
# import uvicorn
# from client_prediction import ask_model_training_data
from .client_prediction import ask_model_training_data
from .ceck_all_prediction import Check_data
# from ceck_all_prediction import Check_data
from pydantic import BaseModel


app = FastAPI()
logging.info("app created ")


class PredictionRequest(BaseModel):
    column:str
    choose:int
    age:str
    income:str
    student:str
    credit_rating:str


@app.post("/predict_all")
def predict_all(request: PredictionRequest):
    logging.info("entered to the server !!!")
    # logging.info("Received prediction request")

    # שליפת הפרמטרים
    column = request.column
    choose = request.choose
    params = {
        'age': request.age,
        'income': request.income,
        'student': request.student,
        'credit_rating': request.credit_rating
    }
    dict_resolt = ask_model_training_data(column)
    check_data = Check_data(dict_resolt,column)
    prediction1,answer = check_data.tests(params)
    print(">>> התחזית שהתקבלה:",answer )
    logging.info(">>> התחזית שהתקבלה:",answer )
    # logging.info(f"Prediction completed for {params}")
    # logging.info(prediction1)
    return {
        "input_parameters": params,
        "selected_column": column,
        "chosen_option": choose,
        "full_prediction": prediction1,
        "the result":answer
    }

    # # פעולות על המודל
    # controler1 = controler12()
    # controler1.make_all_desition()
    # controler1.colum(column)
    # controler1.cuntinue(column)
    # prediction = controler1.chose_whet_param(choose,params)
    # # prediction = controler1.check_data.tests(params)
# uvicorn.run("server_prediction:app", host="0.0.0.0", port=8008,reload=True)

    # , reload = True