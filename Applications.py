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
url = 'https://130.162.115.46/analytics/saw.dll?Dashboard&PortalPath=%2Fshared%2FSelf%20Service%2FApplication%20Approval%2FDashboard%20-%20Application&page=Applications%20Summary'
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

print('Esperando segunda flecha para abajo')
xpath = '//img[@id="d:dashboard~p:mrt4ql8stfjk5oo7~s:5iebu9spu8j3u3l4Max"]'
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
print(id_dinamico)
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

entra = time.time()
listaXpaths = [
              '//div[@id="d:dashboard~p:mrt4ql8stfjk5oo7~r:itr7vhg44pof0rcrNavDone"]/div[@class="ProgressIndicatorDiv"]',
              '//div[@id="d:dashboard~p:mrt4ql8stfjk5oo7~r:vt2qdj9bj3qci7duNavDone"]/div[@class="ProgressIndicatorDiv"]',
              '//div[@id="d:dashboard~p:mrt4ql8stfjk5oo7~r:tknatvi9p11ovgodNavDone"]/div[@class="ProgressIndicatorDiv"]',
              '//div[@id="d:dashboard~p:mrt4ql8stfjk5oo7~r:uh1pv26oagsgkk0dNavDone"]/div[@class="ProgressIndicatorDiv"]',
              '//div[@id="d:dashboard~p:mrt4ql8stfjk5oo7~r:qste6r8mq3emkjonNavDone"]/div[@class="ProgressIndicatorDiv"]',
              '//div[@id="d:dashboard~p:mrt4ql8stfjk5oo7~r:pt5m6736gtt6gvioNavDone"]/div[@class="ProgressIndicatorDiv"]',
              '//div[@id="d:dashboard~p:mrt4ql8stfjk5oo7~r:9u61n3ao5itmf101NavDone"]/div[@class="ProgressIndicatorDiv"]',
              '//div[@id="d:dashboard~p:mrt4ql8stfjk5oo7~r:61klcle93upv01qbNavDone"]/div[@class="ProgressIndicatorDiv"]',
              '//div[@id="d:dashboard~p:mrt4ql8stfjk5oo7~r:2sdgks9rautn9giqNavDone"]/div[@class="ProgressIndicatorDiv"]',
              '//div[@id="d:dashboard~p:mrt4ql8stfjk5oo7~r:kprfbc86f4s2il1bNavDone"]/div[@class="ProgressIndicatorDiv"]',
              ]

listaNombres = ['Aggregate Volume by Channel: ',
                'Cancelled Rate by Channel: ',
                'Approved Rate by Channel: ',
                'Declined Rate by Channel: ',
                'Automatic Approval Rate by Channel: ',
                'Avg. Age: ',
                'Avg. Time at Job: ',
                'Avg. Initial Credit Line: ',
                'Declined by Reason: ',
                'Cancellation by Reason: ']

listaHilos = []

def anadirXpath(xpathaux, nombre):
  xpath = xpathaux
  esperaVisibilidad(xpath)
  sale = time.time()
  print(nombre + str(sale - entra))

for numero in range(len(listaXpaths)):
  hilo = threading.Thread(target=anadirXpath, args=(listaXpaths[numero],listaNombres[numero]))
  hilo.start()
  listaHilos.append(hilo)

for numero in range(len(listaHilos)):
  listaHilos[numero].join



