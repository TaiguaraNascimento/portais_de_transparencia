from navegador.buscador import Buscador
from navegador.entidade import Entidade

class SCBalnearioGaivota:

    def __init__(self) -> None:

        self.entidade = Entidade(
            'Balneario Gaivota',       
            'SC', 
            'https://transparencia.betha.cloud/#/LLL0P0o_xuzlF0HbhRul5w==/agrupador/19505',  
            'sc_balneario_gaivota',                                                                                  
            'xxxxxx')

        self.buscador = Buscador(self.entidade)

    def processar_entidade(self) -> None:
        
        try:

            self.buscador.pausa_media()
            print('Esperando a tela carregar.......')

            botao_filtro = '/html/body/div[1]/main/div/div/div/div/div/div[1]/span/div/div/div/div/div/div[1]/button'
            self.buscador.clicar_no_elemento_xpath(botao_filtro)

            # Clicar no 04/22
            self.buscador.clicar_no_elemento_xpath('/html/body/div[6]/div/div[2]/div/div/div/div/div[1]/div[2]/ul/li[1]')

            # Botão filtrar
            self.buscador.clicar_no_elemento_xpath('/html/body/div[6]/div/div[3]/button[1]')

            elemento = '/html/body/div[1]/main/div/div/div/div/div/div[5]/div/div/table/tbody/tr'
            print(self.buscador.obter_lista_de_elementos_por_xpath(elemento))
            
 
        except:
            print('Não foi possível executar o script inteiro.')

  
    def manter_janela_aberta(self):
        while(True):
            pass