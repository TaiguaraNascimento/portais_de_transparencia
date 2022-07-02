from navegador.buscador import Buscador
from navegador.entidade import Entidade

class PBCampinaGrande:

    def __init__(self) -> None:

        self.entidade = Entidade(
            'Campina Grande',
            'PB',
            'https://sagres.tce.pb.gov.br/pessoal01.php',
            'pb_campina_grande',
            'A partir de 01/2017, porém está por órgão.')

        self.buscador = Buscador(self.entidade)


    def processar_entidade(self) -> None:

        anos = ['2021']

        orgaos = [
            # ['605050', 'Fundo Municipal do Meio Ambiente de Campina Grande'],
            # ['601050', 'Fundo Municipal de Saúde de Campina Grande'], 
            ['301050', 'Instituto de Prev. dos Serv. Mun. de Campina Grande'], 
            ['302050', 'Agência Municipal de Desenvolvimento de Campina Grande'], 
            ['303050', 'Superintendência de Transportes Públicos de Campina Grande'], 
            ['304050', 'Empresa Municipal de Urbanização da Borborema'], 
            ['602050', 'Fundo Municipal da Infância e Adolescência de Campina Grande'], 
            ['603050', 'Fundo Municipal de Assistencia Social de Campina Grande'], 
            ['604050', 'Fundo Municipal de Defesa dos Direitos Difusos de Campina Grande']
            
            
            # ['201050', 'Prefeitura Municipal de Campina Grande'], 
        ]

        prontos = [
            ['101050', 'Câmara Municipal de Campina Grande']


        ]


        sem_dados = [
        ]

        

        # Abrir modelo antigo
        self.acessar_modelo_antigo()

        
        for ano in anos:

            for orgao in orgaos:

                arquivo_exportar = 'C:\\Users\\Taiguara Nascimento\OneDrive - Fundação Instituto de Administração\\__backup\\Desktop\\Saidas\\exportar_dados_' + ano + '_' + orgao[0] + '.txt'
            
                # Acessar o ano de 
                self.acessar_dados_da_entidade(ano, orgao)

                self.processar_meses_da_folha(orgao, ano, arquivo_exportar)

                self.fechar_a_pesquisa()
                self.acessar_modelo_antigo()




    def fechar_a_pesquisa(self):

        self.buscador.pausa_curtissima()

        # Clicar no X
        self.buscador.clicar_no_elemento_xpath('/html/body/div[1]/table/tbody/tr[2]/td[3]/table/tbody/tr/td/a[3]')

        self.buscador.pausa_curtissima()

        self.buscador.clicar_no_elemento_xpath('/html/body/div[2]/div/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div/input[1]')

        self.buscador.pausa_curtissima()










    def processar_meses_da_folha(self, orgao, ano, arquivo_exportar):

        with open(arquivo_exportar, "w") as f:

            f.write(str('-'*100) + '\n')

            print("######## Começar a obter dados da folha de pagamento ######## ")

            # Conta quantos meses existem listados - nivel 1
            qtde_meses = self.obter_quantidade_de_linhas_da_tabela('meses', 1)
            
            for mes in range(1, qtde_meses + 1):

                self.buscador.pausa_curtissima()

                dados_nivel_1 = self.coletar_dados_do_nivel_1(mes)

                #Acessar o mês específico
                self.buscador.clicar_no_elemento_xpath('/html/body/div[2]/div[2]/table/tbody/tr[' + str(mes+1) + ']/td[4]/div/a')

                # Entra no tipo de vinculo/detalhamento do tipo - nivel 2
                qtde_tipo = self.obter_quantidade_de_linhas_da_tabela('tipos de vinculos', 2)

                for tipo in range(1, qtde_tipo + 1):

                    self.buscador.pausa_curtissima()

                    # Exportar os dados dessa tela
                    dados_nivel_2 = self.coletar_dados_do_nivel_2(tipo)

                    # Acessa o tipo específico
                    self.buscador.clicar_no_elemento_xpath('/html/body/div[2]/div[2]/table/tbody/tr[' + str(tipo + 1 ) + ']/td[5]/div/a')

                    # Clica no cargo - nivel 3
                    qtde_cargo = self.obter_quantidade_de_linhas_da_tabela('cargos', 3)

                    for cargo in range(1, qtde_cargo + 1):

                        self.buscador.pausa_curtissima()

                        # Exportar os dados dessa tela
                        dados_nivel_3 = self.coletar_dados_do_nivel_3(cargo)
                        
                        self.buscador.clicar_no_elemento_xpath('/html/body/div[2]/div[2]/table/tbody/tr[' + str(cargo + 1 ) + ']/td[6]/div/a')

                        # Inicia o processo de copiar dados da tela
                        self.popular_arquivo_de_exportacao(f, orgao, ano, mes, dados_nivel_1, dados_nivel_2, dados_nivel_3)

                        self.buscador.clicar_em_link_text('Voltar')
                        
                    self.buscador.clicar_em_link_text('Voltar')

                self.buscador.clicar_em_link_text('Voltar')

            f.write('-'*100)

            f.close()
    
    
    
    def coletar_dados_do_nivel_1(self, mes):

        nome_do_mes = self.buscador.obter_valor_de_xpath('/html/body/div[2]/div[2]/table/tbody/tr[' + str(mes+1) + ']/td[1]')
        valor_do_mes = self.buscador.obter_valor_de_xpath('/html/body/div[2]/div[2]/table/tbody/tr[' + str(mes+1) + ']/td[2]')
        servidores_do_mes = self.buscador.obter_valor_de_xpath('/html/body/div[2]/div[2]/table/tbody/tr[' + str(mes+1) + ']/td[3]')

        # self.linhas_de_exportacao.append(['-'*100])
        # self.linhas_de_exportacao.append([self.nome_do_mes, self.valor_do_mes, self.servidores_do_mes])

        # print(self.nome_do_mes, self.valor_do_mes, self.servidores_do_mes)
            
        return [nome_do_mes, valor_do_mes, servidores_do_mes]

 
    
    def coletar_dados_do_nivel_2(self, tipo):
 
        linha = self.buscador.obter_valor_de_xpath('/html/body/div[2]/div[2]/table/tbody/tr[' + str(tipo+1) + ']/td[1]')
        descricao = self.buscador.obter_valor_de_xpath('/html/body/div[2]/div[2]/table/tbody/tr[' + str(tipo+1) + ']/td[2]')
        valor_do_mes1 = self.buscador.obter_valor_de_xpath('/html/body/div[2]/div[2]/table/tbody/tr[' + str(tipo+1) + ']/td[3]')
        servidores_do_mes1 = self.buscador.obter_valor_de_xpath('/html/body/div[2]/div[2]/table/tbody/tr[' + str(tipo+1) + ']/td[4]')

        # self.linhas_de_exportacao.append(['-'*100])
        # self.linhas_de_exportacao.append(['', '', '', self.linha, self.tipo, self.valor_do_mes1, self.servidores_do_mes1])

        # print(self.linha, self.tipo, self.valor_do_mes, self.servidores_do_mes)

        return [linha, descricao, valor_do_mes1, servidores_do_mes1]        
    

    def coletar_dados_do_nivel_3(self, cargo):
 
        linha1 = self.buscador.obter_valor_de_xpath('/html/body/div[2]/div[2]/table/tbody/tr[' + str(cargo+1) + ']/td[1]')
        codigo = self.buscador.obter_valor_de_xpath('/html/body/div[2]/div[2]/table/tbody/tr[' + str(cargo+1) + ']/td[2]')
        cargos = self.buscador.obter_valor_de_xpath('/html/body/div[2]/div[2]/table/tbody/tr[' + str(cargo+1) + ']/td[3]')
        tipo1 = self.buscador.obter_valor_de_xpath('/html/body/div[2]/div[2]/table/tbody/tr[' + str(cargo+1) + ']/td[4]')
        servidores_do_mes2 = self.buscador.obter_valor_de_xpath('/html/body/div[2]/div[2]/table/tbody/tr[' + str(cargo+1) + ']/td[5]')

        # self.linhas_de_exportacao.append(['-'*100])
        # self.linhas_de_exportacao.append(['', '', '', '', '', '', '', self.linha1, self.codigo, self.cargo, self.tipo1, self.servidores_do_mes2])

        # print(self.linha, self.codigo, self.cargo, self.tipo, self.servidores_do_mes)
            
        return [linha1, codigo, cargos, tipo1, servidores_do_mes2 ]



    def obter_quantidade_de_linhas_da_tabela(self, texto: str, qtde: int) -> int:

        qtde_linhas = self.buscador.contar_ocorrencias_de_classe('trConteudoCor1')
        qtde_linhas = qtde_linhas + self.buscador.contar_ocorrencias_de_classe('trConteudoCor2')

        saida = '-'*(5*qtde) + '> ' + texto.upper() + ': ' + str(qtde_linhas) 
        saida = saida + '-'*(70 - len(saida))

        # print(saida)
        
        return qtde_linhas




    def popular_arquivo_de_exportacao(self, arquivo, orgao, ano, mes, dados_nivel_1, dados_nivel_2, dados_nivel_3):

        qtde_funcionarios = self.obter_quantidade_de_linhas_da_tabela('funcionarios', 4)
        
        self.buscador.pausa_curtissima()

        for funcionario in range(1, qtde_funcionarios + 1):

            num = self.buscador.obter_valor_de_xpath('/html/body/div[2]/div[2]/table[1]/tbody/tr[' + str(funcionario + 1) + ']/td[1]')
            nome = self.buscador.obter_valor_de_xpath('/html/body/div[2]/div[2]/table[1]/tbody/tr[' + str(funcionario + 1) + ']/td[2]')
            unidade = self.buscador.obter_valor_de_xpath('/html/body/div[2]/div[2]/table[1]/tbody/tr[' + str(funcionario + 1) + ']/td[3]')
            salario = self.buscador.obter_valor_de_xpath('/html/body/div[2]/div[2]/table[1]/tbody/tr[' + str(funcionario + 1) + ']/td[4]')

            
            linha = [
                orgao[0], 
                orgao[1], 
                ano,
                mes,

                dados_nivel_1[0],
                dados_nivel_1[1],
                dados_nivel_1[2],

                dados_nivel_2[0],
                dados_nivel_2[1],
                dados_nivel_2[2],
                dados_nivel_2[3],

                dados_nivel_3[0],
                dados_nivel_3[1],
                dados_nivel_3[2],
                dados_nivel_3[3],
                dados_nivel_3[4],

                num, 
                nome,
                unidade, 
                salario
                ]
            
            # print(self.serializar(linha))

            arquivo.write(self.serializar(linha))

            # print(linha)


    def acessar_dados_da_entidade(self, ano: str, entidade: str):

        print(">>>>>> Acessando o município - Ano: ", ano, " - ", entidade[1], ' <<<<<<<')

        self.buscador.pausa_curtissima()

         # Seleciona o municipio correto
        self.buscador.selecionar_opcao_no_dropdown('ugestora', '050')

        # Seleciona o ano
        self.buscador.selecionar_opcao_no_dropdown('ano', str(ano))

        self.buscador.pausa_curta()

        self.buscador.selecionar_opcao_no_dropdown('entidade', entidade[0])

        # Clicar no botão Consultar
        self.buscador.clicar_no_elemento_xpath('//*[@id="form"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[4]/td/div/input[1]')

        self.buscador.pausa_curtissima()

        # Clicar em Pessoal
        self.buscador.clicar_no_elemento_xpath('//*[@id="menuItens"]/table/tbody/tr/td[7]/a')

        self.buscador.pausa_curtissima()


    def acessar_modelo_antigo(self):

        # Seleciona o modelo antigo
        self.buscador.clicar_no_elemento_xpath('//*[@id="parent-fieldname-text"]/div/div[1]/div[2]/p[1]/a/img')
        self.buscador.pausa_curtissima()

        
    def serializar(self, conteudo):

        saida = '|' +   str(conteudo[0]) + '|'
        saida = saida + str(conteudo[1]) + '|'
        saida = saida + str(conteudo[2]) + '|'
        saida = saida + str(conteudo[3]) + '|'
        saida = saida + str(conteudo[4]) + '|'
        saida = saida + str(conteudo[5]) + '|'
        saida = saida + str(conteudo[6]) + '|'
        saida = saida + str(conteudo[7]) + '|'
        saida = saida + str(conteudo[8]) + '|'
        saida = saida + str(conteudo[9]) + '|'
        saida = saida + str(conteudo[10]) + '|'
        saida = saida + str(conteudo[11]) + '|'
        saida = saida + str(conteudo[12]) + '|'
        saida = saida + str(conteudo[13]) + '|'
        saida = saida + str(conteudo[14]) + '|'
        saida = saida + str(conteudo[15]) + '|'
        saida = saida + str(conteudo[16]) + '|'
        saida = saida + str(conteudo[17]) + '|'
        saida = saida + str(conteudo[18]) + '|'
        saida = saida + str(conteudo[19]) + '|'
        saida = saida + '\n'

        return saida





    def manter_janela_aberta(self):
        print('############ TERMINOU ###############')
        while(True):
            pass