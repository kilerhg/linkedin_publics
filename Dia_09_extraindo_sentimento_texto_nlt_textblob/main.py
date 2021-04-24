###### Contéudo Post Ontem ###### 

# Importando bibliotecas
from newspaper import Article


# Recebendo url artigo
url = 'https://edition.cnn.com/2021/04/24/politics/inequality-biden-100-days/index.html'

# Definindo classe artigo para variável
artigo = Article(url)

artigo.download() # Baixa o artigo
artigo.parse() # Raspa o site, buscando artigo
artigo.nlp() # Separa o sumário & Palavras Chaves

# Recebe o conteúdo do Titulo
titulo = artigo.title
# TEXTO DO TITULO

# Recebe o conteúdo do Sumário
conteudo_texto = artigo.summary
# TEXTO DO SUMÁRIO

###### Contéudo Post Ontem ###### 

###### Contéudo Post Hoje ######  


# instalando bibliotecas
# pip install -U textblob
# python -m textblob.download_corpora

# Importando bibliotecas
from textblob import TextBlob

# Atribuindo Objeto da classe TextBlob
# OBS: Texto somente em Inglês
texto = TextBlob(conteudo_texto)

# Retirando Sentimento de -1 a 1
#  ------------ Tabela Sentimento ------------
# Muito Negativo    --Neutro--      Muito Positivo
#     -1          <<    0    >>           1
sentimento_texto = texto.sentiment.polarity

# Mostrando sentimento humanizado
if sentimento_texto < 0:
    print("Negativo")
elif sentimento_texto == 0:
    print("Neutro")
else:
    print('Positivo')

# Print Valor decimal sentimento
print(sentimento_texto)
# 0.17408521303258148

###### Contéudo Post Hoje ######  