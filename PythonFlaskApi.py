# Para que funcione tuve que selecccionar python internpreter 3.8.3 BASE
#por que en OS terminal alli installe FastAPI
import fastapi
from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI() # To create API object 

""" EXAMPLES of endpoints using get method
# To create endpoint
@app.get("/")
def  home():
    return {"Data" : "Testing"}# return som data that says test

# Create anoter endpoint
@app.get("/about")
def about():
    return{"Data" : "About"}
"""

#PATH/ENDPOINT parameters 
inventory = {
       1: {
           "name": "Milk",
           "price": 3.99,
           "brand": "Regular"
       }        
    }

# end point to retreive for us item information based on its id
@app.get("/get-item/{item_id}")
def get_item(item_id : int = Path(None, description="The ID of the item you would like to view", gt=0, lt=2)):
    return inventory[item_id]# return inventory at item_id

# query parameters
# Mas o menos asi es query parameter lleva un ? es como decir feacebook.com/home?reidrect=/tim&msg=fail
# how do we accept query parameter for our endpoint
@app.get("/get-by-name")# this qery parameter is going to be the name of the item we want to retrieve
def get_item(name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not found"}
        
        


