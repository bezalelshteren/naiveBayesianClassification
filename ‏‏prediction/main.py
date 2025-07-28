from server_pre.server_prediction import app
import logging
import uvicorn
if __name__ == "__main__":
    logging.info("server is running")
    uvicorn.run(app, host="0.0.0.0", port=8004)
    logging.info("server is finish !!!")