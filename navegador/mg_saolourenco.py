from navegador.buscador import Buscador
from navegador.entidade import Entidade


class MGSaoLourenco:
    def __init__(self) -> None:


        self.entidade = Entidade(
            'São Lourenço',       
            'RJ', 
            'http://transparencia.saolourenco.mg.gov.br/FolhaPagamento', 
            'saolourenco',                                                                                  
            'A partir de 01/2017, porém está valor líquido.')

        self.buscador = Buscador(self.entidade)

    def processar_entidade(self) -> None:

        self.buscador.pausa_longa()

        ano_inicial = 2013
        ano_final = 2022

        for ano in range(ano_inicial, ano_final + 1):

            self.buscador.pausa_longa()
            
            self.buscador.selecionar_opcao_no_dropdown('NUM_EXERCICIO', str(ano))

            mes_inicial = 1
            mes_final = 12

            for mes in range(mes_inicial, mes_final + 1):

                self.buscador.pausa_longa()

                # Seleciona o mês
                self.buscador.selecionar_opcao_no_dropdown('MES_REFERENCIA', '{:02d}'.format(mes))
                
                self.buscador.pausa_longa()

                self.buscador.clicar_no_elemento_xpath('//*[@id="formDados"]/fieldset/div[2]/div[5]/input')

                self.buscador.pausa_longa()

                self.buscador.clicar_no_elemento_xpath('/html/body/div[6]/div/div[2]/div[1]/div/fieldset/fieldset/div/div/input[4]')


    def manter_janela_aberta(self):
        while(True):
            pass