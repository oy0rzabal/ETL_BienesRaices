from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

web = "https://www.inmuebles24.com/oficinas-en-renta-en-acapulco-de-juarez.html"
path = '/Escritorio/chromedriver'
driver = webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()

# Localizar el contenedor (container) que contiene todos los audiolibros listados en la pagina
container = driver.find_element(By.ID, "root")
# Obtener todos los audiolibros listados (el "/" da los nodos hijos)
products = container.find_elements(By.XPATH, ".//div[@class='sc-1tt2vbg-3 kGTsiT']")
# products = container.find_elements_by_xpath('./li')

# Inicializar el almacenamiento
precio = []
m2_a_l_estac = []
descripcion = []
direccion = []
# Hacer un "bucle for" a la lista de productos (cada "product" representa un audiolibro)
for product in products:
    # Usamos la funcion "contains" para buscar elementos que contienen un texto en particular, así evitamos construir XPath largos
    precio.append(product.find_element(By.XPATH, './/div[@class="sc-i1odl-5 cypYcv"]').text)  # Almacenando data en la lista
    m2_a_l_estac.append(product.find_element(By.XPATH, './/div[@class="sc-i1odl-5 bkbRHX"]').text)
    descripcion.append(product.find_element(By.XPATH, './/div[@class="sc-i1odl-12 kiOjEU"]').text)
    direccion.append(product.find_element(By.XPATH, './/h2[@class="sc-i1odl-10 fzzQwx"]').text)




driver.quit()
# Almacenando data en un dataframe y exportando a un archivo CSV
df_data = pd.DataFrame({'info': precio, 'm2_a_l_estac':m2_a_l_estac, 'descripcion':descripcion, 'direccion':direccion})
df_data.to_csv('info.csv', index=False)
