import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def enter_page():
    p = "welcome to the naivi baice project !"

    def choise_your_path(choise:int):
        if choise == 1:
            get_parm_to_check()
        if choise == 2:
            get_csv_file()
    return p


@app.get("/readCsv")
def get_csv_file(path: str = r"C:\Users\User\Downloads\buy_computer_data.csv"):
    return {"index of data": path}

@app.get("/parm")
def get_parm_to_check():
    pass


if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
