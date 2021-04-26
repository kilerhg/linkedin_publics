# Importando Flask
from flask import Flask

# definindo objeto da classe
app = Flask(__name__)

@app.route('/') # caminho da rota
def index(): # Define função para raiz
    # Mostra o conteúdo na tela
    return "Página Inicial" 

# Verifica se o app é o arquivo principal
if __name__ == "__main__":
    app.run() # Executa o app