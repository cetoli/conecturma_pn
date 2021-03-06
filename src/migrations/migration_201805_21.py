from facade.facade_main import *
from control.dicionarios import TIPO_ESTRUTURA,TIPO_USUARIOS

facade=Facade()


facade.create_observador_facade(nome="administrador", senha="@onde2929", telefone="21999999999", cpf="0",email="admin", tipo='0',
                                            rede='0',escola='0')

facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['rede'], nome="Rede Conecturma", telefone="(21)99999999")

facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['escola'], nome="Escola Conecturma",telefone="(21)99999999", estado="Rio de Janeiro", uf="RJ",cep="123",numero='5',vinculo_rede = "1")

facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['turma'], nome="KND", quem_criou="Sr.Ninguem", serie='1', vinculo_escola="2")


facade.create_observador_facade(nome="gestor", senha="123", telefone="21999999999", cpf="0",email="gestor@conecturma.com.br", tipo=TIPO_USUARIOS['gestor'],
                                            escola='0', rede='1')

facade.create_observador_facade(nome="diretor", senha="123", telefone="21999999999", cpf="0",email="diretor@conecturma.com.br", tipo=TIPO_USUARIOS['diretor'],
                                            rede='1',escola='2')

facade.create_observador_facade(nome="professor", senha="123", telefone="21999999999", cpf="0",email="professor@conecturma.com.br", tipo=TIPO_USUARIOS['professor'],
                                            rede='1',escola='2', vinculo_turma='3')

facade.create_aluno_facade(nome="aluno", senha="123", matricula='123',vinculo_rede='1', escola='2')

facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['item'], nome="Cores", preco="0", tipo_item="1")
facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['item'], nome="Cores2", preco="5", tipo_item="1")
facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['item'], nome="Cores3", preco="10", tipo_item="1")

facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['item'], nome="Rosto", preco="0", tipo_item="2")
facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['item'], nome="Rosto2", preco="5", tipo_item="2")
facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['item'], nome="Rosto3", preco="10", tipo_item="2")

facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['item'], nome="Cabeça", preco="0", tipo_item="3")
facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['item'], nome="Cabeça2", preco="5", tipo_item="3")
facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['item'], nome="Cabeça3", preco="10", tipo_item="3")

facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['item'], nome="Corpo", preco="0", tipo_item="4")
facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['item'], nome="Corpo2", preco="5", tipo_item="4")
facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['item'], nome="Corpo3", preco="10", tipo_item="4")

facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['medalha'], nome="Medalha1",tipo_medalha='1')
facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['medalha'], nome="Medalha2",tipo_medalha='2')
facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['medalha'], nome="Medalha3",tipo_medalha='1')
facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['medalha'], nome="Medalha4",tipo_medalha='2')
facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['medalha'], nome="Medalha5",tipo_medalha='1')
