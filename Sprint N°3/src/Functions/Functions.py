
from selenium import webdriver
from Functions.Inicializar import Inicializar
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,NoAlertPresentException,NoSuchWindowException, \
 UnexpectedAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import string
import pytest
import unittest
import json
from test.test_tomllib.test_data import json_path




class Functions(Inicializar): #Le pasamos como parámetro la clase Inicializar


    def _init_(self):
        self.json_GetFieldBy = None
        self.json_ValueToFind = None 
    
    def tearDown(self):
        self.driver.quit()
        
    def get_json_file(self, file):
        """para abrir el archivo"""
        json_path = Inicializar.Json + "/" + file + '.json'
        #para traenos el archivo
        try:
            with open(json_path, "r") as read_file:
                self.json_strings = json.loads(read_file.read())
                print("get_json_file: " + json_path)
                return self.json_strings
        except FileNotFoundError:
            self.json_strings = False
            Functions.tearDown(self)
            pytest.skip("get_json_file: No se encontro el Archivo " + file)
    
    def get_entity(self,entity):
        if self.json_strings is False:
            print("Define el DOM para este TC")
        else:
            try:
                self.json_ValueToFind = self.json_strings[entity]["ValueToFind"]
                self.json_GetFieldBy = self.json_strings[entity]["GetFieldBy"]
                return True
            except KeyError:
                self.msj = "get_entity: No se encontro la key a la cual se hace referencia: " + entity
                Functions.tearDown(self, "fail")
                pytest.skip(self.msj) #se skipea el paso

    def get_elements(self,entity, MyTextElement=None):
        Get_Entity = Functions.get_entity(self, entity)
        
        if Get_Entity is None:
            print ('No se encontró el valor en el Json definido')
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element(By.ID,(self.json_ValueToFind))

                if self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element(By.NAME,(self.json_ValueToFind))

                if self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)
                    elements = self.driver.find_element(By.XPATH,(self.json_ValueToFind))
                    
                if self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element(By.PARTIAL_LINK_TEXT,(self.json_ValueToFind))

                if self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_element(By.CSS_SELECTOR,(self.json_ValueToFind))

                if self.json_GetFieldBy.lower() == "class":
                    elements = self.driver.find_element(By.CLASS_NAME,(self.json_ValueToFind))
                print("get_elements: " + self.json_ValueToFind)
                return elements
            
            except AttributeError:
                self.msj = ("get_elements AttributeError: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self, "fail")
                
            except NoSuchElementException:
                self.msj = ("get_elements NoSuchElementException: No se encontró el elemento: "+ self.json_ValueToFind)
                Functions.tearDown(self, "fail")
                
            except TimeoutException:
                self.msj = ("get_elements TimeoutException: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self, "fail")
                
            except UnexpectedAlertPresentException as e:
                self.msj = "get_elements: " + str(e)
                Functions.close_all_alerts(self)
                Functions.tearDown(self, "fail")