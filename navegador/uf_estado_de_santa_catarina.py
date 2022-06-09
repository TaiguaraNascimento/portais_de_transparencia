from navegador.buscador import Buscador
from navegador.entidade import Entidade

class SCSantaCatarina:

    def __init__(self) -> None:

        self.entidade = Entidade(
            'Estado de SC',       
            'SC', 
            'http://www.transparencia.sc.gov.br/remuneracao-servidores',  
            'uf_estado_de_santa_catarina',                                                                                  
            'A partir de 01/2017 por órgão, apenas salário bruto.')


        self.buscador = Buscador(self.entidade)

    def processar_entidade(self) -> None:
        

        try:
            self.buscador.pausa_curta()

            # Abaixar um pouco a tela
            self.buscador.pressionar_teclas_em_serie("down", 28)

            ano_inicial = 2021
            ano_final = 2022 # Exclusive

            ano_de_apoio = 2011

            for ano in range(ano_inicial, ano_final + 1):

                self.buscador.pausa_longa()

                seletor = ano - ano_de_apoio

                print('Apoio:', seletor, ',', ano, ',', ano_de_apoio)

                # Abre o seletorc
                self.buscador.clicar_no_elemento_xpath('//*[@id="balanco"]/div[3]/div/div/div/div[3]/div[2]/div/div[2]/div/div[2]')

                # Seleciona o ano do projeto
                self.buscador.clicar_no_elemento_xpath('//*[@id="balanco"]/div[3]/div/div/div/div[3]/div[2]/div/div[2]/div/div[2]/ul/li[' + str(seletor) + ']/a')

                mes_inicial = 1
                mes_final = 12 # Exclusive

                self.buscador.pausa_curta()

                for mes in range(mes_inicial, mes_final + 1):

                    self.buscador.pausa_curta()

                    # Abre o seletor de meses
                    self.buscador.clicar_no_elemento_xpath('//*[@id="balanco"]/div[3]/div/div/div/div[3]/div[2]/div/div[2]/div/div[1]')

                    # Aciona um botão de dropdown de período
                    self.buscador.clicar_no_elemento_xpath('//*[@id="balanco"]/div[3]/div/div/div/div[3]/div[2]/div/div[2]/div/div[1]/ul/li[' + str(mes) + ']')

                    try:

                        orgao = [
                            'Ativos',
                            'Inativo_Iprev',
                            'Pensionista_Especial',
                            'Pensionista_IPREV',
                            'PDI_PVI']

                        '''orgao = [
                            'Todas as situações'
                        ]'''

                        for etapa in range(0, 6):

                            self.buscador.pausa_curta()

                            # Aciona um botão de dropdown da situacao
                            self.buscador.selecionar_opcao_no_dropdown_por_xpath('//*[@id="balanco"]/div[3]/div/div/div/div[3]/div[4]/div/div[2]/div/select', str(etapa + 1))

                            self.buscador.pausa_curta()

                            print('Obtendo dados de ', ano, ' do mes ', mes, '...', str(etapa + 1), '-', orgao[etapa], 'Valores ->', self.buscador.obter_valor_de_xpath('//*[@id="balanco"]/div[3]/div/div/div/div[3]/div[6]/div[1]/div[2]/div/div[1]/div/div[1]'), "Servidores ->", self.buscador.obter_valor_de_xpath('//*[@id="balanco"]/div[3]/div/div/div/div[3]/div[6]/div[1]/div[2]/div/div[2]/div/div[1]'))

                            if self.buscador.verificar_se_xpath_existe('//*[@id="balanco"]/div[3]/div/div/div/div[3]/div[6]/div[1]/div[3]/div/div[1]/a[2]'):
                                    
                                self.buscador.clicar_em_posicao_especifica_na_tela(558, 772)

                                self.buscador.pausa_longa()
                                self.buscador.pausa_longa()
                                
                                # self.buscador.organizar_arquivos_baixados(orgao[etapa], 'Ano ' + str(ano), 'todos', str(orgao[etapa] + '_' + str(ano) + '_' + str(mes)))

                            else:

                                print('---------> Não há dados para download em ', ano, ' do mes ', mes, '...', str(etapa + 1), '-', orgao[etapa])



                    except:
                        print('Não foi possível obter dados desse mês.')
        
        except:
            print('Não foi possível executar o script inteiro.')

  
    def manter_janela_aberta(self):
        while(True):
            pass