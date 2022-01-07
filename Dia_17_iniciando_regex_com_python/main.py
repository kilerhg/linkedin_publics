# Importando Bibliotecas
import re

# Pattern Regex para validação de CEP
regex_valida_cep = r"^\d{5}-\d{3}$"

# EX: 00000-000
valor_input = str(input('Digite o cep:')).strip()

# Utiliza-se o re.match quando se quer encontrar apenas uma ocorrência
resultado_único = re.match(regex_valida_cep, valor_input)

# Utiliza-se o re.findall quando se quer encontrar diversas ocorrências
resultado_vários = re.findall(regex_valida_cep, valor_input)

print(resultado_único)
# <re.Match object; span=(0, 9), match='00000-000'>

print(resultado_único.group())
# 00000-000

print(resultado_vários)
# ['00000-000']