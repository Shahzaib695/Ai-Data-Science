from fastapi import FastAPI, HTTPException
from hello import load_data, save_data
app = FastAPI()
data = load_data()
@app.get('/')
def first_api():
    return {"Message": "Hello World"}
@app.get('/about')
def second_api():
    return {"Message": "About Route"}
@app.get('/biodata')
def biodata():
    return {
        "Name": "Shahzaib",
        "Age": "19"
    }
@app.get('/data/{person_id}')
def show_data(person_id: str):
    if person_id not in data:
        raise HTTPException(status_code=404, detail="Person does not exist")
    return data[person_id]
# The original spelling is kept for compatibility with the class example.
@app.post('/paitent')
@app.post('/patient')
def create_patient(patient_id: str, patient_data: dict):
    if patient_id in data:
        raise HTTPException(status_code=409, detail="Patient already exists")
    data[patient_id] = patient_data
    save_data(data)
    return{
        "Message": "New Patient Id Added",
        "Patient_id": patient_id,
        "Patient_data": patient_data
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