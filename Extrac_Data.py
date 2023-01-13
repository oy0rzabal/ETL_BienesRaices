#Impport library:
import random
from time import sleep
from selenium import webdriver

#controlamos el webdriver:
def setup(self):
    self.driver = webdriver.Chrome('./chromediver.exe')

def test_search(self):
    driver = self.driver
    driver.get("https://www.inmuebles24.com/oficinas-en-venta-q-acapulco.htmlv") #Mandame a llamar la pagina
    self.casas = driver.find_elemtns_by_xpath('//div[@class="sc-1tt2vbg-3 kGTsiT"]')

def extrac_data_test(sel):
    casa = self.casas
    for i in casa:
        precio = casa.find_element_by_xpath('.//div[@class="sc-12dh9kl-3 gGCVnu"]').text
        localizacion = casa.find_element_by_xpath('//div[@class="sc-ge2uzh-2 ggYRKF"]').text
        zona = casa.find_element_by_xpath('//div[@class ="sc-ge2uzh-0 lnBueA"]').text
        m2_estacionamiento = casa.find_element_by_xpath('//div[@class="sc-1uhtbxc-0 cAEjmC"]').text
        direccion = casa.fins_element_by_spath('//div[@class="sc-i1odl-12 bKAWqU"]').text

def tearDown():
    self.driver.close()

if __name__ == '__main__':
    extrac_data_test()