import requests
import logging


BASE_URL = "http://127.0.0.1:8000"

logging.info("client created !")

json_send = {
  "column": "buys_computer"
}

def ask_model_training_data(coll):
    try:
        logging.info("is start the client")
        response_data = requests.post(f"{BASE_URL}/get_all_module",json={"column":coll})
        print(response_data.json())
        logging.info("returned from server !",response_data.json())
        return response_data.json()

    except Exception as e:
        logging.error("Error:", e)


# print(ask_model_training_data())