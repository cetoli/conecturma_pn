from bottle import route, view, get, request, redirect
from facade.turma_facade import TurmaFacade
from facade.escola_facade import EscolaFacade

turma_facade = TurmaFacade()
escola_facade = EscolaFacade()
""" Controle de Turma """


@route('/turma')
@view('turma/turma')
def view_turma():
    turmas = controller_read_turma()
    return dict(turma=turmas)


""" Create Turma """


@route('/turma/turma_cadastro')
@view('turma/turma_cadastro')
def view_cadastrar_turma():
    """
    pagina de cadastro de turma
    :return:
    """
    escola = escola_facade.read_escola_facade()
    return dict(escolas=escola)


@route('/turma/cadastro_turma', method='POST')
def controller_create_turma():
    """
    Pagina para chamar a funçao create_turma , pedindo pelo tpl o parametro turma_nome
    :return: cria uma entrada no banco de dados da turma criada
    """
    turma = request.forms['turma_nome']
    serie = request.forms['serie']
    escola = request.forms['escola']
    turma_facade.create_turma_facade(nome=turma, login=request.get_cookie("login", secret='2524'), serie=serie, escola=escola)

    redirect('/turma')

def controller_read_turma():
    """
    Direciona para a pagina que mostra a turma em ordem de id
    :return: a entrada de dicionario que contem o id e o turma_nome
    """
    turmas = turma_facade.read_turma_facade()
    if turmas == None:
        return None
    else:

        turma = []
        for t in turmas:
            escola = escola_facade.search_escola_id_facade(t['escola'])
            t['escola'] = escola['nome']

            if t['serie'] == 0:
                t['serie'] = "Pré-escola"
            elif t['serie'] == 1:
                t['serie'] = "1ª Ano"
            elif t['serie'] == 2:
                t['serie'] = "2ª Ano"
            elif t['serie'] == 3:
                t['serie'] = "3ª Ano"
            elif t['serie'] == 4:
                t['serie'] = "4ª Ano"
            elif t['serie'] == 5:
                t['serie'] = "5ª Ano"
            turma.append(t)

        return turma


"""Turma Delete"""


@get('/deletar_turma')
def deletar_turma():
    turma_facade.delete_turma_facade(request.params['id'])
    redirect('/turma')
