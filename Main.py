from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from login_utils import login
import time

def main():
    # Configura el controlador del navegador utilizando webdriver_manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Datos de inicio de sesión (podrían ser obtenidos de un archivo de configuración o similar)
    username = 'cru23110@uvg.edu.gt'
    password = 'F8STJFGVLfGZsqr'

    # Llama a la función de inicio de sesión
    login(driver, username, password)

    # Pausa para ver el resultado antes de cerrar el navegador
    time.sleep(10)

    # Cierra el navegador al final
    driver.quit()

if __name__ == "__main__":
    main()
