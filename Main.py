from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from login_utils import login
from interaction_functions import realizar_asignacion_y_consentimiento
import time

def main():
    # Configura el controlador del navegador utilizando webdriver_manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Datos de inicio de sesión (podrían ser obtenidos de un archivo de configuración o similar)
    username = 'cru23110@uvg.edu.gt'
    password = 'F8STJFGVLfGZsqr'

    # Llama a la función de inicio de sesión
    login(driver, username, password)
    
    # Espera corta para asegurar que la página cargue completamente después del login
    time.sleep(1)  # Ajusta el tiempo según sea necesario

    # Llama a la función para realizar la asignación y aceptar el consentimiento
    realizar_asignacion_y_consentimiento(driver)

    # Pausa para ver el resultado antes de cerrar el navegador
    time.sleep(10)

    # Cierra el navegador al final
    driver.quit()

if __name__ == "__main__":
    main()
