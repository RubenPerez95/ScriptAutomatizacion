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
url = 'https://130.162.115.46/analytics/saw.dll?Dashboard&PortalPath=%2Fshared%2FSelf%20Service%2FKPI%2FDashboard%20-%20KPI&Page=Plan%20Summary&Action=RefreshAll&ViewState=jt7et9sd0pkrn5h1f2hhpg13bm&StateAction=samePageState'
driver.get(url)

listaxPaths = ['//div[@id="d:dashboard~p:62qm6i1ctovm0jbc~r:mq30hij2vj5jpeb8NavDone"]/div[@class="ProgressIndicatorDiv"]',
                '//div[@id="d:dashboard~p:62qm6i1ctovm0jbc~r:hfeanopj8tn8m288NavDone"]/div[@class="ProgressIndicatorDiv"]',
                '//div[@id="d:dashboard~p:62qm6i1ctovm0jbc~r:d163jqt0osej70l4NavDone"]/div[@class="ProgressIndicatorDiv"]',
                ]

listaHilos = []

listaNombres = ["New Accounts"]

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

def esperaOculto(xpath_visi):
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

def anadirXpath(xpathaux, nombre):
  xpath = xpathaux
  esperaVisibilidad(xpath)
  sale = time.time()
  print(nombre + str(sale - entra))

def anadirXpathOculto(xpathaux, nombre):
  xpath = xpathaux
  esperaOculto(xpath)
  sale = time.time()
  print(nombre + str(sale - entra))

def carga():

  for num in range(len(listaNombres)):
    print("Current")
    hilo = threading.Thread(target=anadirXpathOculto, args=(listaxPaths[num],listaNombres[num]))
    hilo.start()
    listaHilos.append(hilo)
    print("% of Plan Achieved")
    hilo1 = threading.Thread(target=anadirXpathOculto, args=(listaxPaths[num+1],listaNombres[num]))
    hilo1.start()
    listaHilos.append(hilo)
    print("Trend")
    hilo2 = threading.Thread(target=anadirXpathOculto, args=(listaxPaths[num+2],listaNombres[num]))
    hilo2.start()
    listaHilos.append(hilo)



timeout=300
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


entra = time.time()

#xpath = '//td[@class="PTChildPivotTable"]'
#anadirXpathOculto(xpath, "Default: ")

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

print('Esperando Menu Desplegable')
menu_desplegable=sys.argv[1]
print(menu_desplegable)
xpath = '//label[@title="' + menu_desplegable + '"]'
espera(xpath)
obj = driver.find_element_by_xpath(xpath)
id_label=obj.get_attribute('for')
id_dinamico=id_label.replace("_op", "_1_dropdownIcon")
xpath = '//img[@id="' + id_dinamico + '"]'
espera(xpath)
obj = driver.find_element_by_xpath(xpath)
obj.click()


print('Esperando Menu Dinamico')
menu_click=sys.argv[2]
if (menu_click is 'Todos los Valores de Columna'):
  menu_click = "*)nqgtac(*"
print(menu_click)
xpath='//input[@value="' + menu_click + '"]'
espera(xpath)
obj = driver.find_element_by_xpath(xpath)
obj.click()


if len(sys.argv)>=4:
  print('Esperando Menu Desplegable 2')
  menu_desplegable=sys.argv[3]
  print(menu_desplegable)
  xpath = '//label[@title="' + menu_desplegable + '"]'
  espera(xpath)
  obj = driver.find_element_by_xpath(xpath)
  id_label=obj.get_attribute('for')
  id_dinamico=id_label.replace("_op", "_1_dropdownIcon")  
  xpath = '//img[@id="' + id_dinamico + '"]'
  espera(xpath)
  obj = driver.find_element_by_xpath(xpath)
  obj.click()
  print('Esperando Menu Dinamico 2')
  menu_click=sys.argv[4]
  print(menu_click)
  xpath='//input[@value="' + menu_click + '"]'
  espera(xpath)
  obj = driver.find_element_by_xpath(xpath)
  obj.click()
  


#print('Esperando Menu Dinamico')
#menu_click=sys.argv[2]
#print(menu_click)

#xpath='//input[@value="' + menu_click + '"]'
#espera(xpath)
#obj = driver.find_element_by_xpath(xpath)
#obj.click()

xpathClick = driver.find_element_by_xpath(By.XPATH, "Embedd:dashboard~p:62qm6i1ctovm0jbc~s:1ifc3beakhor6t6s")
xpath.click()
#Actions builder = new Actions(driver)
#Action clickfuera = builder.

entra = time.time()

carga()


for numero in range(len(listaHilos)):
  listaHilos[numero].join