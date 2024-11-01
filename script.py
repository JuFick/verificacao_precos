import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

# Configuração do logging
logging.basicConfig(filename='logs/precos_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Função para configurar o WebDriver com um User-Agent
def configurar_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36")
    driver = webdriver.Chrome(options=options)
    return driver

# Função para verificar preços
def verificar_precos(driver):
    precos = {}

    # Centauro
    try:
        driver.get("https://www.centauro.com.br/tenis-nike-air-max-excee-xbts-masculino-989893.html")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'p[data-testid="price-current"]'))
        )
        preco_centauro = driver.find_element(By.CSS_SELECTOR, 'p[data-testid="price-current"]').text
        match = re.search(r'R\$\s*\d+,\d{2}', preco_centauro)
        if match:
            preco_centauro = match.group(0)  # Captura apenas o valor 'R$ 549,47'
        precos['Centauro'] = preco_centauro
    except Exception as e:
        logging.error(f"Erro ao acessar Centauro: {str(e)}")

    # Nike
    try:
        driver.get("https://www.nike.com.br/tenis-nike-air-max-excee-xbts-masculino-029517.html")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="main-price"]'))
        )
        preco_nike = driver.find_element(By.CSS_SELECTOR, 'span[data-testid="main-price"]').text
        precos['Nike'] = preco_nike
    except Exception as e:
        logging.error(f"Erro ao acessar Nike: {str(e)}")

    # Mercado Livre
    try:
        driver.get("https://produto.mercadolivre.com.br/MLB-3799415319-tnis-nike-air-max-excee-xbts-masculino-_JM")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span.andes-money-amount__fraction'))
        )
        preco_mercadolivre = driver.find_element(By.CSS_SELECTOR, 'span.andes-money-amount__fraction').text
        preco_mercadolivre = f"R$ {preco_mercadolivre},00"  # Adiciona a formatação para o valor
        precos['Mercado Livre'] = preco_mercadolivre
    except Exception as e:
        logging.error(f"Erro ao acessar Mercado Livre: {str(e)}")
        
        
    return precos

# Loop de verificação
try:
    while True:
        driver = configurar_driver()  # Inicializa o WebDriver
        precos_encontrados = verificar_precos(driver)
        logging.info(f"Preços encontrados: {precos_encontrados}")
        print(precos_encontrados)
        driver.quit()  # Fecha o driver após cada execução
        time.sleep(60)  # Aguardar 1 minuto antes da próxima verificação

except KeyboardInterrupt:
    logging.info("Execução interrompida pelo usuário.")
