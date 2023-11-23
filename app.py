from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support.select import Select
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as condicao_esperada


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1200,700', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)
    chrome_options.add_experimental_option('prefs', {
        # Auterar o local padrão do download de arquivos
        'download.default_directory': 'C:\\Users\\lino\Desktop\\Passagens RYANAIR\\download',
        # Notificar o google chrome sobre essa auteração
        'download.directory_upgrade': True,
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos download
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    # Inicializando o webdriver
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchCookieException,
            ElementNotVisibleException,
            ElementNotSelectableException
        ]
    )

    return driver, wait


driver, wait = iniciar_driver()


def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1, 5)/30)


# navegar até o site
driver.get('https://www.ryanair.com/pt/pt/lp/descontos-e-promocoes/compra-um-recebe-outro-a-metade-do-preco')
sleep(2)

# botao_windows = driver.find_element(By.ID, 'WindowsRadioButton')

permitir_cookies = driver.find_element(
    By.XPATH, '//button[@class="cookie-popup-with-overlay__button"]')
sleep(3)
permitir_cookies.click()
sleep(2)

# popup_promocional = wait.until(condicao_esperada.visibility_of_element_located(
#   (By.XPATH, '//img[@alt="Registrieren"]')))
# sleep(2)
# popup_promocional.click()

driver.execute_script("window.scrollTo(0, 800);")

primeira_opcao_promocao = wait.until(condicao_esperada.visibility_of_element_located(
    (By.XPATH, '//div[@class="exp-panel__title ng-tns-c957786576-0 exp-panel__title--icon-right"]')))
sleep(3)
primeira_opcao_promocao.click()
sleep(5)
# botao_windows = driver.find_element(By.ID, 'WindowsRadioButton')
driver.execute_script("window.scrollTo(0, 800);")
sleep(3)

data_ida = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, '//button[@class="priced-date__date ng-star-inserted"]')))
sleep(2)
data_ida.click()
sleep(2)

driver.execute_script("window.scrollTo(0, 800);")
sleep(3)

botao_continuar_sem_devolucao = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, '//button[@data-ref="destination-summary__continue"]')))
sleep(2)
botao_continuar_sem_devolucao.click()
sleep(2)

botao_selecionar = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, '//button[@color="gradient-blue"]')))
sleep(2)
botao_selecionar.click()
sleep(2)

driver.execute_script("window.scrollTo(0, 800);")
sleep(3)

botao_continuar_basic = wait.until(condicao_esperada.element_to_be_clickable((
    By.XPATH, '//div[@class="fare-table__fare-column-border fare-table__fare-column-border--regular fare-table__fare-column-border--not-recommended"]')))
sleep(2)
botao_continuar_basic.click()
sleep(2)

botao_continuar_basic_02 = wait.until(condicao_esperada.element_to_be_clickable((
    By.XPATH, '//button[@data-e2e="value"]')))
sleep(2)
botao_continuar_basic_02.click()
sleep(2)

iniciar_sessao_mais_tarde = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, "//span[text()='Iniciar sessão mais tarde']")))
sleep(2)
iniciar_sessao_mais_tarde.click()
sleep(2)

dropdown_01 = driver.find_element(
    By.XPATH, '//button[@class="dropdown__toggle body-l-lg body-l-sm"]')

driver.execute_script("arguments[0].scrollIntoView();", dropdown_01)
sleep(3)
opcao_senhor = Select(dropdown_01)
sleep(3)
opcao_senhor.select_by_index(0)

select_primeiro_nome = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, '//input[@id="form.passengers.ADT-0.name"]')))
sleep(2)
select_primeiro_nome.send_keys('Lucas')
sleep(2)

select_segundo_nome = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, '//input[@id="form.passengers.ADT-0.name"]')))
sleep(2)
select_segundo_nome.send_keys('guedes')
sleep(2)

# driver.execute_script('arguments[0].click()', botao_radio)
# botao_radio.send_keys(Keys.DOWN)

input('Aperte uma tecla para fechar')
