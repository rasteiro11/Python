from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"    # localiza onde esta installado o driver no seu pc
driver = webdriver.Chrome(PATH)                     # cria um driver
driver.get("https://www.youtube.com/?hl=pt&gl=BR")  # connecta a um endereco url
# driver.close()                                        #fecha a janela
print(driver.title)                                 # pega o titulo da pagina
driver.quit()                                       # fecha o navegador
