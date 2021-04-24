# instalando bibliotecas
# pip install newspaper3k

# Importando bibliotecas
from newspaper import Article


# Recebendo url artigo
url = 'https://edition.cnn.com/2021/04/24/us/derek-chauvin-eyes-indifference-blake/index.html'

# Definindo classe artigo para variável
artigo = Article(url, language='pt')

artigo.download() # Baixa o artigo
artigo.parse() # Raspa o site, buscando artigo
artigo.nlp() # Separa o sumário & Palavras Chaves

# Recebe o conteúdo do Titulo
titulo = artigo.title
# TEXTO DO TITULO

# Recebe o conteúdo do Sumário
sumario = artigo.summary
# TEXTO DO SUMÁRIO

# Continuação Amanhã falando sobre como extrair sentimento do sumário ;)'

# Definindo classe artigo para variável
artigo = Article(url, language='pt')

artigo.download() # Baixa o artigo
artigo.parse() # Raspa o site, buscando artigo
artigo.nlp() # Separa o sumário & Palavras Chaves

# Recebe o conteúdo do Titulo
titulo = artigo.title
# TEXTO DO TITULO

# Recebe o conteúdo do Sumário
sumario = artigo.summary
# TEXTO DO SUMÁRIO

# Continuação Amanhã falando sobre como extrair sentimento do sumário ;)'

# Definindo classe artigo para variável
artigo = Article(url, language='pt')

artigo.download() # Baixa o artigo
artigo.parse() # Raspa o site, buscando artigo
artigo.nlp() # Separa o sumário & Palavras Chaves

# Recebe o conteúdo do Titulo
titulo = artigo.title
# TEXTO DO TITULO

# Recebe o conteúdo do Sumário
sumario = artigo.summary
# TEXTO DO SUMÁRIO


print(sumario)

# Continuação Amanhã falando sobre como extrair sentimento do sumário ;)



# --------- DETALHES EXTRA SOBRE A BIBLIOTECA ---------

# titulo = artigo.title
# autores = artigo.authors
# data_publicacao = artigo.publish_date
# texto = artigo.text
# imagem = artigo.top_image
# videos = artigo.movies
# sumario = artigo.summary
#
# # Print sobre todas as variaveis
#
# print(f'''
#
# Titulo          : {titulo}
# Texto           : {texto.strip():.30}
# Sumario         : {sumario.strip()}
# Imagem          : {imagem}
# Videos          : {videos}
# Autores         : {autores}
# Data publicacao : {data_publicacao}

# ''')

# --------- DETALHES EXTRA SOBRE A BIBLIOTECA ---------
