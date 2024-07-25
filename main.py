# import pickle

# file= open('classify.pickle', 'rb')
# model= pickle.load(file)
# file.close()

# from fastapi import FastApi

# app= FastAPI()

# @app.get("/")
# def home():
#     return {"msg": "Spam classifier is running"}

# import pickle
# file= open("classify.pickle", 'rb')
# model= pickle.load(file)
# file.close()

# from fastapi import FastAPI
# app = FastAPI()
# from pydantic import BaseModel
# class Data(BaseModel): 
#     email: str@app.get("/")
#     def home(): return {"msg": "Spam classifier is running"}
#     @app.post("/classify")
#     def classify(item:Data): 
#         email = item.email 
#         y_pred = model.predict([email])[0] 
#         return {"label": y_pred}



