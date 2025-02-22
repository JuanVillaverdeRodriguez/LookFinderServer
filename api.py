from fastapi import FastAPI, File, HTTPException, UploadFile, Path
import os

from fastapi.staticfiles import StaticFiles

app = FastAPI()

UPLOAD_FOLDER = "uploads"
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    try:
        if not file.filename.lower().endswith((".jpg", ".jpeg")):
            raise HTTPException(status_code=400, detail="Solo se permiten archivos JPG")

        file_location = os.path.join(UPLOAD_FOLDER, file.filename)

        with open(file_location, "wb") as f:
            f.write(await file.read())

        return {"url": f"https://lookfinderserver-production.up.railway.app/uploads/{file.filename}"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

@app.get("/") 
def read_root():
    return {"message": "API funcionando correctamente"}