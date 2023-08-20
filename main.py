from fastapi import FastAPI
from pymongo import MongoClient
import json


connection_string="mongodb+srv://dheerajgajula2202:dheeraj@cluster0.w5zpnhp.mongodb.net/"
connection_string_meta = "mongodb+srv://dheerajgajula2209:dheeraj@cluster0.akjrg3v.mongodb.net/"
client_meta = MongoClient(connection_string_meta)
test_meta = client_meta['test']
meta_data_collection = test_meta['meta_data']
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

@app.get("/meta_data")
def meta_data(pid):
    val = meta_data_collection.find({"asin": pid})
    meta ={}
    for n in val:
        meta = n

    response = {
        "title":meta['title'],
        "category":meta['main_cat'],
        "price": meta['price'],
    }

    return response   
    
    

    
