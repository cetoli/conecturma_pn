from bottle import *

from facade.escola_facade import EscolaFacade
from facade.turma_facade import  TurmaFacade
from facade.aluno_facade import AlunoFacade
from facade.loja_facade import LojaFacade

escola_facade = EscolaFacade()
turma_facade = TurmaFacade()
aluno_facade = AlunoFacade()
loja_facade = LojaFacade()


""" Controle aluno """


@route('/aluno')
@view('aluno/aluno')
def aluno_read():
    """
    Cria o cookie para a sessao atual do aluno
    pagina inicial do aluno
    :return: None
    """
    if request.get_cookie("login", secret='2525'):
        return
    else:
        redirect('/')


""" Cadastro de aluno """


@route('/aluno/cadastro_aluno')
@view('aluno/aluno_cadastro')
def aluno():
    """
    Cookie e view para cadastrar aluno
    :return:
    """
    if request.get_cookie("login", secret='2525'):
        escolas = escola_facade.read_escola_facade()
        return dict(escolas = escolas)
    else:
        redirect('/')


@route('/aluno_cadastro', method='POST')
def create_aluno():
    """
    Direcionamento a pagina para criar aluno buscando , na tpl os parâmetros usuário , senha e matricula
    Chama a funçao create_aluno_facade
    :return:
    """
    escola = request.forms['escola']
    if aluno_facade.create_aluno_facade(nome=request.forms['aluno_nome'], escola=escola,senha=request.forms['senha']):
        redirect('/usuario')
    else:
        print("deu erro na criação do ALuno")


"""Read de aluno"""


@route('/aluno/ler_aluno')
@view('aluno/aluno_read')
def read_aluno():
    """
    Direciona para a função read_aluno_facade
    Chama a funçao read_aluno_facade

    :return: o dicionario com a id , usuário_nome e senha_aluno para ser usado pela tpl
    """

    """pesquisa_aluno = request.params['']"""
    """ return dict(aluno_pesquisado=pesquisa_aluno)"""

    if True or request.get_cookie("login", secret='2525'):
        usuarios = aluno_facade.read_aluno_facade()
        turma = turma_facade.read_turma_facade()
        alunos = [(aluno['id'], aluno['usuario_nome'], aluno['matricula'], aluno['turma_do_aluno']) for aluno in usuarios]
        return dict(aluno_id=alunos, turmas=turma)
    else:
        redirect('/')


@get('/turma_aluno')
def aluno_in_turma():
    """
    recebe todos os valores do submit e separa o numero do id da turma e os numeros de ids dos alunos , para colocar o id de um al8uno em uma turma
    e chama a funçao aluno_in_turma_facade
    :return:
    """
    escolhidos = request.query_string
    print(escolhidos)
    escolha = [aluno.split('=')[0].split('_')[1] for aluno in escolhidos.split('&') if 'aluno' in aluno]
    turma_add = request.query.get('escolhidos')
    print(escolhidos, escolha, turma_add)
    aluno_facade.aluno_in_turma_facade(escolha, turma_add)
    redirect('/')


""" Deletar aluno(usuario) """


@get('/deletar_alunos')
def deletar_aluno():
    """
    Pegaos ids para deletar os alunos (futuramente apenas coloca eles no lugar de desativados)
    Chama a funçao delete_aluno_facade
    :return: Deleta a entrada de dicionario equivalente e retorna ao menu
    """
    escolhidos = request.query_string
    deletar_ids = [aluno.split('=')[0].split('_')[1] for aluno in escolhidos.split('&') if 'aluno' in aluno]
    print(escolhidos, deletar_ids)
    aluno_facade.delete_aluno_facade(deletar_ids)
    redirect('/')





"""Ver medalhas"""


@route('/aluno/ver_itens_comprados')
@view('aluno/view_itens')
def ver_itens():
    """
    mostra os itens que o usuario tem posse
    chama os metodos : pesquisa_aluno_facade, ver_item_comprado_facade e pesquisa_iten_facade
    cria uma lista com os ids dos itens do aluno

    :return: dicionario de itens
    """

    usuario = aluno_facade.pesquisa_aluno_facade(request.get_cookie("login", secret='2524'))
    itens_comprado = aluno_facade.ver_item_comprado_facade(usuario.id)
    itens = []
    for y in itens_comprado:
        itens.append(loja_facade.pesquisa_item_facade(y))

    return dict(lista_itens=itens)


@route('/equipar_item', method='POST')
def equipar_item():
    """
    Equipar o avatar
    metodos chamados: pesquisa_aluno_facade,pesquisa_item_facade e equipar_item_facade
    :return:
    """

    usuario = aluno_facade.pesquisa_aluno_facade(request.get_cookie("login", secret='2524'))

    id_item = request.forms['id']
    item = loja_facade.pesquisa_item_facade(id_item)

    aluno_facade.equipar_item_facade(usuario.id, item)

    redirect('/aluno/ver_itens_comprados')

# """Pagina de aluno , anotaçoes"""
# @route('/anotacoes_aluno')
# @view('pagina_anotaçoes.tpl')
# def anotacoes_aluno():
#     pass
