from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configura el controlador del navegador utilizando webdriver_manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Función para iniciar sesión
def login(username, password):
    driver.get('https://asignaciones.uvg.edu.gt/home')

    try:
        # Espera a que el campo de email esté presente y luego ingresa el nombre de usuario
        email_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'i0116'))
        )
        email_field.send_keys(username)
        print("Campo de email encontrado y nombre de usuario ingresado")
        
        # Presiona el botón de siguiente
        next_button = driver.find_element(By.ID, 'idSIButton9')
        next_button.click()
        print("Botón de 'Siguiente' clicado con éxito")
        
        # Espera a que el campo de contraseña esté presente
        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'i0118'))
        )
        password_field.send_keys(password)
        print("Campo de contraseña encontrado y contraseña ingresada")
        
        # Presiona el botón de iniciar sesión
        sign_in_button = driver.find_element(By.ID, 'idSIButton9')
        sign_in_button.click()
        print("Botón de iniciar sesión clicado con éxito")
        
        print("Login realizado con éxito")
    except Exception as e:
        print(f"Error durante el inicio de sesión: {e}")

# Datos de inicio de sesión
username = 'cru23110@uvg.edu.gt'
password = 'F8STJFGVLfGZsqr'

# Iniciar sesión
login(username, password)

# Pausar para ver el resultado antes de cerrar el navegador
time.sleep(10)

# Cerrar el navegador al final
driver.quit()
