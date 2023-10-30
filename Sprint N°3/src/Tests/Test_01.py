'''
Created on 26 oct. 2023

@author: joeln
'''
import unittest
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
import pytest
class Test_01(unittest.TestCase):


    def setUp(self, URL=ini.URL):
        self.driver = webdriver.Chrome() #Abrir Chrome
        self.driver.implicitly_wait(10) #Esperamos 10 segundos para continuar (para que se cargue por completo)
        self.driver.maximize_window() #Maximizamos la ventana
        self.driver.get(URL)
    
    def test_01(self):
        #Ingresamos a la sección MUJER
        Selenium.get_json_file(self, "nav_items")
        Selenium.get_elements(self, "Mujer").click()
        time.sleep(2)
        #Rechazamos las cookies
        Selenium.get_elements(self,"ad").click()
        self.assertEqual("Colección Mujer en Grimoldi", self.driver.title, 'El titulo de la pagina "mujer" no coincide con la solicitada')

        #Sacamos screenshot
        self.driver.save_screenshot("C:\\Users\\joeln\\AppData\\Local\\Programs\\Python\\Python311\\Automation Proyect\\Sprint N°3\\src\\data\\evidencia\\test01\\seccionMujer.png")
       
        #Ingresamos a la sección HOMBRES
        Selenium.get_elements(self,"Hombre").click()
        time.sleep(2)
        self.assertEqual("Colección Hombre en Grimoldi", self.driver.title, 'El titulo de la pagina "hombres" no coincide con el solicitado')
        #Sacamos screenshot
        self.driver.save_screenshot("C:\\Users\\joeln\\AppData\\Local\\Programs\\Python\\Python311\\Automation Proyect\\Sprint N°3\\src\\data\\evidencia\\test01\\seccionHombre.png")
       
       
        #Ingresamos a la sección NIÑOS
        Selenium.get_elements(self,"Nenes").click()
        time.sleep(2)
        self.assertEqual("Colección Niños en Grimoldi", self.driver.title, 'El titulo de la pagina "niños" no coincide con el solicitado')
        #Sacamos screenshot
        self.driver.save_screenshot("C:\\Users\\joeln\\AppData\\Local\\Programs\\Python\\Python311\\Automation Proyect\\Sprint N°3\\src\\data\\evidencia\\test01\\seccionNiños.png")
   
        
        #Ingresamos a la sección ACCESORIOS
        Selenium.get_elements(self,"Accesorios").click()
        time.sleep(2)
        self.assertEqual("Accesorios en Grimoldi", self.driver.title, 'El titulo de la pagina "accesorios" no coincide con el solicitado')
        #Sacamos screenshot
        self.driver.save_screenshot("C:\\Users\\joeln\\AppData\\Local\\Programs\\Python\\Python311\\Automation Proyect\\Sprint N°3\\src\\data\\evidencia\\test01\\seccionAccesorios.png")
      
     
        #Ingresamos a la sección POR OCASIÓN
        Selenium.get_elements(self,"Ocasion").click()
        time.sleep(2)
        self.assertEqual("Por Ocasión en Grimoldi", self.driver.title, 'El titulo de la pagina "Por ocasión" no coincide con el solicitado')
        #Sacamos screenshot
        self.driver.save_screenshot("C:\\Users\\joeln\\AppData\\Local\\Programs\\Python\\Python311\\Automation Proyect\\Sprint N°3\\src\\data\\evidencia\\test01\\seccionOcasion.png")
            #será la misma que accesorios ya que produce un bug
   
        #Ingresamos a la sección MARCAS
        Selenium.get_elements(self,"Marcas").click()
        time.sleep(2)
        self.assertEqual("Por Marcas en Grimoldi", self.driver.title, 'El titulo de la pagina "Marcas" no coincide con el solicitado')
        #Sacamos screenshot
        self.driver.save_screenshot("C:\\Users\\joeln\\AppData\\Local\\Programs\\Python\\Python311\\Automation Proyect\\Sprint N°3\\src\\data\\evidencia\\test01\\seccionMarcas.png")

        
        #Ingresamos a la sección OUTLET
        Selenium.get_elements(self,"outlet").click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.assertEqual("Grimoldi Outlet", self.driver.title, 'El titulo de la pagina "Outlet" no coincide con el solicitado')
        #Sacamos screenshot
        self.driver.save_screenshot("C:\\Users\\joeln\\AppData\\Local\\Programs\\Python\\Python311\\Automation Proyect\\Sprint N°3\\src\\data\\evidencia\\test01\\Outlet.png")
      
        
        
    
        
        
    def tearDown(self):
        self.driver.quit()
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()