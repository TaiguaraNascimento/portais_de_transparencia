from turtle import pos
from navegador.buscador import Buscador
from navegador.entidade import Entidade

class SPItaquaquecetuba:

    def __init__(self) -> None:

        self.entidade = Entidade('Itaquaquecetuba',    
                        'RJ', 
                        'https://transparencia.itaquaquecetuba.sp.gov.br/TDAPortalClient.aspx?417',                                                                     
                        'sp_itaquaquecetuba',
                        'A partir de 01/2017, apenas remuneração total.')

        self.buscador = Buscador(self.entidade)

    def processar_entidade(self) -> None:

        self.buscador.pausa_longa()

        self.buscador.clicar_em_posicao_especifica_na_tela(1291, 517)

        self.buscador.pausa_longa()

        ano_inicial = 1
        ano_final = 1 # Exclusive

        anos = [
            [2014, 298, 255],
            [2015, 298, 273],
            [2016, 298, 282],
            [2017, 298, 301],
            [2018, 298, 314],
            [2019, 298, 324],
            [2020, 298, 341],
            [2021, 298, 357],
            [2022, 298, 370]
        ]

        meses = [
            ['1', 550,255 ],
            ['2', 550,270 ],
            ['3', 550,285 ],
            ['4', 550,300 ],
            ['5', 550,315 ],
            ['6', 550,330],
            ['7', 550,345 ],
            ['8', 550,360],
            ['9', 550,374 ],
            ['10', 550, 388 ],
            ['11', 550, 402 ],
            ['12', 550, 416]
        ]

        for ano in range(ano_inicial, ano_final + 1):

            self.buscador.clicar_em_posicao_especifica_na_tela(284, 239) # Clica na caixa

            posicao_x = anos[ano][1]
            posicao_y = anos[ano][2]

            print('Ano - Clique ', posicao_x, ' e ', posicao_y)

            self.buscador.clicar_em_posicao_especifica_na_tela(posicao_x, posicao_y) # Escolhe o ano

            self.buscador.pausa_curta()

            mes_inicial = 0
            mes_final = 11 # Exclusive

            for mes in range(mes_inicial, mes_final + 1):

                self.buscador.pausa_curta()

                posicao_xa = meses[mes][1]
                posicao_ya = meses[mes][2]

                self.buscador.clicar_em_posicao_especifica_na_tela(540, 240) # Clica na caixa
                self.buscador.clicar_em_posicao_especifica_na_tela(posicao_xa, posicao_ya) # Escolhe o mes

                self.buscador.pausa_curta()

                print(' --> Meses - Clique ', posicao_xa, ' e ', posicao_ya, str(mes+1))

                self.buscador.clicar_em_posicao_especifica_na_tela(1797, 234) # Clica no filtrar

                self.buscador.aguardar(12, 'Clica no botão')

                self.buscador.pressionar_teclas('esc')

                self.buscador.pausa_media()

        '''

                try:

                    # Abaixar um pouco a tela
                    self.buscador.pressionar_teclas_em_serie("down", 28)



                        seletor = ano - ano_de_apoio

                        print('Apoio:', seletor, ',', ano, ',', ano_de_apoio)

                        # Abre o seletorc

                        # Seleciona o ano do projeto


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

                                orgao = [
                                    'Todas as situações'
                                ]

                                for etapa in range(0, 6):

                                    self.buscador.pausa_curta()

                                    # Aciona um botão de dropdown da situacao

                                    self.buscador.pausa_curta()

                                    print('Obtendo dados de ', ano, ' do mes ', mes, '...', str(etapa + 1), '-', orgao[etapa], 'Valores ->', self.buscador.obter_valor_de_xpath('//*[@id="balanco"]/div[3]/div/div/div/div[3]/div[6]/div[1]/div[2]/div/div[1]/div/div[1]'), "Servidores ->", self.buscador.obter_valor_de_xpath('//*[@id="balanco"]/div[3]/div/div/div/div[3]/div[6]/div[1]/div[2]/div/div[2]/div/div[1]'))

                                    if self.buscador.verificar_se_xpath_existe('//*[@id="balanco"]/div[3]/div/div/div/div[3]/div[6]/div[1]/div[3]/div/div[1]/a[2]'):
                                            

                                        self.buscador.pausa_longa()
                                        self.buscador.pausa_longa()
                                        
                                        # self.buscador.organizar_arquivos_baixados(orgao[etapa], 'Ano ' + str(ano), 'todos', str(orgao[etapa] + '_' + str(ano) + '_' + str(mes)))

                                    else:

                                        print('---------> Não há dados para download em ', ano, ' do mes ', mes, '...', str(etapa + 1), '-', orgao[etapa])



                            except:
                                print('Não foi possível obter dados desse mês.')
                
                except:
                    print('Não foi possível executar o script inteiro.')
        '''
  
    def manter_janela_aberta(self):
        while(True):
            pass