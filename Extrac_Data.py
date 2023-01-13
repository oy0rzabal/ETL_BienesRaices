#Impport library:
import random
from time from sleep
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
        precio = self.casas.find_element_by_xpath('.//div[@class="sc-12dh9kl-3 gGCVnu"]')
        localizacion = self.casas.find_element_by_xpath('//div[@class="sc-ge2uzh-2 ggYRKF"]')
        zona = self.casas.find_element_by_xpath('//div[@class ="sc-ge2uzh-0 lnBueA"]')
        m2_estacionamiento = self.casas.find_element_by_xpath('//div[@class="sc-1uhtbxc-0 cAEjmC"]')
        direccion = self.casas.fins_element_by_spath('//div[@class="sc-i1odl-12 bKAWqU"]')

def tearDown():
    self.driver.close()

if __name__ == '__main__':
    extrac_data_test()