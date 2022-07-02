def rj_itatiaia():
    from navegador.rj_itatiaia_v1 import RJItatiaia 
    rj_itatiaia = RJItatiaia()
    rj_itatiaia.processar_entidade()
    rj_itatiaia.manter_janela_aberta()

# Executar
rj_itatiaia()