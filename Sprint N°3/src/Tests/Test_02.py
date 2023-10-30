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
import msvcrt;
import unittest
import pytest_html
import pytest


class Test02(unittest.TestCase):


    def setUp(self, URL=ini.URL):
        self.driver = webdriver.Chrome() #Abrir Chrome
        self.driver.implicitly_wait(10) #Esperamos 10 segundos para continuar (para que se cargue por completo)
        self.driver.maximize_window() #Maximizamos la ventana
        self.driver.get(URL)


    def test02(self):
        Selenium.get_json_file(self, 'nav_items')
        
        #Comparamos label de mujer.
        self.assertEqual("MUJER",Selenium.get_elements(self, "Mujer").text,"El label del enlace a la colección mujer no es correcto.")

        #Comparamos label de hombre.
        self.assertEqual("HOMBRE",Selenium.get_elements(self, "Hombre").text,"El label del enlace a la colección hombre no es correcto.")

        #Comparamos label de niños.
        self.assertEqual("NIÑOS",Selenium.get_elements(self, "Nenes").text,"El label del enlace a la seccion niños no es correcto.")

        #Comparamos label de accesorios.
        self.assertEqual("ACCESORIOS",Selenium.get_elements(self, "Accesorios").text,"El label del enlace a la sección accesorios no es correcto.")

        #Comparamos label de por ocasión.
        self.assertEqual("POR OCASIÓN",Selenium.get_elements(self, "Ocasion").text,"El label del enlace a la sección por ocasion no es correcto.")
        
        #Comparamos label de marcas.
        self.assertEqual("MARCAS",Selenium.get_elements(self, "Marcas").text,"El label del enlace a la sección marcas no es correcto.")
        
        #Comparamos label de Outlet.
        self.assertEqual("OUTLET",Selenium.get_elements(self, "outlet").text,"El label del enlace a la sección outlet no es correcto.")
        
        #Sacamos screenshot
        self.driver.save_screenshot("C:\\Users\\joeln\\AppData\\Local\\Programs\\Python\\Python311\\Automation Proyect\\Sprint N°3\\src\\data\\evidencia\\test02\\Labels.png")

    def testName(self):
        self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()