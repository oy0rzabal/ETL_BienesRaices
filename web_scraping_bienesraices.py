from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

#Pagina a Scrapiar: https://www.inmuebles24.com/oficinas-en-renta-en-acapulco-de-juarez.html
#Documentacion a Seguir: https://selenium-python.readthedocs.io/locating-elements.html


web = "https://www.inmuebles24.com/oficinas-en-renta-en-acapulco-de-juarez.html"
path = 'chromedriver'
driver = webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()

# Localizar el contenedor (container) que contiene todos los audiolibros listados en la pagina
container = driver.find_element(By.ID, "root")
# Obtener todos los audiolibros listados (el "/" da los nodos hijos)
products = container.find_elements(By.XPATH, ".//div[@class='sc-1tt2vbg-3 kGTsiT']")
# products = container.find_elements_by_xpath('./li')

# Listas donde se van almacenar nuestra data:
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
data_renta = pd.DataFrame({'info': precio, 'm2_a_l_estac':m2_a_l_estac, 'descripcion':descripcion, 'direccion':direccion})
data_renta.to_csv('rentas.csv', index=False)


#---------------------------------------------------------------WebScraping a ventas--------------------------------------------------------------

web = "https://propiedades.com/acapulco/oficinas-renta"
path = 'chromedriver'
driver = webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()

# Localizar el contenedor (container) que contiene todos los audiolibros listados en la pagina
container = driver.find_element(By.ID, "__next")
# Obtener todos los audiolibros listados (el "/" da los nodos hijos)
products = container.find_elements(By.XPATH, './/section[@class="sc-b38b1161-0 kFFvKh pcom-property-card-body"]')
# products = container.find_elements_by_xpath('./li')

# Inicializar el almacenamiento
precio_2 = []
m2_a_l_estac_2 = []
direccion_2 = []
# Hacer un "bucle for" a la lista de productos (cada "product" representa un audiolibro)
for product in products:
    # Usamos la funcion "contains" para buscar elementos que contienen un texto en particular, así evitamos construir XPath largos
    precio_2.append(product.find_element(By.XPATH, './/div[@class="sc-b38b1161-1 bsdIdD"]').text)  # Almacenando data en la lista
    m2_a_l_estac_2.append(product.find_element(By.XPATH, './/ul[@class="sc-b38b1161-3 ebLhta"]').text)
    direccion_2.append(product.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div[1]/div/div[3]/div/div[2]/section/section/section[2]/section/div[2]/a/h2').text)


driver.quit()

# Almacenando data en un dataframe y exportando a un archivo CSV
def data():
    data_renta = pd.DataFrame({'info': precio_2, 'm2_a_l_estac':m2_a_l_estac_2, 'direccion':direccion_2})
    data_renta.to_csv('rentas_2.csv', index=False)
    


