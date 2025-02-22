from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



def scrape_image(url: str) -> str:
    # Configurar opciones de Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Para no abrir la ventana del navegador
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Evita detección de bot
    chrome_options.add_argument("start-maximized")  # Maximizar pantalla
    chrome_options.add_argument("disable-infobars")  # Ocultar notificaciones de automatización
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-webgl")

    # Cambiar User-Agent a uno real
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    chrome_options.add_argument(f"user-agent={user_agent}")

    # Inicializar WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Abrir la página
    url = "https://www.zara.com/es/en/bear-print-sweatshirt-p02511601.html"
    driver.get(url)

    try:
        imagen = driver.find_element(By.CSS_SELECTOR, ".media-image__image.media__wrapper--media")
        imagen_url = imagen.get_attribute("src")
        print("Imagen encontrada:", imagen_url)
    except:
        print("No se encontró la imagen.")

    driver.quit()