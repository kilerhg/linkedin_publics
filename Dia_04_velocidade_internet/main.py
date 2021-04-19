# Importando Biblioteca
import speedtest

# Recebe resultado Teste de velocidade
velocidade = speedtest.Speedtest()

# Atribui velocidade de Dowload
download = round(velocidade.download()/1000000,2)

# Atribui velocidade de Upload
upload = round(velocidade.upload()/1000000,2)
# Dividindo por 1 milhao para converter bit para mbps
# Utilizando Round para arredondar para 2 digitos

# Mostrando Resultado
print(f"Velocidade de Download em Mbps: {download}")
# Velocidade de Download em Mbps: 52.11
print(f"Velocidade de Upload   em Mbps: {upload}")
# Velocidade de Upload   em Mbps: 10.23
