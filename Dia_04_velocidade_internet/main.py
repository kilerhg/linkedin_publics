# Importando Biblioteca
import speedtest

# Recebe resultado Teste de velocidade
velocidade = speedtest.Speedtest()

# Atribui velocidade de Download
download = round(velocidade.download()/1000000,2)

# Atribui velocidade de Upload
upload = round(velocidade.upload()/1000000,2)
# Dividindo por 1 milhão para converter bit para mbps
# Utilizando Round para arredondar para 2 dígitos

# Mostrando Resultado
print(f"Velocidade de Download em Mbps: {download}")
# Velocidade de Download em Mbps: 52.11
printf"Velocidade de Upload em Mbps: {upload}")
# Velocidade Upload em Mbps: 10.23
