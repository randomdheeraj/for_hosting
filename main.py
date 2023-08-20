from fastapi import FastAPI
from pymongo import MongoClient
import json


connection_string="mongodb+srv://dheerajgajula2202:dheeraj@cluster0.w5zpnhp.mongodb.net/"
client = MongoClient(connection_string)
test = client['rough']
test_collection = test['test']

app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "World"}

@app.get("/order_list")
def order_list(user_id):
    print(user_id)
    val = test_collection.find({"user_id": user_id})
    dict_array =[]
    for n in val:
        dict_array.append(n)
    json_arr=[]
    for dics in dict_array:
        temp = {"product_id":dics['product_id'],"rating":dics['rating']}
        json_arr.append(temp)
    
    final_json = json.dumps(json_arr)
    return final_json

@app.get("/high_rating")
def high_rating(user_id):
    print(user_id)
    val=test_collection.find({"user_id": user_id})
    dict_array =[]
    for n in val:
        dict_array.append(n)
    higest_rating = max(dict_array, key=lambda x:x['rating'])
    response = {"product_id":higest_rating['product_id'],"rating":higest_rating['rating']}
    print(response)
    return response
    
    

    
