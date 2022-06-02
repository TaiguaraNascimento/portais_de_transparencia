from navegador.buscador import Buscador
from navegador.entidade import Entidade


class RJIpojuca:
    def __init__(self) -> None:

        self.entidade = Entidade(
            'Ipojuca',         
            'RJ', 
            'http://s2.asp.srv.br/etransparencia.pm.ipojuca.pe/servlet/wppessoalconsulta', 
            'rj_ipojuca',
            'A partir de 01/2017, porém está por órgão.')

        self.buscador = Buscador(self.entidade)

    def processar_entidade(self) -> None:

        ano_inicial = 2016
        ano_final = 2019 # Exclusive

        numero_de_apoio = 2024

        for ano in range(ano_inicial, ano_final + 1):

            print(ano,  '---------------', str(numero_de_apoio - ano))
            
            self.buscador.pausa_curta()

            # Limpar o conteúdo que está lá
            self.buscador.limpar_campo_de_input_por_id('vEXERCICIO')

            # Seleciona a caixa de listagem
            self.buscador.clicar_no_elemento_xpath('//*[@id="TBCONSULTAEXERCICIO"]/tbody/tr/td[2]/span/span')
            
            self.buscador.pausa_curtissima()

            # Seleciona o item da lista
            self.buscador.clicar_no_elemento_xpath('/html/body/div[5]/div[' + str(numero_de_apoio - ano) + ']/div/div[2]')

            # Clica no botão para acessar a página
            self.buscador.clicar_no_elemento_xpath('')
            
            self.buscador.pausa_longa()


                        
            '''
                        mes_inicial = 1
                        mes_final = 12

                        for mes in range(mes_inicial, mes_final):

                            # Seleciona o mês
                            self.buscador.selecionar_opcao_no_dropdown('vMES', str(mes))

                            self.buscador.pausa_curta()

                            self.buscador.clicar_no_elemento_xpath('//*[@id="EXPORTCSV"]')
                            
            '''



    def manter_janela_aberta(self):
        while(True):
            pass