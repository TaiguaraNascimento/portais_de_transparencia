from navegador.buscador import Buscador
from navegador.entidade import Entidade

class MGJuizDeFora:

    def __init__(self) -> None:

        self.entidade = Entidade(
            'Juiz de  Fora',       
            'MG', 
            'https://www.pjf.mg.gov.br/transparencia/servidores/pesquisar.php?orgao_pesq=PJF',  
            'mg_juiz_de_fora',                                                                                  
            'xxxxxx')

        self.buscador = Buscador(self.entidade)

    def processar_entidade(self) -> None:
        
        try:

            print('Esperando a tela carregar.......')
            self.buscador.pausa_curta()

            orgaos = [
                'CGM','PGM',
                'SCS','SDS',
                'SE','SEAPA',
                'SEDH','SEDIC',
                'SE/FUNDEB', 'STDA',
                'SEL','SEMAUR',
                'SEPPOP','SEPUR',
                'SESUC','SETTRA',
                'SETUR','SF',
                'SG','SO',
                'SRH','SS']
            
            numero_inicial = 2
            numero_final = 110

            for item in range(numero_inicial, numero_final):

                try:

                    for orgao in orgaos:

                        self.buscador.pausa_media()

                        self.buscador.selecionar_opcao_no_dropdown('secretaria_pesq', orgao)
                    
                        self.buscador.clicar_no_elemento_xpath('/html/body/div[4]/div[3]/div/form/div[5]/button')

                        self.buscador.pausa_media()

                        # Botão de baixar
                        self.buscador.clicar_no_elemento_xpath('/html/body/div[4]/div[3]/div[1]/table/tbody/tr[2]/td/button[2]')

                        self.buscador.pausa_media()
    
                        self.buscador.retornar()


                except:
                    print('Inferno, os órgãos não foram selecionados...')
                
                try:
                    self.buscador.aguardar(5, "Troca a competência ")

                    # Clicar no item de competencia
                    self.buscador.clicar_no_elemento_xpath('/html/body/div[4]/div[3]/div/form/div[1]/span/span[1]/span/span[1]')

                    self.buscador.clicar_no_elemento_xpath('/html/body/span/span/span[2]/ul/li[' + str(item) +']')

                    self.buscador.pressionar_teclas('enter') 

                    self.buscador.pausa_media()
                
                except:

                    print('Erro ao trocar a competência')
 

        except:
            print('Não foi possível executar o script inteiro.')

  
    def manter_janela_aberta(self):
        while(True):
            pass