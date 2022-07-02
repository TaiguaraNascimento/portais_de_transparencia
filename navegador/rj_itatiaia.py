from navegador.buscador import Buscador
from navegador.entidade import Entidade

class RJItatiaia:

    def __init__(self) -> None:

        self.entidade = Entidade(
            'Itatiaia',       
            'RJ', 
            'https://e-gov.betha.com.br/transparencia/01037-136/con_servidoresativos.faces?mun=1R7DbiTV1F3ZWkqAKT7j1Q==',  
            'rj_itatiaia',                                                                                  
            'xxxxxx')

        self.buscador = Buscador(self.entidade)

    def processar_entidade(self) -> None:

        
        
        anos = [ 
            '2016' 
            ]
        
        for ano in anos:

            for mes in range(11, 13):

            # for mes in [2, 3]:

                lista_de_pessoas = []

                if ano == '2022' and mes > 5:
                    print('# Não será feita nenhuma ação a partir de junho de 2022. ')
                else:

                    # Acessar primeiro o mês e ano
                    self.acessar_ano_e_mes(ano, mes)

                    # Realizar a cópia dos dados
                    self.colecionar_dados_das_paginas(lista_de_pessoas)

                    # Retornar à página inicial
                    self.retornar_a_tela_inicial()

                # self.demonstrar_o_conteudo_obtido(lista_de_pessoas)

                self.exportar_dados(lista_de_pessoas, mes, ano)


    def demonstrar_o_conteudo_obtido(self, lista_de_pessoas):

        print('--------------------------------------------------------------------------------')
        
        for linha in lista_de_pessoas:
            print(linha)

        print('--------------------------------------------------------------------------------')

       

    def colecionar_dados_das_paginas(self, lista_de_pessoas):

        parar = False

        pagina = 1

        while parar == False:

            self.buscador.pausa_curta()
            
            print('>>>>>>>>>>> Copiando dados da página ', pagina)

            # self.buscador.comandos_de_teclado('ctrl', 'end')

            self.copiar_lista_de_dados(lista_de_pessoas, pagina)

            pagina = pagina + 1

            if self.buscador.verificar_se_elemento_existe_por_link('Próxima'):
                self.buscador.clicar_em_link_text('Próxima')            
            else:
                parar = True


    def acessar_ano_e_mes(self, ano, mes):
        
        print('# Acessando informações do período: ', ano, '/', mes)

        try:

            # Selecionar o ano
            self.buscador.pausa_longa()
            self.buscador.selecionar_opcao_no_dropdown_por_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/span/div/span/div[1]/div[1]/label/span/select', ano)

            # Selecionar o mês
            self.buscador.pausa_media()
            self.buscador.selecionar_opcao_no_dropdown_por_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/span/div/span/div[1]/div[2]/label/span/select', str(mes))

            # CLicar no item da pesquisa
            self.buscador.clicar_no_elemento_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/span/span/div/span[2]/input')
            self.buscador.pausa_media()

        except:
            print('Erro ao atualizar mes ' , mes, ' e ano ', ano, '.')
            self.manter_janela_aberta()



    def retornar_a_tela_inicial(self):
        # Retornar à inicial
        self.buscador.pausa_curta()
        self.buscador.pressionar_teclas('f5')
        self.buscador.pausa_longa()



    def copiar_lista_de_dados(self, lista_de_retorno, pagina):

        try:
            mesano = self.quebrar_ano_mes()
        except:
            mesano = [0, 0]

        qtde = self.buscador.contar_ocorrencias_de_classe('row-expand')
        # print('# Existem ', qtde, ' linhas na página.')

        numero = 1
              
        try:

            for linha in range(0, qtde):
                nome = self.buscador.obter_valor_de_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/div[2]/div/div[3]/table[2]/tbody[' + str(numero) + ']/tr/td/ul/li[1]/label[1]')
                cargo = self.buscador.obter_valor_de_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/div[2]/div/div[3]/table[2]/tbody[' + str(numero) + ']/tr/td/ul/li[1]/label[2]')
                entidade = self.buscador.obter_valor_de_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/div[2]/div/div[3]/table[2]/tbody[' + str(numero) + ']/tr/td/ul/li[1]/label[3]')
                remuneracao_total = self.buscador.obter_valor_de_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/div[2]/div/div[3]/table[2]/tbody[' + str(numero) + ']/tr/td/ul/li[1]/label[5]')
                remuneracao_liquida = self.buscador.obter_valor_de_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/div[2]/div/div[3]/table[2]/tbody[' + str(numero) + ']/tr/td/ul/li[1]/label[7]')

                secao = [
                    str(mesano[0]),
                    str(mesano[1]),
                    str(pagina),
                    nome,
                    cargo,
                    entidade,
                    str(remuneracao_total),
                    str(remuneracao_liquida)
                ]

                lista_de_retorno.append(secao)

                numero = numero + 2

        except:
            print('>>>> Não foi possível obter os dados dessa posição da tabela.')





    def quebrar_ano_mes(self):

        texto = self.buscador.obter_valor_de_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/div[2]/div/div[1]')
        texto = texto.replace('Relação de servidores/empregados ativos em ', '')
        
        mes = texto[:-4]
        ano = texto[-4:]

        return [mes, ano]




    def exportar_dados(self, conteudo, mes, ano):

        try:
            arquivo_exportar = 'C:\\Users\\Taiguara Nascimento\OneDrive - Fundação Instituto de Administração\\__backup\\Desktop\\Cunha\\exportar_dados_' + str(mes) + '_' + str(ano) + '.txt'

            with open(arquivo_exportar, "w") as f:

                f.write(str('-'*100) + '\n')

                for linha in conteudo:

                    escrever = '|' + str(linha[0]) + '|' + str(linha[1]) + '|' + str(linha[2]) + '|' + str(linha[3]) + '|' + str(linha[4]) + '|' + str(linha[5]) + '|' + str(linha[6]) + '|' + str(linha[7]) + '|\n'
                    
                    # print(escrever)

                    f.write(escrever) 
                
                f.write('-'*100)

            f.close()
        
        except:
            print('######### NÃO FOI POSSÍVEL EXPORTAR O ARQUIVO')



    def manter_janela_aberta(self):
        print('############ TERMINOU ###############')
        while(True):
            pass