def testar_espirito_santo():
    from navegador.uf_espirito_santo import UFEspiritoSanto
    uf_espirito_santo = UFEspiritoSanto()
    uf_espirito_santo.processar_entidade()

def testar_minas_gerais():
    from navegador.uf_minas_gerais import UFMinasGerais
    uf_minas_gerais = UFMinasGerais()
    uf_minas_gerais.processar_entidade()
    uf_minas_gerais.manter_janela_aberta()

def testar_pb_campina_grande():
    from navegador.pendentes.pb_campina_grande import PBCampinaGrande
    pb_campina_grande = PBCampinaGrande()
    pb_campina_grande.processar_entidade()
    pb_campina_grande.manter_janela_aberta()

def testar_rj_ipojuca():
    from navegador.pendentes.rj_ipojuca import RJIpojuca 
    rj_ipojuca = RJIpojuca()
    rj_ipojuca.processar_entidade()
    rj_ipojuca.manter_janela_aberta()

def testar_mg_juiz_de_fora_camara():
    from navegador.pendentes.mg_juiz_de_fora_camara import MGJuizDeForaCamara 
    mg_juiz_de_fora_camara = MGJuizDeForaCamara()
    mg_juiz_de_fora_camara.processar_entidade()
    mg_juiz_de_fora_camara.manter_janela_aberta()

def testar_sc_santa_catarina():
    from navegador.uf_estado_de_santa_catarina import SCSantaCatarina 
    uf_estado_de_santa_catarina = SCSantaCatarina()
    uf_estado_de_santa_catarina.processar_entidade()
    uf_estado_de_santa_catarina.manter_janela_aberta()


# Executar

testar_sc_santa_catarina()


'''



Entidade('Estado do Amazonas', 'RJ', 'http://www.transparencia.am.gov.br/pessoal/',                                                                                                  'A partir de 01/2017, porém está por órgão.')













Entidade('Carapicuíba',        
'RJ', 
'http://www2.camaracarapicuiba.sp.gov.br/portaltransparencia/Pages/Geral/wfFolhaPagamento.aspx',                                                
'A partir de 01/2017, porém está por servidor (pesquisa por nome).')

Entidade('Resende/RJ',         
'RJ', 
'https://e-gov.betha.com.br/transparencia/01037-136/con_servidoresativos.faces?mun=OKdsadUWH3o%3D',                                             
'A partir de 01/2017, porém está por servidor.')

Entidade('Itaquaquecetuba',    
'RJ', 
'https://transparencia.itaquaquecetuba.sp.gov.br/TDAPortalClient.aspx?417',                                                                     
'A partir de 01/2017, apenas remuneração total.')

Entidade('Ipojuca/RJ',         
'RJ', 
'http://s2.asp.srv.br/etransparencia.pm.ipojuca.pe/servlet/wwpessoalservidor?rXGyD5hur9qZbly23+MiuAyngEAGtuD+loFBiAKAFoSH7KJ9E4cjjYPDHa2xRmgC', 
'A partir de 01/2017, porém está por órgão.')

Entidade('Itatiaia/RJ',        
'RJ', 
'https://e-gov.betha.com.br/transparencia/01037-136/con_servidoresativos.faces?mun=1R7DbiTV1F3ZWkqAKT7j1Q==',                                   
'A partir de 01/2017, porém está por servidor.')

Entidade('Cáceres/MT',         
'RJ', 
'http://177.4.174.14:5656/transparencia/',                                                                                                      
'A partir de 01/2017, porém está por órgão.')

Entidade('Niterói',            
'RJ', 
'https://transparencia.niteroi.rj.gov.br/#/folha-pagamento',                                                                                    
'A partir de 01/2017, porém está por servidor (pesquisa por nome).')

Entidade('Barra do Garças',    
'RJ', 
'https://www.gp.srv.br/transparencia_barradogarcas/servlet/contrato_servidor_v3?1',                                                             
'A partir de 01/2017, porém está por servidor (pesquisa por nome) ou por cargo.')

Entidade('Diamantino',         
'RJ', 
'https://www.gp.srv.br/transparencia_diamantino/servlet/contrato_servidor_v3?1',                                                                
'A partir de 01/2017, porém está por servidor (pesquisa por nome) ou por cargo.')

Entidade('Sooretama',          
'RJ', 
'https://www.sooretama.es.gov.br/transparencia/rh/servidores',                                                                                  
'A partir de 01/2017, porém está por servidor (pesquisa por nome) ou por cargo.')

Entidade('São Lourenço',       
'RJ', 
'http://transparencia.saolourenco.mg.gov.br/FolhaPagamento',                                                                                    
'A partir de 01/2017, porém está valor líquido.')

Entidade('São João do Sul',    
'RJ', 
'https://e-gov.betha.com.br/transparencia/01037-136/con_servidoresativos.faces',	                                                            
'A partir de 01/2017, porém está por servidor (pesquisa por nome) ou por cargo.')

Entidade('Estado do RJ',       
'RJ', 
'https://www.consultaremuneracao.rj.gov.br/ConsultaRemuneracao',                                                                                
'A partir de 01/2017, porém está por órgão.')

Entidade(
    'Estado do MT',       
    'RJ', 
    'http://seplag.mt.gov.br/index.php?pg=remuneracao',	                                                                                            
    'A partir de 01/2021, porém está por órgão.')
'''