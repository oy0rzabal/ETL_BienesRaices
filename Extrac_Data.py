#Impport library:
import random
from time from sleep
from selenium import webdriver

#controlamos el webdriver:
def setup(self):
    self.driver = webdriver.Chrome('./chromediver.exe')

def test_search():
    driver = self.driver
    driver.get("https://www.inmuebles24.com/oficinas-en-venta-q-acapulco.htmlv") #Mandame a llamar la pagina
    casas = driver.find_elemtns_by_xpath()


def tearDown():
    self.driver.close()

if __name__ == '__main__':
