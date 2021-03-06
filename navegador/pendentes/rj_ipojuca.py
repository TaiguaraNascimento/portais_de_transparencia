from navegador.buscador import Buscador
from navegador.entidade import Entidade


class RJIpojuca:
    def __init__(self) -> None:

        links = [
            [2016, 'http://s2.asp.srv.br/etransparencia.pm.ipojuca.pe/servlet/wwpessoalservidor?rXGyD5hur9qZbly23+MiuGcD5ZtNBDFt+AzAY8UF+OCGP0HQEEIAjPKjB9k2_LMV'],
            [2017, 'http://s2.asp.srv.br/etransparencia.pm.ipojuca.pe/servlet/wwpessoalservidor?rXGyD5hur9qZbly23+MiuJB7YFoJKAj9gYguaIJI5c3SZraa8tzG2NnBovD8wvpz'],
            [2018, 'http://s2.asp.srv.br/etransparencia.pm.ipojuca.pe/servlet/wwpessoalservidor?rXGyD5hur9qZbly23+MiuLezmSEQg_ko55_GW97sJ72B3zuoibLXhHovZ2YuNP3M'],
            [2019, 'http://s2.asp.srv.br/etransparencia.pm.ipojuca.pe/servlet/wwpessoalservidor?rXGyD5hur9qZbly23+MiuD7YsfaKI5vB6L43qxx7uVMTCbin8R70XH5n0qmO2o6c'],
            [2020, 'http://s2.asp.srv.br/etransparencia.pm.ipojuca.pe/servlet/wwpessoalservidor?rXGyD5hur9qZbly23+MiuJSqwETiFW_sZoW8ovmvZhPmRqZVWPVdrwXXLLjZuzGU'],
            [2021, 'http://s2.asp.srv.br/etransparencia.pm.ipojuca.pe/servlet/wwpessoalservidor?rXGyD5hur9qZbly23+MiuFoRbiSUUbqHCHZ5w2hB4D8sSJWYvBlXnuGEnj2b9IIA'],
            [2022, 'http://s2.asp.srv.br/etransparencia.pm.ipojuca.pe/servlet/wwpessoalservidor?rXGyD5hur9qZbly23+MiuMYGj+kcaaxah5JU7F1Juu4oaBAU_N7fRGdAugeykPZq'],
        ]

        self.entidade = Entidade(
            'Ipojuca',         
            'RJ', 
            'http://s2.asp.srv.br/etransparencia.pm.ipojuca.pe/servlet/wppessoalconsulta', 
            links[0],
            'A partir de 01/2017, porém está por órgão.')

        self.buscador = Buscador(self.entidade)

    def processar_entidade(self) -> None:

        mes_inicial = 1
        mes_final = 12

        for mes in range(mes_inicial, mes_final + 1):

            # Seleciona o mês
            self.buscador.selecionar_opcao_no_dropdown('vMES', str(mes))

            self.buscador.pausa_curta()

            # self.buscador.clicar_no_elemento_xpath('//*[@id="EXPORTCSV"]')


    def manter_janela_aberta(self):
        while(True):
            pass