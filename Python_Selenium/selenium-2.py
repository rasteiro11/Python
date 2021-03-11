from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"    # localiza onde esta installado o driver no seu pc
driver = webdriver.Chrome(PATH)                     # cria um driver

driver.get("https://www.techwithtim.net")           # connecta a um endereco url
print(driver.title)

search = driver.find_element_by_name("s")           # acessa algum elemento HTML pelo seu ID
search.send_keys("test")                            # digita alguma coisa
search.send_keys(Keys.RETURN)                       # pressiona ENTER

try:                                                # tenta acessar    (para nao dar erro se a pagina nao tiver carregado)
    main = WebDriverWait(driver, 10).until(         # espera 10sec usando o driver ate
        EC.presence_of_element_located((By.ID, "main"))# encontrar elemento HTML de ID main
    )

    articles = main.find_elements_by_tag_name("article") # encontra os elementos HTML chamados de article
    for article in articles: # da um loop por todos os articles
        header = article.find_element_by_class_name("entry-summary") # encontra os headers pelo nome da classe
        print(header.text) # mostra os titulos

finally:
    driver.quit()

