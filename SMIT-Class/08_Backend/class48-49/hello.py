from fastapi import FastAPI
import json

app=FastAPI()

def load_data():

    with open("data.json", "r") as f:
        data = json.load(f)
        return data 
    
def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

@app.get("/")
def first():
    return {"Messagre": "hello world"}@app.get("/view")

def secound():
    data = load_data()
    return data

@app.post("/patient")
def creat_patinet(patident_id: str, patient_data: dict):
    # data is now a proper Python dictionary
    data = load_data()
    if patident_id in data:
        return {"error": "Yeh patient pehlai sai exist krta hai"}
    # Now this assignment will work successfully
    data[patident_id] = patient_data
    # (Optional) Save the updated dictionary back to your JSON file
    save_data(data)
    return {
        "message": "patient succesfut add hogia",
        "patient_id": patident_id,
        "patient_data": patient_data,
    }
@app.put("/update")
def update_data(paitent_id:str,paitent_data: dict):
    data = load_data()
    if paitent_id not in data:
        return{"Message": "Not Found"}
    data[paitent_id].update([paitent_data])
    save_data(data)
    return{
        "message" : "Paitient Updated",
        "paitent_id" : paitent_id,
        "paitent_data" : paitent_data
    }

@app.delete("/delete")
def delete_data(paitent_id: str):
    data = load_data()
    if paitent_id not in data:
        return {"Message": "Not Found"}
    deleted_patient = data.pop(paitent_id)
    save_data(data)
    return {
        "message": "Paitient Deleted",
        "paitent_id": paitent_id,
        "paitent_data": deleted_patient
    }
    