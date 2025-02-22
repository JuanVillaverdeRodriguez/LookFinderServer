from fastapi import FastAPI, File, UploadFile
import os

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    file_location = f"{UPLOAD_FOLDER}/{file.filename}"
    
    with open(file_location, "wb") as f:
        f.write(await file.read())

    return {"url": f"https://tu-servidor.com/{file_location}"}

@app.get("/") 
def read_root():
    return {"message": "API funcionando correctamente"}