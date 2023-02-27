# Versão do Chrome 110.0.5481.178
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


class autoGitHub:
    def __init__(self):
        # Endereço do site a ser automatizado.
        self.SITE_LINK = "https://github.com/"
        # Dicionário com as coordenadas dos objetos a ser criado.
        # Seperar por botões, checkbox, input.
        self.SITE_MAP = {
            "buttons": {
                "login": {
                    "xpath": "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[2]/a"
                },
                "login_field": {
                    "xpath": "/html/body/div[1]/div[3]/main/div/div[4]/form/input[2]"
                },
                "password_fiels": {
                    "xpath": "/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[1]"
                },
                "submit_login": {
                    "xpath": "/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[11]"
                },
                "new_repository": {
                    "xpath": "/html/body/div[1]/div[6]/div/aside/div/loading-context/div/div[1]/div/h2/a"
                },
                "repository_name": {
                    "xpath": "/html/body/div[1]/div[6]/main/div/form/div[2]/auto-check/dl/dd/input"
                },
                "repository_description": {
                    "xpath": "/html/body/div[1]/div[6]/main/div/form/div[5]/dl/dd/input"
                },
                "checkbox_public": {
                    "xpath": "/html/body/div[1]/div[6]/main/div/form/div[5]/div[1]/label/input"
                },
                "checkbox_readme": {
                    "xpath": "/html/body/div[1]/div[6]/main/div/form/div[5]/div[3]/div[1]/label/input[2]"
                },
                "git_ignore": {
                    "xpath": "/html/body/div[1]/div[6]/main/div/form/div[5]/div[3]/div[2]/span/details/summary"
                },
                "git_ignore_filter": {
                    "xpath": "/html/body/div[1]/div[6]/main/div/form/div[5]/div[3]/div[2]/span/details/details-menu/div/filter-input/input"
                },
                "choose_license": {
                    "xpath": "/html/body/div[1]/div[6]/main/div/form/div[5]/div[3]/div[3]/span/details/summary"
                },
                "choose_license_filter": {
                    "xpath": "/html/body/div[1]/div[6]/main/div/form/div[5]/div[3]/div[3]/span/details/details-menu/div/filter-input/input"
                },
                "creating_repository": {
                    "xpath": "/html/body/div[1]/div[6]/main/div/form/div[5]/button"
                },
                "code": {
                    "xpath": "/html/body/div[1]/div[6]/div/main/turbo-frame/div/div/div/div[3]/div[1]/div[2]/span[1]/get-repo/feature-callout/details/summary"
                },
                "url_code": {
                    "xpath": "/html/body/div[1]/div[6]/div/main/turbo-frame/div/div/div/div[3]/div[1]/div[2]/span[1]/get-repo/feature-callout/details/div/div/div[1]/tab-container/div[2]/ul/li[1]/tab-container/div[2]/div/input"
                }
            }
        }

        # Iniciar o Driver do selenium, no path colocar duas barras ou r depois do igual.
        self.driver = webdriver.Chrome(executable_path = "C:\\Users\\David\\Documents\\Python\\Automacao\\chrome_driver\\chromedriver.exe")
        
        # Abrir o navegador em tela cheia.
        self.driver.maximize_window()


    # Metódos
    def open_website(self):
        time.sleep(2)
        # Pedir ao driver abrir o link do site.
        self.driver.get(self.SITE_LINK)
        time.sleep(2)


    # Fazer login.
    def to_do_login(self):
        # Encontrar um elemento na tela e clicar.
        self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["login"]["xpath"]).click()
        time.sleep(1)
        # Encontrar um elemento input na tela e colocar um texto.
        # Como criptografar usuário e senha?
        self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["login_field"]["xpath"]).send_keys("david.simas81@gmail.com")
        # Encontrar um elemento input na tela e colocar um texto.
        # Principalmente a senha.
        self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["password_fiels"]["xpath"]).send_keys("d4a1i9d4pro")
        # Encontrar um elemento na tela e clicar.
        self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["submit_login"]["xpath"]).click()
        time.sleep(1)


    # Criar novo Repositório.
    def new_repository(self):
        # Encontrar um elemento na tela e clicar.
        self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["new_repository"]["xpath"]).click()
        time.sleep(1)
        auto.fill_fields_repository()
        self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["creating_repository"]["xpath"]).click()
        time.sleep(10)


    # Preenchendo os campos.
    def fill_fields_repository(self):
        self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["repository_name"]["xpath"]).send_keys("Atividade_Automacao")
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["repository_description"]["xpath"]).send_keys("Atividade de automação para crir um novo repositório usando Python e Selenium.")
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["checkbox_public"]["xpath"]).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["checkbox_readme"]["xpath"]).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["git_ignore"]["xpath"]).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["git_ignore_filter"]["xpath"]).send_keys("Python")
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["git_ignore_filter"]["xpath"]).send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["choose_license"]["xpath"]).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["choose_license_filter"]["xpath"]).send_keys("MIT License")
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["choose_license_filter"]["xpath"]).send_keys(Keys.ENTER)
        time.sleep(1)
    

    # Copia o link para clonar o repositório
    def clone_repository(self):
        self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["code"]["xpath"]).click()
        repository_name = self.driver.find_element(By.XPATH, self.SITE_MAP["buttons"]["url_code"]["xpath"]).get_attribute("value")

        return repository_name



# Exetucar

auto = autoGitHub()
auto.open_website()
auto.to_do_login()
auto.new_repository()
auto.clone_repository()