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

            ano_inicial = 2022
            ano_final = 2022 # Exclusive

            ano_de_apoio = 2011
            

            for ano in range(ano_inicial, ano_final + 1):

                self.buscador.pausa_curta()

                seletor = ano - ano_de_apoio

                print('Apoio:', seletor, ',', ano, ',', ano_de_apoio)

                # Abre o seletor
                self.buscador.clicar_no_elemento_xpath('//*[@id="balanco"]/div[3]/div/div/div/div[3]/div[2]/div/div[2]/div/div[2]')

                # Seleciona o ano do projeto
                self.buscador.clicar_no_elemento_xpath('//*[@id="balanco"]/div[3]/div/div/div/div[3]/div[2]/div/div[2]/div/div[2]/ul/li[' + str(seletor) + ']/a')

                mes_inicial = 1
                mes_final = 12 # Exclusive

                for mes in range(mes_inicial, mes_final + 1):

                    self.buscador.pausa_curta()

                    # Abre o seletor de meses
                    self.buscador.clicar_no_elemento_xpath('//*[@id="balanco"]/div[3]/div/div/div/div[3]/div[2]/div/div[2]/div/div[1]')

                    # Aciona um botão de dropdown de período
                    self.buscador.clicar_no_elemento_xpath('//*[@id="balanco"]/div[3]/div/div/div/div[3]/div[2]/div/div[2]/div/div[1]/ul/li[' + str(mes) + ']')

                    try:
                        print('Obtendo dados de ', ano, ' do mes ', mes, '...')


                        for etapa in range(0, 5):

                            self.buscador.pausa_curta()

                            # Aciona um botão de dropdown da situacao
                            self.buscador.selecionar_opcao_no_dropdown_por_xpath('//*[@id="balanco"]/div[3]/div/div/div/div[3]/div[4]/div/div[2]/div/select', str(etapa))

                            self.buscador.pausa_curta()
                            
                            self.buscador.clicar_em_posicao_especifica_na_tela(558, 772)

                    except:
                        print('Não foi possível obter dados desse mês.')
        
        except:
            print('Não foi possível executar o script inteiro.')

  
    def manter_janela_aberta(self):
        while(True):
            pass