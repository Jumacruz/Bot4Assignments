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

def verificar_y_asignar_cursos(driver, cursos):
    # Iterar sobre la lista de cursos proporcionados
    for curso in cursos:
        codigo_curso = curso['Codigo del curso']
        seccion_A = curso['opcion A']
        seccion_B = curso['opcion B']

        # Encontrar el botón del curso por su código
        xpath_curso = f"//span[contains(text(), '{codigo_curso}')]"
        curso_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_curso)))
        curso_element.click()

        # Esperar a que se cargue la tabla de secciones
        xpath_tabla_secciones = "//div[@class='table-responsive mb-3']//table"
        tabla_secciones = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath_tabla_secciones)))

        seccion_encontrada = False

        # Intentar primero con la sección A y luego con la B si es necesario
        for seccion_numero in [seccion_A, seccion_B]:
            try:
                # Encontrar la fila de la sección deseada por su número
                xpath_fila_seccion = f"//tr[contains(., '{seccion_numero}')]"
                fila_seccion = tabla_secciones.find_element(By.XPATH, xpath_fila_seccion)

                # Obtener datos de la sección
                disponibles = int(fila_seccion.find_element(By.XPATH, ".//div[contains(., 'Disponibles')]//strong").text.strip())
                cupo_maximo = int(fila_seccion.find_element(By.XPATH, ".//div[contains(., 'Cupo')]//strong").text.strip())

                # Verificar disponibilidad y asignarse si es posible
                if disponibles > 0:
                    # Hacer clic en el botón "Asignarse"
                    try:
                        boton_asignarse = fila_seccion.find_element(By.XPATH, ".//button[contains(@title, 'Asignarse')]")
                        boton_asignarse.click()
                        seccion_encontrada = True
                        break  # Salir del bucle si se pudo asignar
                    except Exception as e:
                        print(f"No se pudo hacer clic en 'Asignarse' para la sección {seccion_numero}: {str(e)}")
                else:
                    print(f"No hay disponibilidad en la sección {seccion_numero} del curso {codigo_curso}")

            except Exception as e:
                print(f"No se encontró la sección {seccion_numero} del curso {codigo_curso}: {str(e)}")

                # Si no se encontró la sección deseada, intentar con secciones cercanas
                if not seccion_encontrada:
                    print(f"Intentando con secciones cercanas para el curso {codigo_curso} y sección {seccion_numero}")
                    secciones_cercanas = [str(int(seccion_numero) - 1), str(int(seccion_numero) + 1)]

                    for seccion_cercana in secciones_cercanas:
                        try:
                            xpath_fila_seccion_cercana = f"//tr[contains(., '{seccion_cercana}')]"
                            fila_seccion_cercana = tabla_secciones.find_element(By.XPATH, xpath_fila_seccion_cercana)

                            disponibles = int(fila_seccion_cercana.find_element(By.XPATH, ".//div[contains(., 'Disponibles')]//strong").text.strip())
                            cupo_maximo = int(fila_seccion_cercana.find_element(By.XPATH, ".//div[contains(., 'Cupo')]//strong").text.strip())

                            if disponibles > 0:
                                try:
                                    boton_asignarse = fila_seccion_cercana.find_element(By.XPATH, ".//button[contains(@title, 'Asignarse')]")
                                    boton_asignarse.click()
                                    seccion_encontrada = True
                                    break  # Salir del bucle si se pudo asignar
                                except Exception as e:
                                    print(f"No se pudo hacer clic en 'Asignarse' para la sección {seccion_cercana}: {str(e)}")
                            else:
                                print(f"No hay disponibilidad en la sección {seccion_cercana} del curso {codigo_curso}")

                        except Exception as e:
                            print(f"No se encontró la sección {seccion_cercana} del curso {codigo_curso}: {str(e)}")

        if not seccion_encontrada:
            print(f"No se encontró una sección disponible para el curso {codigo_curso}")

        # Cerrar el detalle del curso para prepararse para el siguiente
        curso_element.click()