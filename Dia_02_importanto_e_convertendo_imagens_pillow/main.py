# Instalando Bibliotecas
# pip install pillow

# Importando Bibliotecas
from PIL import Image
import os

# Define a pasta de Origem
origem = './pasta_origem/'

# Busca os arquivos que estão na pasta origem e salvar na Variavel "arquivos"
for raiz, diretorios, files in os.walk(origem):
    arquivos = files # Retorna os arquivos encontrados em forma de lista

# Define Pasta Destino
destino = './pasta_destino/'

# Um laço para salvar os arquivos em sua nova estensão
for arquivo in arquivos:
    image = Image.open(f'{origem}{arquivo}') # Retorna a imagem aberta
    image.save(f'{destino}{arquivo[:-4]}.estensao_desejada') # Salva a imagem em sua nova estensão