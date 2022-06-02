from navegador.buscador import Buscador
from navegador.entidade import Entidade

class MGJuizDeForaPrefeitura:

    def __init__(self) -> None:

        self.entidade = Entidade(
            'Juiz de Fora',       
            'MG', 
            'https://www.pjf.mg.gov.br/transparencia/servidores/pesquisar.php?orgao_pesq=PJF',
            'mg_juiz_de_fora',
            'A partir de 01/2017, porém está por órgão, não demonstra o salário.')

        self.buscador = Buscador(self.entidade)


    def processar_entidade(self) -> None:

        numero_inicial = 169
        numero_final = 190

        for arquivo in range(numero_inicial, numero_final):

            # Clica no item e acessa a página
            self.buscador.clicar_no_elemento_xpath('//*[@id="dataset-resources"]/ul/li[' + str(arquivo) + ']/a')
            
            try:
                # Clica no botão baixar
                self.buscador.clicar_no_elemento_xpath('//*[@id="content"]/div[3]/section/div/div[1]/ul/li[1]/div/a')
            except:
                print('Erro ao captar esse arquivo.')

            self.buscador.pausa_curta()

            # Retorna à página
            self.buscador.retornar()