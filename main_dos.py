from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_youtube_comments(video_url):
    # Configura el navegador web (asegúrate de tener ChromeDriver instalado)
    driver = webdriver.Chrome()
    driver.get(video_url)

    try:
        # Espera hasta que aparezca la ventana emergente y acéptala
        WebDriverWait(driver, 10).until(
            EC.alert_is_present(),
        ).accept()

        # Espera a que la página cargue completamente (puedes ajustar este tiempo según sea necesario)
        time.sleep(5)

        # Desplázate hacia abajo para cargar más comentarios (puedes repetir este paso según sea necesario)
        body = driver.find_element_by_tag_name('body')
        for _ in range(3):  # por ejemplo, desplázate 3 veces
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(2)  # espera a que carguen más comentarios

        # Obtén los elementos que contienen los comentarios
        comment_elements = driver.find_elements_by_xpath('//yt-formatted-string[@id="content-text"]')

        # Imprime los comentarios
        for comment in comment_elements:
            print(comment.text)

    finally:
        # Cierra el navegador
        driver.quit()

# Reemplaza 'TU_URL_DEL_VIDEO' con la URL del video de YouTube
video_url = 'https://www.youtube.com/watch?v=0QY4z4IsHSo'
get_youtube_comments(video_url)
