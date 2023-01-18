from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
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
precio = []
m2_a_l_estac = []
direccion = []
# Hacer un "bucle for" a la lista de productos (cada "product" representa un audiolibro)
for product in products:
    # Usamos la funcion "contains" para buscar elementos que contienen un texto en particular, así evitamos construir XPath largos
    precio.append(product.find_element(By.XPATH, './/div[@class="sc-b38b1161-1 bsdIdD"]').text)  # Almacenando data en la lista
    m2_a_l_estac.append(product.find_element(By.XPATH, './/ul[@class="sc-b38b1161-3 ebLhta"]').text)
    direccion.append(product.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div[1]/div/div[3]/div/div[2]/section/section/section[2]/section/div[2]/a/h2').text)




driver.quit()
# Almacenando data en un dataframe y exportando a un archivo CSV
data_venta = pd.DataFrame({'info': precio, 'm2_a_l_estac':m2_a_l_estac, 'direccion':direccion})
data_venta.to_csv('propiedades_com.csv', index=False)