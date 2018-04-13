from model.estrutura_model import DbEstrutura

estrutura = '2'

class EscolaFacade:

    def __init__(self):
        """
        método para utilização do banco de dados
        """
        self.escola = DbEstrutura()

    def create_escola_facade(self, nome, numero, telefone, estado, uf,vinculo_rede, cep):
        return self.escola.create_estrutura(nome=nome, tipo_estrutura=estrutura,telefone=telefone, cep=cep,estado=estado,
                                            uf=uf, numero=numero, vinculo_rede=vinculo_rede)

    def read_escola_facade(self):
        return self.escola.read_estrutura(tipo_estrutura=estrutura)

    def update_escola_facade(self, id, nome, rua, numero, cidade, estado, telefone, rede_pertencente,
                             cod_identificacao):
        return self.escola.update_escola(id, nome, rua, numero, cidade, estado, telefone, rede_pertencente,
                                         cod_identificacao)

    def delete_escola_facade(self, deletar_ids):
        return self.escola.delete_escola(deletar_ids)

    def search_escola_id_facade(self, id):
        return self.escola.search_estrutura_id(id=id)

    def search_escola_facade(self, nome):
        return self.escola.search_estrutura(tipo_estrutura=estrutura,nome=nome)
