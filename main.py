from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello! My first API is working."}
@app.get("/coffees")
def get_coffees():
    return {
         "coffees": ["Latte" ,"Cappuccino" "Espresso"]
           }
