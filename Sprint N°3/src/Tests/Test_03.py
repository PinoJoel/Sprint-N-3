'''
Created on 27 oct. 2023

@author: joeln
'''
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException
from Functions.Functions import Functions as Selenium
from Functions.Inicializar import Inicializar as ini
import pytest_html
import msvcrt;
import unittest
import pytest



class Test03(unittest.TestCase):


    def setUp(self, URL=ini.URL):
        self.driver = webdriver.Chrome() #Abrir Chrome
        self.driver.implicitly_wait(10) #Esperamos 10 segundos para continuar (para que se cargue por completo)
        self.driver.maximize_window() #Maximizamos la ventana
        self.driver.get(URL)

    def test03(self):
        Selenium.get_json_file(self, 'nav_items')
        
        Selenium.get_elements(self, 'wishlist').click()     
        self.assertEqual("Mi wishlist", self.driver.title, 'El link de la redirección es erroneo.')
        

    def testName(self):
        self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    pytest.main(["--html=PinoJoel_Test03.html"])
    pytest_html
    unittest.main()