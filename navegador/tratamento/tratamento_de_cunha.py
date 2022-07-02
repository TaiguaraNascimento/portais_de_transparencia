import os
import re

from pkg_resources import resource_isdir

arquivo = "C:\\Users\\Taiguara Nascimento\\OneDrive - GRANT THORNTON BRASIL\\OUTROS PROJETOS\\Projeto Santander\\Bases de Dados\\__Daniel\\Cunha\\HTML\\Compilado\\compilado_original_2.txt"


print(os.path.exists(arquivo))

placeholder = "@"

ajustes = [
    '<BODY>',
    '</BODY>',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
]

# Leitura do arquivo
with open(arquivo, 'r') as file:
    dados = file.read()

# Tamanho do arquivo bruto
print('Tamanho do arquivo bruto: ', len(dados))


# Coloca todos os caracteres em maiúsculas
dados.upper()

for ajuste in ajustes:
    dados.replace(ajuste, placeholder)


resultado = re.findall('^<?body$>', dados)

print(resultado)
print(len(resultado))



# Tamanho do arquivo tratado
print('Tamanho do arquivo tratado: ', len(dados))
