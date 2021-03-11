from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"    # localiza onde esta installado o driver no seu pc
driver = webdriver.Chrome(PATH)                     # cria um driver

driver.get("https://techwithtim.net/")              # abre esse url

link = driver.find_element_by_link_text("Python Programming") # procura um link pelo seu nome
link.click()                                                  # clica no link

try:
    element = WebDriverWait(driver, 10).until(      # esperar 10seg ate encontarrmos o elemento de link Beginner Python Tutorials
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()                                 #clica nesse elemento

    element = WebDriverWait(driver, 10).until(      # esperar 10seg ate encontarrmos o elemento de id sow-button-19310003
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()                                 # clique nesse elemento

    driver.back()                                   # volta uma pagina
    driver.back()                                   # volta uma pagina
    driver.back()                                   # volta uma pagina
    driver.forward()                                # avanca uma pagina
    driver.forward()                                # avanca uma pagina

except:
    driver.quit()                                   # fechar o  navegador