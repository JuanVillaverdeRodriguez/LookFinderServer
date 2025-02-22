# 1️⃣ Usa una imagen de Python ligera
FROM python:3.9-slim

# 2️⃣ Instalar dependencias del sistema
RUN apt update && apt install -y wget curl unzip google-chrome-stable

# 3️⃣ Instalar ChromeDriver compatible con Chrome
RUN CHROME_VERSION=$(google-chrome --version | awk '{print $3}') && \
    CHROMEDRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION") && \
    wget -q "https://storage.googleapis.com/chrome-for-testing-public/133.0.6943.126/linux64/chromedriver-linux64.zip" -O /tmp/chromedriver.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver

# 4️⃣ Agregar ChromeDriver al PATH permanentemente
ENV PATH="/usr/local/bin:$PATH"

# 5️⃣ Configurar el entorno de trabajo
WORKDIR /app
COPY . /app

# 6️⃣ Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# 7️⃣ Exponer el puerto
EXPOSE 8080

# 8️⃣ Comando para iniciar FastAPI
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]