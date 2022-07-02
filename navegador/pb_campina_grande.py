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

        self.popular_dados_importantes()

        self.buscador = Buscador(self.entidade)

    def processar_entidade(self) -> None:


       

        ano_inicial = 2015
        ano_final = 2022

        for ano in range(ano_inicial, ano_final):

            

            for orgao in self.orgaos:
                
                self.buscador.pausa_curta()

                

                

                self.buscador.pausa_curta()

                

                self.buscador.pausa_curta()
                linhas_da_tabela = '//*[@id="centro"]/div[2]/table/tbody/tr'
                print(self.buscador.contar_ocorrencias_de_xpath(linhas_da_tabela))



                mes_inicial = 1
                mes_final = 12

                for mes in range(mes_inicial, mes_final):

                    codigo = mes + 1 # Para simular o número no xpath
                    # self.buscador.clicar_no_elemento_xpath('//*[@id="centro"]/div[2]/table/tbody/tr[' + str(codigo) + ']/td[4]/div/a/img')



        
    def manter_janela_aberta(self):
        while(True):
            pass

    def popular_dados_importantes(self):

        

        self.meses = [
            [1, 'Janeiro'],
            [2, 'Fevereiro'],
            [3, 'Março'],
            [4, 'Abril'],
            [5, 'Maio'],
            [6, 'Junho'],
            [7, 'Julho'],
            [8, 'Agosto'],
            [9, 'Setembro'],
            [10, 'Outubro'],
            [11, 'Novembro'],
            [12, 'Dezembro']
        ]

        self.municipios = [
            ['001', 'Água Branca'], 
            ['002', 'Aguiar'], 
            ['003', 'Alagoa Grande'], 
            ['004', 'Alagoa Nova'], 
            ['005', 'Alagoinha'], 
            ['006', 'Alcantil'], 
            ['007', 'Algodão de Jandaíra'], 
            ['008', 'Alhandra'], 
            ['009', 'Amparo'], 
            ['010', 'Aparecida'], 
            ['011', 'Araçagi'], 
            ['012', 'Arara'], 
            ['013', 'Araruna'], 
            ['014', 'Areia'], 
            ['015', 'Areia de Baraúnas'], 
            ['016', 'Areial'], 
            ['017', 'Aroeiras'], 
            ['018', 'Assunção'], 
            ['019', 'Baía da Traição'], 
            ['020', 'Bananeiras'], 
            ['021', 'Baraúna'], 
            ['022', 'Barra de Santa Rosa'], 
            ['023', 'Barra de Santana'], 
            ['024', 'Barra de São Miguel'], 
            ['025', 'Bayeux'], ['026', 'Belém'], 
            ['027', 'Belém do Brejo do Cruz'], 
            ['028', 'Bernardino Batista'], 
            ['029', 'Boa Ventura'], 
            ['030', 'Boa Vista'],
            ['031', 'Bom Jesus'], 
            ['032', 'Bom Sucesso'], 
            ['033', 'Bonito de Santa Fé'], 
            ['034', 'Boqueirão'], 
            ['035', 'Borborema'], 
            ['036', 'Brejo do Cruz'], 
            ['037', 'Brejo dos Santos'], 
            ['038', 'Caaporã'], 
            ['039', 'Cabaceiras'], 
            ['040', 'Cabedelo'], 
            ['041', 'Cachoeira dos Índios'], 
            ['042', 'Cacimba de Areia'], 
            ['043', 'Cacimba de Dentro'], 
            ['044', 'Cacimbas'],
            ['045', 'Caiçara'], 
            ['046', 'Cajazeiras'], 
            ['047', 'Cajazeirinhas'], 
            ['048', 'Caldas Brandão'], 
            ['049', 'Camalaú'], 
            ['050', 'Campina Grande'], 
            ['052', 'Capim'],
            ['053', 'Caraúbas'],
            ['054', 'Carrapateira'], 
            ['055', 'Casserengue'],
            ['056', 'Catingueira'], 
            ['057', 'Catolé do Rocha'], 
            ['058', 'Caturité'], 
            ['059', 'Conceição'], 
            ['060', 'Condado'], 
            ['061', 'Conde'], 
            ['062', 'Congo'], 
            ['063', 'Coremas'], 
            ['064', 'Coxixola'],
            ['065', 'Cruz do Espírito Santo'],
            ['066', 'Cubati'], 
            ['067', 'Cuité'], 
            ['068', 'Cuité de Mamanguape'], 
            ['069', 'Cuitegi'], 
            ['070', 'Curral de Cima'], 
            ['071', 'Curral Velho'], 
            ['072', 'Damião'], 
            ['073', 'Desterro'],
            ['074', 'Diamante'], 
            ['075', 'Dona Inês'], 
            ['076', 'Duas Estradas'], 
            ['077', 'Emas'], 
            ['078', 'Esperança'], 
            ['079', 'Fagundes'], 
            ['080', 'Frei Martinho'],
            ['081', 'Gado Bravo'], 
            ['082', 'Guarabira'], 
            ['083', 'Gurinhém'], 
            ['084', 'Gurjão'], 
            ['085', 'Ibiara'],
            ['086', 'Igaracy'], 
            ['087', 'Imaculada'], 
            ['088', 'Ingá'], 
            ['089', 'Itabaiana'], 
            ['090', 'Itaporanga'], 
            ['091', 'Itapororoca'], 
            ['092', 'Itatuba'], 
            ['093', 'Jacaraú'], 
            ['094', 'Jericó'], 
            ['095', 'João Pessoa'],
            ['096', 'Juarez Távora'], 
            ['097', 'Juazeirinho'], 
            ['098', 'Junco do Seridó'], 
            ['099', 'Juripiranga'],
            ['100', 'Juru'], 
            ['101', 'Lagoa'],
            ['102', 'Lagoa de Dentro'], 
            ['103', 'Lagoa Seca'],
            ['104', 'Lastro'], 
            ['105', 'Livramento'], 
            ['106', 'Logradouro'], 
            ['107', 'Lucena'], 
            ['108', 'Mãe dÁgua'], 
            ['109', 'Malta'], 
            ['110', 'Mamanguape'], 
            ['111', 'Manaíra'], 
            ['112', 'Marcação'],
            ['113', 'Mari'],
            ['114', 'Marizópolis'], 
            ['115', 'Massaranduba'], 
            ['116', 'Mataraca'],
            ['117', 'Matinhas'], 
            ['118', 'Mato Grosso'], 
            ['119', 'Maturéia'], 
            ['120', 'Mogeiro'],
            ['121', 'Montadas'],
            ['122', 'Monte Horebe'], 
            ['123', 'Monteiro'], 
            ['124', 'Mulungu'], 
            ['125', 'Natuba'], 
            ['126', 'Nazarezinho'],
            ['127', 'Nova Floresta'],
            ['128', 'Nova Olinda'], 
            ['129', 'Nova Palmeira'],
            ['130', 'Olho dÁgua'], 
            ['131', 'Olivedos'],
            ['132', 'Ouro Velho'], 
            ['133', 'Parari'],
            ['134', 'Passagem'], 
            ['135', 'Patos'], 
            ['136', 'Paulista'], 
            ['137', 'Pedra Branca'], 
            ['138', 'Pedra Lavrada'],
            ['139', 'Pedras de Fogo'],
            ['140', 'Pedro Régis'], 
            ['141', 'Piancó'], 
            ['142', 'Picuí'], 
            ['143', 'Pilar'], 
            ['144', 'Pilões'], 
            ['145', 'Pilõezinhos'], 
            ['146', 'Pirpirituba'], 
            ['147', 'Pitimbu'],
            ['148', 'Pocinhos'], 
            ['149', 'Poço Dantas'], 
            ['150', 'Poço de José de Moura'],
            ['151', 'Pombal'], 
            ['152', 'Prata'], 
            ['153', 'Princesa Isabel'], 
            ['154', 'Puxinanã'], 
            ['155', 'Queimadas'],
            ['156', 'Quixabá'], 
            ['157', 'Remígio'], 
            ['158', 'Riachão'], 
            ['159', 'Riachão do Bacamarte'], 
            ['160', 'Riachão do Poço'],
            ['161', 'Riacho de Santo Antônio'], 
            ['162', 'Riacho dos Cavalos'], 
            ['163', 'Rio Tinto'], 
            ['164', 'Salgadinho'], 
            ['165', 'Salgado de São Félix'], 
            ['166', 'Santa Cecília'], 
            ['167', 'Santa Cruz'], 
            ['168', 'Santa Helena'],
            ['169', 'Santa Inês'], 
            ['170', 'Santa Luzia'], 
            ['171', 'Santa Rita'], 
            ['172', 'Santa Teresinha'],
            ['173', 'Santana de Mangueira'], 
            ['174', 'Santana dos Garrotes'], 
            ['175', 'Santarém'], 
            ['176', 'Santo André'], 
            ['177', 'São Bentinho'], 
            ['178', 'São Bento'], 
            ['179', 'São Domingos'], 
            ['180', 'São Domingos do Cariri'],
            ['181', 'São Francisco'], 
            ['182', 'São João do Cariri'], 
            ['183', 'São João do Rio do Peixe'], 
            ['184', 'São João do Tigre'],
            ['185', 'São José da Lagoa Tapada'], 
            ['186', 'São José de Caiana'], 
            ['187', 'São José de Espinharas'], 
            ['188', 'São José de Piranhas'], 
            ['189', 'São José de Princesa'],
            ['190', 'São José do Bonfim'], 
            ['191', 'São José do Brejo do Cruz'], 
            ['192', 'São José do Sabugi'], 
            ['193', 'São José dos Cordeiros'], 
            ['194', 'São José dos Ramos'], 
            ['195', 'São Mamede'], 
            ['196', 'São Miguel de Taipu'], 
            ['197', 'São Sebastião de Lagoa de Roça'],
            ['198', 'São Sebastião do Umbuzeiro'], 
            ['199', 'São Vicente do Seridó'], 
            ['200', 'Sapé'], 
            ['201', 'Serra Branca'],
            ['202', 'Serra da Raiz'], 
            ['203', 'Serra Grande'],
            ['204', 'Serra Redonda'], 
            ['205', 'Serraria'], 
            ['206', 'Sertãozinho'], 
            ['207', 'Sobrado'], 
            ['208', 'Solânea'], 
            ['209', 'Soledade'],
            ['210', 'Sossêgo'],
            ['211', 'Sousa'],
            ['212', 'Sumé'], 
            ['051', 'Tacima'],
            ['213', 'Taperoá'], 
            ['214', 'Tavares'],
            ['215', 'Teixeira'], 
            ['216', 'Tenório'], 
            ['217', 'Triunfo'], 
            ['218', 'Uiraúna'], 
            ['219', 'Umbuzeiro'], 
            ['220', 'Várzea'], 
            ['221', 'Vieirópolis'], 
            ['222', 'Vista Serrana'], 
            ['223', 'Zabelê']]