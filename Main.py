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
        
        # Espera hasta que el botón de iniciar sesión sea clicable y luego haz clic
        sign_in_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'idSIButton9'))
        )
        sign_in_button.click()
        print("Botón de iniciar sesión clicado con éxito")
        
        # Espera hasta que el campo para el código 2FA esté presente
        code_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'idTxtBx_SAOTCC_OTC'))
        )
        print("Campo de código 2FA encontrado")

        # Solicita al usuario que ingrese el código 2FA manualmente
        code = input("Ingrese el código de autenticación de dos factores (2FA): ")
        code_field.send_keys(code)
        print("Código 2FA ingresado")

        # Espera hasta que el botón de verificación sea clicable y luego haz clic
        verify_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'idSubmit_SAOTCC_Continue'))
        )
        verify_button.click()
        print("Botón de verificar clicado con éxito")

        # Ahora esperamos a que aparezca la opción de mantener sesión iniciada
        kmsi_checkbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'KmsiCheckboxField'))
        )
        kmsi_checkbox.click()
        print("Opción de mantener sesión iniciada marcada")
        
        # Presiona el botón de continuar después de marcar la opción
        continue_button = driver.find_element(By.ID, 'idSIButton9')
        continue_button.click()
        print("Botón de continuar clicado con éxito después de marcar la opción")
        
        # Espera a que el botón "Sí" esté presente y haz clic en él
        yes_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'idSIButton9'))
        )
        yes_button.click()
        print("Botón 'Sí' clicado con éxito")
        
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
