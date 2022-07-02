from navegador.buscador import Buscador
from navegador.entidade import Entidade

class MGJuizDeFora:

    def __init__(self) -> None:

        self.entidade = Entidade(
            'Juiz de  Fora',       
            'MG', 
            'https://e-gov.betha.com.br/transparencia/01037-136/con_servidoresativos.faces?mun=9eKRnLq5M4TIY6rasmASXTUQ5PRfrTTo',  
            'mg_juiz_de_fora',                                                                                  
            'xxxxxx')

        self.buscador = Buscador(self.entidade)

    def processar_entidade(self) -> None:

        lista_de_pessoas = []

        posicao1 = [1087,913]
        posicao2 = [1142,908]
        posicao3 = [1192,911]

        anos = ['2021']

        '''
        anos = [
            '2021',
            '2020', 
            '2019', 
            '2018', 
            '2017', 
            '2016', 
            '2015']
        '''

        
        for ano in anos:

            for mes in range(1, 13):

                # Selecionar o ano
                self.buscador.pausa_curta()
                self.buscador.selecionar_opcao_no_dropdown_por_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/span/div/span/div[1]/div[1]/label/span/select', ano)

                if ano == '2022' and mes > 6:
                    pass

                else:

                    self.buscador.pausa_curta()
                    self.buscador.selecionar_opcao_no_dropdown_por_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/span/div/span/div[1]/div[2]/label/span/select', str(mes))
                    
                    # CLicar no item da pesquisa
                    self.buscador.clicar_no_elemento_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/span/span/div/span[2]/input')

                    for passo in range(2, 33):

                        self.buscador.pausa_curta()

                        print(passo, '...', self.buscador.verificar_se_elemento_existe_por_link('Próxima'))
                        self.buscador.clicar_em_link_text('Próxima')
                        
                        '''
                        try:

                            self.buscador.pausa_curta()

                            # self.buscador.pressionar_teclas_em_serie('down', 30)
                            self.buscador.comandos_de_teclado('ctrl', 'end')

                            self.copiar_lista_de_dados(lista_de_pessoas, (passo - 1)) 
                            
                            if passo == 2:
                                posicao = posicao1
                            elif passo > 2 and passo <= 13:
                                posicao = posicao2
                            else:
                                posicao = posicao3

                            self.buscador.clicar_em_posicao_especifica_na_tela(posicao[0], posicao[1])
                            
                            print('----> página ', passo)

                            self.buscador.pausa_curtissima()

                        except:
                            print('Erro ao clicar no step.... ')'''


                    # Retornar à inicial
                    self.buscador.aguardar(5, 'Retornar')
                    self.buscador.pressionar_teclas('f5')

        self.exportar_dados(lista_de_pessoas)



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

    def exportar_dados(self, conteudo):

        arquivo_exportar = 'C:\\Users\\Taiguara Nascimento\OneDrive - Fundação Instituto de Administração\\__backup\\Desktop\\exportar_dados.txt'

        with open(arquivo_exportar, "w") as f:

            for linha in conteudo:

                escrever = '|' + linha[0] + '|' + linha[1] + '|' + linha[2] + '|' + linha[3] + '|' + linha[4] + '|' + linha[5] + '|' + linha[6] + '|' + linha[7] + '|\n'

                f.write(escrever) 

    def manter_janela_aberta(self):
        while(True):
            pass