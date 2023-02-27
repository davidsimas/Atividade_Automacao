# Versão do Chrome 110.0.5481.178
from selenium import webdriver
from selenium.webdriver.common.by import By

import time


class CookieCliker:
    def __init__(self):
        # Endereço do site a ser automatizado.
        self.SITE_LINK = "https://orteil.dashnet.org/cookieclicker/"
        # Dicionário com as coordenadas dos objetos a ser criado.
        self.SITE_MAP = {
            "buttons": {
                "biscoito": {
                    "xpath": "/html/body/div[2]/div[2]/div[15]/div[8]/button"
                },
                "upgrade": {
                    "xpath": "/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[$$NUMBERS$$]"
                },
                "idioma": {
                    "xpath": "/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[10]",
                    "id": "//*[@id='langSelect-PT-BR']"
                }
            }
        }

        # Iniciar o Driver do selenium, no path colocar duas barras ou r depois do igual.
        self.driver = webdriver.Chrome(executable_path = "C:\\Users\\David\\Documents\\Python\\Automacao\\chrome_driver\\chromedriver.exe")
        
        # Abrir o navegador em tela cheia.
        self.driver.maximize_window()
    

    # Metódos
    def abrir_site(self):
        time.sleep(2)
        # Pedir ao driver abrir o link do site.
        self.driver.get(self.SITE_LINK)
        time.sleep(5)
    

    # Escolhe o idioma.
    def escolhe_idioma(self):
        # Encontrar um elemento na tela.
        self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["idioma"]["xpath"]).click()
        time.sleep(5)


    def clicar_no_cookie(self):
        # Encontrar um elemento na tela.
        self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["biscoito"]["xpath"]).click()


    def pega_melhor_upgrade(self):
        encontrei = False
        elemento_atual = 2

        while not encontrei:
            objeto = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace("$$NUMBERS$$", str(elemento_atual))
            # Pega o contéudo do atributo class. 
            classes_objeto = self.driver.find_element(By.XPATH, objeto).get_attribute("class")

            if not "enabled" in classes_objeto:
                encontrei = True
            else:
                elemento_atual += 1

        return elemento_atual - 1


    def comprar_upgrade(self):
        objeto = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace("$$NUMBERS$$", str(self.pega_melhor_upgrade()))
        self.driver.find_element(By.XPATH, objeto).click()


# Exetucar

biscoito = CookieCliker()
biscoito.abrir_site()
biscoito.escolhe_idioma()


i = 0

while True:
    # Verifica se a variável i é resto da divisão por 500 é igual a 0, 
    # e não é a primeira execução do nosso loop.
    if i % 500 == 0 and i != 0:
        time.sleep(1)
        biscoito.comprar_upgrade()
        time.sleep(1)
    biscoito.clicar_no_cookie()
    # Incrementa a variável i.
    i += 1