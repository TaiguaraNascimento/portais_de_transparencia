

import os
from unittest import result


endereco = 'C:\\Users\\Taiguara Nascimento\\OneDrive - GRANT THORNTON BRASIL\\OUTROS PROJETOS\\Projeto ECD\\ECD RANDON\\ECD RANDON\\'
endereco = 'C:\\Users\\TaiguaraPiresdoNasci\\OneDrive - GRANT THORNTON BRASIL\\OUTROS PROJETOS\\Projeto ECD\\ECD RANDON\\ECD RANDON\\'


arquivo1 = os.path.join(endereco, 'ECD Abr21.txt')
arquivo2 = os.path.join(endereco, 'ECD Jan21.txt')


#Arquivo de gravação
arquivo_de_saida = os.path.join(endereco, 'ECD_ABRIL_alterada_v1.txt')
with open(arquivo_de_saida, 'w') as out:

    # Arquivo de leitura
    with open(arquivo1) as f:
        lines = f.readlines()


    for line in lines:

        linha = line

        if line.startswith('|I250|004'): 

            alterada = line.split('|')

            if len(alterada[3]) > 0:
                pass
                '''
                if alterada[3] != '1000SPED':
                    print('Sim - ', line)
                else:
                    print('Não - ', line)
                '''
            else:
                
                alterada[3] = '1000SPED'
                alterada = '|'.join(alterada)
                linha = alterada

        else:
            linha = line

        out.write(linha)




# filtro1 = ecd_jan.query("Linhas.str.startswith('|I250|004') & ~Linhas.str.contains('1000SPED')")