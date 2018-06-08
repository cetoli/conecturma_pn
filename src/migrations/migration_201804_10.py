from facade.observador_facade import ObservadorFacade
from facade.loja_facade import LojaFacade
from facade.medalha_facade import MedalhaFacade

from facade.aluno_facade import AlunoFacade


observador_facade = ObservadorFacade()
loja_facade = LojaFacade()
medalha_facade = MedalhaFacade()

aluno_facade = AlunoFacade()

observador_facade.create_observador_facade(nome="administrador", senha="@onde2929", telefone="21999999999", cpf="0",email="admin", tipo='0',
                                            rede='0',escola='0')
observador_facade.create_observador_facade(nome="allan", senha="123", telefone="21999999999", cpf="0",email="allan@conecturma.com.br", tipo='3',
                                            rede='0',escola='0')

"""rede_facade.create_rede_facade(nome="Rede Conecturma", telefone="(21)99999999")

escola_facade.create_escola_facade(nome = "Escola Conecturma",telefone="(21)99999999", estado="Rio de Janeiro", uf="RJ",cep="123",numero='5',vinculo_rede = "1")

turma_facade.create_turma_facade(nome="KND", login="Sr.Ninguem",serie=1, escola="2")"""

"""
loja_facade.create_estrutura_facade(nome="Cores", preco="0", tipo="1")
loja_facade.create_estrutura_facade(nome="Cores2", preco="5", tipo="1")
loja_facade.create_estrutura_facade(nome="Cores3", preco="10", tipo="1")

loja_facade.create_estrutura_facade(nome="Rosto", preco="0", tipo="2")
loja_facade.create_estrutura_facade(nome="Rosto2", preco="5", tipo="2")
loja_facade.create_estrutura_facade(nome="Rosto3", preco="10", tipo="2")

loja_facade.create_estrutura_facade(nome="Cabeça", preco="0", tipo="3")
loja_facade.create_estrutura_facade(nome="Cabeça2", preco="5", tipo="3")
loja_facade.create_estrutura_facade(nome="Cabeça3", preco="10", tipo="3")

loja_facade.create_estrutura_facade(nome="Corpo", preco="0", tipo="4")
loja_facade.create_estrutura_facade(nome="Corpo2", preco="5", tipo="4")
loja_facade.create_estrutura_facade(nome="Corpo3", preco="10", tipo="4")

medalha_facade.create_medalha_facade(nome="Medalha1",tipo=1)
medalha_facade.create_medalha_facade(nome="Medalha2",tipo=2)
medalha_facade.create_medalha_facade(nome="Medalha3",tipo=1)
medalha_facade.create_medalha_facade(nome="Medalha4",tipo=2)
medalha_facade.create_medalha_facade(nome="Medalha5",tipo=1)"""

