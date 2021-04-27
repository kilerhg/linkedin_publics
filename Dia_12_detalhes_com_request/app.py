# Importando Flask
from flask import Flask, request

# definindo objeto da classe
app = Flask(__name__)

@app.route('/') # caminho da rota
def index(): # Define função para raiz
    # Mostra o conteúdo na tela
    return "<a href='/exemplo'>Página Inicial</a>" # Retorna tag html

# -------------- Conteúdo Post --------------

@app.route('/exemplo')
def exemplo():
    dicionario = dict(
        path=request.path, # Retorna A rota
        referrer = request.referrer, # Retorna o link referência para chegar aqui
        content_type=request.content_type, # Retorna o tipo do conteúdo
        method=request.method, # Retorna o método, GET, POST, UPDATE & etc
        args=request.args, # Retorna os argumentos (Query Strings)
        langs=request.accept_languages, # Retorna Idiomas
    )
    return dicionario # Retorna Dicionário

# -------------- Conteúdo Post --------------

# Verifica se o app é o arquivo principal
if __name__ == "__main__":
    app.run(debug=True) # Executa o app em modo debug