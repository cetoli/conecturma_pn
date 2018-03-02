from bottle import route, view, get, request, redirect
from facade.facade import Facade

facade = Facade()

""" Controle aluno """


@route('/aluno')
@view('aluno/aluno')
def aluno_read():
    return


""" Cadastro de aluno """


@route('/cadastro_aluno')
@view('aluno/aluno_cadastro')
def aluno():
    return


@route('/aluno_cadastro', method='POST')
def create_aluno():
    """
    Direcionamento a pagina para criar aluno buscando , na tpl os parâmetros usuário , senha e matricula
    :return: cria o aluno e volta para a pagina geral aluno
    """
    facade.CreateAlunoFacade(request.forms['aluno_nome'], request.forms['senha'])
    redirect('/')


"""Read de aluno"""


@route('/ler_aluno')
@view('aluno/aluno_read')
def read_aluno():
    """
    Direciona para a função ReadAlunoFacade

    :return: o dicionario com a id , usuário_nome e senha_aluno para ser usado pela tpl
    """
    usuarios = facade.ReadAlunoFacade()

    return dict(aluno_id=usuarios['id'], aluno_matricula=usuarios['matricula'], aluno_nome=usuarios['usuario_nome'])



""" Deletar aluno(usuario) """
@get('/deletar_alunos')
def deletar_aluno():
    """
    Direciona a função DeleteAlunoFacade para a pagina tpl

    :return: Deleta a entrada de dicionario e retorna a pagina geral aluno
    """
    facade.DeleteAlunoFacade(request.params['id'])
    redirect('/aluno')


"""Pesquisa ao aluno por nome"""
