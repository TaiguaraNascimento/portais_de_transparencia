from navegador.buscador1 import Buscador
from navegador.entidade import Entidade

class RJResende:

    def __init__(self) -> None:

        self.entidade = Entidade(
            'Resende',       
            'RJ', 
            'https://e-gov.betha.com.br/transparencia/01037-136/con_servidoresativos.faces?mun=OKdsadUWH3o%3D',  
            'rj_itatiaia',                                                                                  
            'xxxxxx')

        self.buscador = Buscador(self.entidade)

    def processar_entidade(self) -> None:

        anos = [ 
            '2021',
            ]
        
        for ano in anos:

            for mes in range(8, 13):

                lista_de_pessoas = []

                if ano == '2022' and mes > 5:
                    print('# Não será feita nenhuma ação a partir de junho de 2022. ')
                else:

                    # Acessar primeiro o mês e ano
                    self.acessar_ano_e_mes(ano, mes)

                    # Realizar a cópia dos dados
                    self.copiar_lista_de_dados(ano, mes)

                    # Retornar à página inicial
                    self.retornar_a_tela_inicial()


    def acessar_ano_e_mes(self, ano, mes):
        
        print('# Acessando informações do período: ', ano, '/', mes)

        # Selecionar o ano
        self.buscador.pausa_media()
        self.buscador.selecionar_opcao_no_dropdown_por_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/span/div/span/div[1]/div[1]/label/span/select', ano)

        # Selecionar o mês
        self.buscador.pausa_curta()
        self.buscador.selecionar_opcao_no_dropdown_por_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/span/div/span/div[1]/div[2]/label/span/select', str(mes))

        # CLicar no item da pesquisa
        self.buscador.clicar_no_elemento_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/span/span/div/span[2]/input')
        self.buscador.pausa_media()





    def retornar_a_tela_inicial(self):
        # Retornar à inicial
        self.buscador.pausa_curtissima()
        self.buscador.pressionar_teclas('f5')
        self.buscador.pausa_media()


    def copiar_lista_de_dados(self, ano, mes):

        arquivo_exportar = 'C:\\Users\\TaiguaraPiresdoNasci\\OneDrive - GRANT THORNTON BRASIL\\# Backup\\Área de Trabalho\\Aqui\\resende_exportar_dados_' + str(ano) + '_' + str(mes) + '.txt'

        with open(arquivo_exportar, "w") as f:

            linha1 = self.buscador.obter_valor_de_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/div[2]/div/div[3]/table[1]/tbody/tr[1]/td')
            linha2 = self.buscador.obter_valor_de_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/div[2]/div/div[3]/table[1]/tbody/tr[2]/td')
            linha3 = self.buscador.obter_valor_de_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/div[2]/div/div[3]/table[1]/tbody/tr[3]/td')
            linha4 = self.buscador.obter_valor_de_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/div[2]/div/div[3]/table[1]/tbody/tr[4]/td')
            linha5 = self.buscador.obter_valor_de_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/div[2]/div/div[3]/table[1]/tbody/tr[5]/td')
            linha6 = self.buscador.obter_valor_de_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/div[2]/div/div[3]/table[1]/tbody/tr[6]/td')
            linha7 = self.buscador.obter_valor_de_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/div[2]/div/div[3]/table[1]/tbody/tr[7]/td')
            linha8 = self.buscador.obter_valor_de_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/div[2]/div/div[3]/table[1]/tbody/tr[8]/td')

            secao = [
                ano, 
                mes,
                linha1,
                linha2,
                linha3,
                linha4,
                linha5,
                linha6,
                linha7, 
                linha8                
            ]

            f.write(self.serializar(secao))
            print(secao)
        
        f.close()



    def quebrar_ano_mes(self):

        texto = self.buscador.obter_valor_de_xpath('/html/body/div[1]/div[1]/div/div/div/form/div[1]/div[1]/div[2]/div/div[1]')
        texto = texto.replace('Relação de servidores/empregados ativos em ', '')
        
        mes = texto[:-4]
        ano = texto[-4:]

        return [mes, ano]



    def manter_janela_aberta(self):
        print('############ TERMINOU ###############')
        while(True):
            pass



            
    def serializar(self, conteudo):

        saida = '|' +   str(conteudo[0]) + '|'
        saida = saida + str(conteudo[1]) + '|'
        saida = saida + str(conteudo[2]) + '|'
        saida = saida + str(conteudo[3]) + '|'
        saida = saida + str(conteudo[4]) + '|'
        saida = saida + str(conteudo[5]) + '|'
        saida = saida + str(conteudo[6]) + '|'
        saida = saida + str(conteudo[7]) + '|'
        saida = saida + str(conteudo[8]) + '|'
        saida = saida + str(conteudo[9]) + '|'
        saida = saida + '\n'

        return saida
