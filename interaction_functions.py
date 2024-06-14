from selenium.webdriver.common.by import By
import time

def realizar_asignacion_y_consentimiento(driver):
    try:
        # Función para hacer clic en el botón de 'Asignación'
        asignacion_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Asignación')]")
        asignacion_button.click()
        print("Botón 'Asignación' clicado con éxito.")

        # Espera corta para que aparezca el botón de consentimiento
        time.sleep(1)  # Ajusta el tiempo según sea necesario

        # Función para aceptar el consentimiento de seguridad
        consentimiento_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Estoy enterado y acepto las medidas de seguridad en el campus')]")
        consentimiento_button.click()
        print("Botón 'Estoy enterado y acepto' clicado con éxito.")

    except Exception as e:
        print(f"Error: {str(e)}")
