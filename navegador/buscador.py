import os
import time
from navegador.entidade import Entidade
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException    
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pyautogui as py
from datetime import datetime

class Buscador():

    # Endereço base do arquivo
    entidade = None

    # Define o driver
    driver = None

    pasta_de_organizacao = None # Endereço onde montar a pasta de organização
    pasta_origem = None # Pasta de onde os arquivos serão movidos.

    def __init__(self, entidade: Entidade) -> None:
        self.definir_entidade(entidade)
        self.popular_dados()
        self.abrir_navegador()

        self.pasta_de_organizacao = "C:\\Users\\Taiguara Nascimento\\OneDrive - GRANT THORNTON BRASIL\\OUTROS PROJETOS\\Projeto Santander\\Bases de Dados\\buffer\\"
        self.pasta_origem = 'C:\\Users\\Taiguara Nascimento\\Downloads\\'

    def abrir_navegador(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.entidade.link_portal_da_transparencia)

    def definir_entidade(self, entidade: Entidade) -> None:
        self.entidade = entidade

    def __nome_do_arquivo_de_log__(self) -> str:
        if str(self.entidade.entidade) == None or str(self.entidade.entidade) == '':
            nome_do_arquivo_de_log = 'log_de_processamento__XXXXXXXX.csv'
            endereco_para_download = 'C:\\Users\\Taiguara Nascimento\\Downloads\\'
        else:
            nome_do_arquivo_de_log = ('log_de_processamento__' + str(self.entidade.entidade) + '.csv').replace(' ', '_').lower()
            endereco_para_download = os.path.join(self.__endereco_base_para_download__(), self.entidade.endereco_para_download)
        return os.path.join(endereco_para_download, nome_do_arquivo_de_log)

    def __verificar_se_arquivo_existe__(self) -> bool:
        if os.path.exists(self.__nome_do_arquivo_de_log__()):
            return True
        else:
            return False
    
    def __criar_arquivo_de_log__(self) -> None:

        if self.__verificar_se_arquivo_existe__():
            if True:
                print('Arquivo de log existe e já está aberto.')
            elif False:
                print('Arquivo de log existe e mas está fechado.')

        else:
            print('Arquivo de log não existe.')

    def organizar_arquivos_baixados(self, pasta1: str, pasta2: str, nome_prefixo: str) -> None:

        try:
            pasta_para_organizacao = os.path.join(self.pasta_de_organizacao, self.entidade.endereco_para_download, pasta1, pasta2)
            lista_de_arquivos = [arquivo for arquivo in os.listdir(self.pasta_origem) if os.path.isfile(jos.path.join(self.pasta_origem, arquivo))]

            if os.path.exists(pasta_para_organizacao) != True:
                os.makedirs(pasta_para_organizacao)
            
            for arquivo in lista_de_arquivos:

                nome_atual = arquivo
                nome_novo_do_arquivo = nome_prefixo + '_____' + nome_atual

                os.rename(os.path.join(self.pasta_origem, nome_atual), os.path.join(pasta_para_organizacao, nome_novo_do_arquivo))
        
        except:
            print('# Erro ao organizar os arquivos da pasta de origem |', self.pasta_origem, '|')

    def popular_dados(self) -> None:
        # Dados dos seletores

        self.meses = [
            ['01', 'Janeiro'],
            ['02', 'Fevereiro'],
            ['03', 'Março'],
            ['04', 'Abril'],
            ['05', 'Maio'],
            ['06', 'Junho'],
            ['07', 'Julho'], 
            ['08', 'Agosto'], 
            ['09', 'Setembro'], 
            ['10', 'Outubro'], 
            ['11', 'Novembro'], 
            ['12', 'Dezembro']]

        self.anos = [
            '2014', 
            '2015', 
            '2016', 
            '2017', 
            '2018', 
            '2019', 
            '2020', 
            '2021', 
            '2022']

    def verificar_se_xpath_existe(self, xpath: str) -> bool:
        try:
            self.driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            return False
        return True 

    def pausa_curta(self) -> None:
        time.sleep(1)
    
    def pausa_curtissima(self) -> None:
        time.sleep(0.5)
    
    def pausa_longa(self) -> None:
        time.sleep(10)
    
    def pausa_media(self) -> None:
        time.sleep(5)

    def retornar(self) -> None:
        self.driver.back()

    def __endereco_base_para_download__(self) -> str:
        return 'C:\\Users\\Taiguara Nascimento\\OneDrive - GRANT THORNTON BRASIL\\OUTROS PROJETOS\\Projeto Santander\\Bases de Dados\\'

    def clicar_no_elemento_xpath(self, xpath) -> None:
        self.driver.find_element(By.XPATH, xpath).click()

    def clicar_no_elemento_por_id(self, id) -> None:
        self.driver.find_element(By.ID, id).click()

    def selecionar_opcao_no_dropdown(self, objeto: str, valor_para_pesquisar: str):
        seletor = Select(self.driver.find_element(By.ID, objeto))
        seletor.select_by_value(valor_para_pesquisar)

    def preencher_campo_de_input_por_id(self, objeto: str, texto_para_escrever: str):
        elemento = self.driver.find_element_by_id(objeto)
        elemento.send_keys(texto_para_escrever)

    def limpar_campo_de_input_por_id(self, objeto: str):
        self.driver.find_element_by_id(objeto).clear()

    def obter_posicao_de_elemento_por_xpath(self, xpath) -> None:
        elemento = self.driver.find_element(By.XPATH, xpath)
        return elemento.location

    def clicar_na_posicao_de_um_alimento_por_xpath(self, xpath) -> None:
        try:
            elemento = self.obter_posicao_de_elemento_por_xpath(xpath)
            print('O ponteiro será movido para posição: X ', elemento["x"], ' e Y ', elemento["y"])
            py.click(x=elemento["x"], y=elemento["y"])
        except:
            print('Não foi possível localizar o objeto.')

    def mes_atual(self) -> int:
        return datetime.now().month

    def ano_atual(self) -> int:
        return datetime.now().year

    def acionar_link_com_javascript(self, referencia_java) -> None:
        self.driver.execute_script(referencia_java)

    def alterar_zoom_da_tela(self, zoom: int) -> None:
        self.driver.execute_script("document.body.style.zoom='" + str(zoom) + "%'")