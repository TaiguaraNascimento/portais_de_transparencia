from navegador.buscador import Buscador
from navegador.entidade import Entidade

class MGJuizDeForaCamara:

    def __init__(self) -> None:

        self.entidade = Entidade(
            'Juiz de Fora',       
            'MG', 
            'https://www.camarajf.mg.gov.br/transparencia/remuneracaoServidores.php',
            'mg_juiz_de_fora',
            'A partir de 01/2017, porém está por órgão, não demonstra o salário.')

        self.buscador = Buscador(self.entidade)

    def processar_entidade(self) -> None:
        
        self.buscador.pausa_curta()

        self.buscador.clicar_na_posicao_de_um_alimento_por_xpath('//*[@id="services"]/div/div[2]/div/div/a')
        
        a = self.buscador.obter_posicao_de_elemento_por_xpath('//*[@id="services"]/div/div[2]/div/div/a')
        print(a)
        print(type(a))


        # {'x': 922, 'y': 1713}



    def manter_janela_aberta(self):
        while(True):
            pass
