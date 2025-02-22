from fastapi import FastAPI, File, UploadFile, Path
import os

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    if not file.filename.lower().endswith((".jpg", ".jpeg")):
        return {"error": "Solo se permiten archivos JPG, tu has subido:" + file.filename}

    file_location = Path(UPLOAD_FOLDER) / file.filename

    with open(file_location, "wb") as f:
        f.write(await file.read())

    return {"url": f"https://lookfinderserver-production.up.railway.app/{file_location}"}

@app.get("/") 
def read_root():
    return {"message": "API funcionando correctamente"}