from navegador.buscador import Buscador
from navegador.entidade import Entidade

class SCMontanha:

    def __init__(self) -> None:

        self.entidade = Entidade(
            'Montanha',       
            'ES', 
            'https://montanha-es.portaltp.com.br/consultas/pessoal/servidores.aspx',  
            'es_montanha',                                                                                  
            'xxxxxx')

        self.buscador = Buscador(self.entidade)

    def processar_entidade(self) -> None:

        anos = [
            '2022',
            '2021',
            '2020', 
            '2019', 
            '2018', 
            '2017', 
            '2016', 
            '2015']

        # self.abrir_para_aparecer_todas()

        # self.selecionar_ano('2018')

        # self.selecionar_mes('10')

        for um in range(10, 11):
            self.abrir_dados_abrir_item(um)


    def abrir_dados_abrir_item(self, item: int):

        try:
            
            matricula = self.buscador.obter_dados_de_elemento_por_xpath('/html/body/form/div[3]/main/div/div[2]/div[2]/div/div/div[2]/table/tbody/tr[' + str(item + 1) + ']/td[2]')
            nome = self.buscador.obter_dados_de_elemento_por_xpath('/html/body/form/div[3]/main/div/div[2]/div[2]/div/div/div[2]/table/tbody/tr[' + str(item + 1) + ']/td[3]')
            ano = self.buscador.obter_dados_de_elemento_por_xpath('/html/body/form/div[3]/main/div/div[2]/div[2]/div/div/div[2]/table/tbody/tr[' + str(item + 1) + ']/td[9]')
            mes = self.buscador.obter_dados_de_elemento_por_xpath('/html/body/form/div[3]/main/div/div[2]/div[2]/div/div/div[2]/table/tbody/tr[' + str(item + 1) + ']/td[10]')
        
            print(matricula, nome, ano, mes)

            
            # Abrir o funcionario
            self.buscador.clicar_no_elemento_xpath('/html/body/form/div[3]/main/div/div[2]/div[2]/div/div/div[2]/table/tbody/tr[' + str(item + 1) + ']/td[1]/a/span/i[2]')



            '''
            self.buscador.aguardar(3, 'funcionario')

            # Abrir o historico de remuneração
            self.buscador.clicar_no_elemento_xpath('/html/body/form/div[3]/main/div/div[2]/div[2]/div/div[2]/div/ul/li[2]/a')

            self.buscador.aguardar(3, 'clica no historico')

            # Clicar no botao de relatório
            self.buscador.clicar_no_elemento_xpath('/html/body/form/div[3]/main/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/button')

            self.buscador.aguardar(3, 'clica no botao relatorio')

            # Clicar o item de download
            self.buscador.clicar_no_elemento_xpath('/html/body/form/div[3]/main/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/ul/li[5]/a')

            self.buscador.aguardar(3, 'clica no botao download')
                                                                   
            '''

            


        except:
            print('Erro ao abrir o item ' + str(item + 1))



    def selecionar_mes(self, mes: str):

        self.buscador.pausa_curtissima()
        self.buscador.clicar_no_elemento_xpath('/html/body/form/div[3]/main/div/div[2]/div[1]/div[3]/div/div/div[2]/span')
        self.buscador.pausa_curta()

        print(mes)

        match mes:
            case '1':
                texto = '/html/body/form/div[3]/main/div/div[2]/div[1]/div[3]/div/div/div[2]/div/ul/li[2]'

            case '2':
                texto = '/html/body/form/div[3]/main/div/div[2]/div[1]/div[3]/div/div/div[2]/div/ul/li[3]'

            case '3':
                texto = '/html/body/form/div[3]/main/div/div[2]/div[1]/div[3]/div/div/div[2]/div/ul/li[4]'

            case '4':
                texto = '/html/body/form/div[3]/main/div/div[2]/div[1]/div[3]/div/div/div[2]/div/ul/li[5]'

            case '5':
                texto = '/html/body/form/div[3]/main/div/div[2]/div[1]/div[3]/div/div/div[2]/div/ul/li[6]'
                
            case '6':
                texto = '/html/body/form/div[3]/main/div/div[2]/div[1]/div[3]/div/div/div[2]/div/ul/li[7]'

            case '7':
                texto = '/html/body/form/div[3]/main/div/div[2]/div[1]/div[3]/div/div/div[2]/div/ul/li[8]'
                
            case '8':
                texto = '/html/body/form/div[3]/main/div/div[2]/div[1]/div[3]/div/div/div[2]/div/ul/li[9]'

            case '9':
                texto = '/html/body/form/div[3]/main/div/div[2]/div[1]/div[3]/div/div/div[2]/div/ul/li[10]'

            case '10':
                self.buscador.clicar_em_posicao_especifica_na_tela(1226, 714)
                self.buscador.clicar_em_posicao_especifica_na_tela(1226, 714)
                self.buscador.clicar_em_posicao_especifica_na_tela(1226, 714)
                self.buscador.clicar_em_posicao_especifica_na_tela(1226, 714)
                self.buscador.pausa_curtissima()
                texto = '/html/body/form/div[3]/main/div/div[2]/div[1]/div[3]/div/div/div[2]/div/ul/li[7]'
                
            case '11':
                self.buscador.clicar_em_posicao_especifica_na_tela(1226, 714)
                self.buscador.clicar_em_posicao_especifica_na_tela(1226, 714)
                self.buscador.clicar_em_posicao_especifica_na_tela(1226, 714)
                self.buscador.clicar_em_posicao_especifica_na_tela(1226, 714)
                self.buscador.pausa_curtissima()
                texto = '/html/body/form/div[3]/main/div/div[2]/div[1]/div[3]/div/div/div[2]/div/ul/li[8]'

            case '12':
                self.buscador.clicar_em_posicao_especifica_na_tela(1226, 714)
                self.buscador.clicar_em_posicao_especifica_na_tela(1226, 714)
                self.buscador.clicar_em_posicao_especifica_na_tela(1226, 714)
                self.buscador.clicar_em_posicao_especifica_na_tela(1226, 714)
                self.buscador.pausa_curtissima()
                texto = '/html/body/form/div[3]/main/div/div[2]/div[1]/div[3]/div/div/div[2]/div/ul/li[9]'
        
        self.buscador.clicar_no_elemento_xpath(texto)


    def abrir_para_aparecer_todas(self):
        # Filtra todas
        self.buscador.clicar_no_elemento_xpath('/html/body/form/div[3]/main/div/div[2]/div[2]/div/div/div[2]/div[2]/nav/div[2]/div/div/span')
        self.buscador.pausa_curta()
        self.buscador.clicar_no_elemento_xpath('/html/body/form/div[3]/main/div/div[2]/div[2]/div/div/div[2]/div[2]/nav/div[2]/div/div/ul/li[7]/a')
        self.buscador.pausa_longa()
 


    def selecionar_ano(self, ano: str):
        # Abrir o buscador de ano
        self.buscador.clicar_no_elemento_xpath('/html/body/form/div[3]/main/div/div[2]/div[1]/div[2]/div/div/div[2]/span/span')
        
        self.buscador.pausa_curta()

        match ano:
            case '2022' :
                texto = '/html/body/form/div[3]/main/div/div[2]/div[1]/div[2]/div/div/div[2]/div/ul/li[2]/a'
            case '2021':
                texto = '/html/body/form/div[3]/main/div/div[2]/div[1]/div[2]/div/div/div[2]/div/ul/li[3]/a'
            case '2020':
                texto = '/html/body/form/div[3]/main/div/div[2]/div[1]/div[2]/div/div/div[2]/div/ul/li[4]/a'
            case '2019':
                texto = '/html/body/form/div[3]/main/div/div[2]/div[1]/div[2]/div/div/div[2]/div/ul/li[5]/a'
            case '2018':
                texto = '/html/body/form/div[3]/main/div/div[2]/div[1]/div[2]/div/div/div[2]/div/ul/li[6]/a'
            case '2017':
                texto = '/html/body/form/div[3]/main/div/div[2]/div[1]/div[2]/div/div/div[2]/div/ul/li[7]/a'
            case '2016':
                texto = '/html/body/form/div[3]/main/div/div[2]/div[1]/div[2]/div/div/div[2]/div/ul/li[8]/a'
            case '2015':
                texto = '/html/body/form/div[3]/main/div/div[2]/div[1]/div[2]/div/div/div[2]/div/ul/li[9]/a'
            case '2014':
                texto = '/html/body/form/div[3]/main/div/div[2]/div[1]/div[2]/div/div/div[2]/div/ul/li[10]/a'
    
        self.buscador.clicar_no_elemento_xpath(texto)


    def manter_janela_aberta(self):
        while(True):
            pass