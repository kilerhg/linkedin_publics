# Importando Bibliotecas
import requests
import pandas as pd
import json

# Definindo Url da API
url = 'https://www.googleapis.com/books/v1/volumes?q=teste'

# Consumindo API
resposta = requests.get(url).json()

# Convertendo de Dicionario para Pandas
df = pd.DataFrame.from_dict(resposta['items'])