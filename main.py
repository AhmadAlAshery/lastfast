from fastapi import FastAPI
from urllib.parse import urlparse
import json 
import pandas as pd
import ast

df = pd.read_csv("final.csv")

app = FastAPI()





@app.get("/")
def index():
    return {"Hello": "to Gaurd services"}



@app.get("/check_website/{u}")
def check_url(u : str):
    url = urlparse(u).path.replace("www.", "")
    res = df[df['website'] == url].to_json(orient="split", index=False)
    if len(ast.literal_eval(res)['data'])> 0:
        return ast.literal_eval(res)

    else:
        return "trying to get result"