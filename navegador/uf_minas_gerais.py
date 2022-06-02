from navegador.buscador import Buscador
from navegador.entidade import Entidade

class UFMinasGerais:
    def __init__(self) -> None:

        self.entidade = Entidade('Estado de MG',
            'MG', 
            'https://www.transparencia.mg.gov.br/estado-pessoal/remuneracao-dos-servidores',
            'uf_minas_gerais',
            'A partir de 01/2019, porém está por servidor (pesquisa por nome).')

        self.buscador = Buscador(self.entidade)


    def processar_entidade(self) -> None:

        ano_inicial = 5
        ano_final = 8
            
        self.buscador.pausa_curta()

        for ano in range(ano_inicial, ano_final):

            for mes in self.buscador.meses:

                try:
                    
                    # Selecionar o ano
                    self.buscador.selecionar_opcao_no_dropdown('jform_ano', self.buscador.anos[ano])

                    self.buscador.pausa_curta()

                    # Selecionar o mês
                    self.buscador.selecionar_opcao_no_dropdown('jform_mes_ini', mes[0])
                    
                    self.buscador.pausa_curta()

                    # Selecionar tipo
                    self.buscador.selecionar_opcao_no_dropdown('jform_consulta', "3")

                    self.buscador.pausa_curta()

                    # Clicar no botão pesquisar
                    self.buscador.clicar_no_elemento_xpath('//*[@id="estado_remuneracao-form"]/div[7]/div/button[1]')
                    
                    # Clicar no bitão download da planilha
                    self.buscador.clicar_no_elemento_xpath('//*[@id="btn_download_plan"]')

                except:
                    print('Não foi possível obter ' + str(mes[1]) + ' e ' + str(ano))


    def manter_janela_aberta(self):
        while(True):
            pass
