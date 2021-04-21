# Importando Bibliotecas
from selenium.webdriver import Firefox # Busca o controlador do Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from parsel import Selector
# Importando Bibliotecas

# nessa etapa inicial o webdriver é aberto no diretório abaixo
# (Lembrando ser necessario baixar o webdriver antes)
nome_driver = Firefox()

# Recebe Link Url
link_url = 'https://ultimateqa.com/fake-landing-page'

# nessa etapa é aberto o linkedin via webdriver
nome_driver.get(link_url)

# Define Tempo de espera
tempo_maximo_espera = 30

# Busca uma tag pelo Xpath
caminho_xpath = '//h4[@class="et_pb_module_header"]'
# exemplo_xpath = '//tag_html[@atributo="valor"]/tag/tag/tipo()'

# Aguarda para continuar enquanto tag HTML definida não carregar pelo 
# tempo máximo definido: tempo_máximo_espera
WebDriverWait(nome_driver, tempo_maximo_espera).until(
        EC.presence_of_element_located((By.XPATH, caminho_xpath))
        ) 

# Continuação da Automação

fonte_pagina = Selector(text=nome_driver.page_source)

nome_objeto = fonte_pagina.xpath('//h4[@class="et_pb_module_header"]/a/@href').getall()

print(nome_objeto)

