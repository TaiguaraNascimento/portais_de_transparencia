
class Entidade:

    entidade = None
    estado = None
    link_portal_da_transparencia = None
    endereco_para_download = None
    comentarios = None

    def __init__(self, 
        entidade:str, 
        estado:str, 
        link_portal_da_transparencia:str, 
        endereco_para_download: str,
        comentarios:str):

        self.entidade = entidade 
        self.estado = estado 
        self.link_portal_da_transparencia = link_portal_da_transparencia 
        self.endereco_para_download = endereco_para_download
        self.comentarios = comentarios
