from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Firefox, FirefoxProfile, Remote
from selenium.common.exceptions import NoSuchElementException,\
                                       TimeoutException,\
                                       ElementClickInterceptedException,\
                                       NoSuchWindowException,\
                                       WebDriverException,\
                                       ElementNotInteractableException
from base64 import b64decode
# available since 2.4.0
from selenium.webdriver.support.ui import WebDriverWait
# available since 2.26.0
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from re import search
from csv import DictWriter
from sys import argv, stdout, exit
from time import sleep, time
from selenium.webdriver.firefox.options import Options
from logging import getLogger, INFO, StreamHandler, Formatter
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from urllib3.exceptions import MaxRetryError
from selenium.webdriver.common.keys import Keys
import time
import sys
import threading

#options = Options()
#options.add_argument("--headless")
#driver = webdriver.Firefox(options=options)
#driver = webdriver.Firefox()

#options = Options()
#options.add_argument('--headless')
#options.add_argument('--no-sandbox') 
#options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome()
url = 'https://130.162.115.46/analytics/saw.dll?Dashboard&PortalPath=%2Fshared%2FSelf%20Service%2FEarly%20Month%2FDashboard-%20EMOB&page=Cumulative'
driver.get(url)


def espera(xpath_espera):
  try:
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath_espera)))
  except TimeoutException as e:
    print("ha habido un timeout")
    #fichero = str(time.time()) +".png"
    #driver.save_screenshot(fichero)
  except Exception as e:
    print("Otro error")
    print(e)
  else:
    # todo ha ido bien
    pass

def esperaVisibilidad(xpath_visi):
  try:
    WebDriverWait(driver, timeout).until(EC.invisibility_of_element_located((By.XPATH, xpath_visi)))
  except TimeoutException as e:
    print("ha habido un timeout")
    #fichero = str(time.time()) +".png"
    #driver.save_screenshot(fichero)
  except Exception as e:
    print("Otro error")
    print(e)
  else:
    # todo ha ido bien
    pass


timeout=100
espera('//button[@id="btn_login"]')

xpath = '//input[@id="idUser"]'
obj = driver.find_element_by_xpath(xpath)
obj.send_keys('Admin')

xpath = '//input[@id="idPassword"]'
obj = driver.find_element_by_xpath(xpath)
obj.send_keys('W3lcoMe1_#19')

xpath = '//button[@id="btn_login"]'
obj = driver.find_element_by_xpath(xpath)
obj.click()


print('Esperando rueda')
xpath = '//img[@id="uberBar_dashboardpageoptions_image"]'
espera(xpath)
obj = driver.find_element_by_xpath(xpath)
obj.click()

print('Esperando refresh')
xpath = '//img[@alt="Refrescar Imagen"]'
espera(xpath)
obj = driver.find_element_by_xpath(xpath)
obj.click()
try:
    WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

    alert = driver.switch_to.alert
    alert.accept()
    print("alert accepted")
except TimeoutException:
    print("no alert")

print('Esperando segunda flecha para abajo')
xpath = '//img[@id="d:dashboard~p:lsbj05flbk6b3oc1~s:dn3t0vd0jsbd577eMax"]'
espera(xpath)
obj = driver.find_element_by_xpath(xpath)
obj.click()

print('Esperando Menu Desplegable')
menu_desplegable=sys.argv[1]
print(menu_desplegable)
xpath = '//label[@title="' + menu_desplegable + '"]'
espera(xpath)
obj = driver.find_element_by_xpath(xpath)
id_label=obj.get_attribute('for')
id_dinamico=id_label.replace("_op", "_1_dropdownIcon")
#print(id_dinamico)
xpath = '//img[@id="' + id_dinamico + '"]'
espera(xpath)
obj = driver.find_element_by_xpath(xpath)
obj.click()

print('Esperando Menu Dinamico')
menu_click=sys.argv[2]
print(menu_click)

#xpath='//input[@title="' + menu_click + '"]/following::img[@class="promptComboBoxButtonMoz"]'
xpath='//input[@value="' + menu_click + '"]'
espera(xpath)
obj = driver.find_element_by_xpath(xpath)
obj.click()
#xpath='//label[text()="' + menu_click + '"]'
#obj = driver.find_element_by_xpath(xpath)
#id_check=obj.get_attribute('for')
#print(id_check)

#xpath='//input[@id="' + id_check + '"]'

#espera(xpath)
#obj = driver.find_element_by_xpath(xpath)
#obj.click()

#d:dashboard~p:mrt4ql8stfjk5oo7~r:itr7vhg44pof0rcr~v:compoundView!1~v:dvtchart!2ViewContainer

print('Click en apply')
xpath = '//input[@id="gobtn"]'
espera(xpath)
obj = driver.find_element_by_xpath(xpath)
obj.click()



