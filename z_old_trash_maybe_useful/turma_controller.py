from bottle import route, view, get, request, redirect, template
from facade.facade_main import Facade
from facade.observador_facade import ObservadorFacade

facade = Facade()

observador_facade = ObservadorFacade()
""" Controle de Turma """


@route('/turma')
@view('turma/turma')
def view_turma():
    """
    Pagina inicial de turmas e q mostra as turmas ja cadastradas
    metodos utilizados : controller_read_ turma :interno dessa pagina:
    :return: dicionario com os parametros da turma a serem mostrados
    """
    turmas = controller_read_turma()
    return dict(turma=turmas)


""" Create Turma """


@route('/turma/turma_cadastro')
@view('turma/turma_cadastro')
def view_cadastrar_turma():
    """
    Pagina de cadastro de turma , mostra as escolas ja cadastradas no banco de dados
    metodos usados: read_escola_facade
    :return:o dicionario com as escolas
    """

    observador = facade.search_observador_facade(request.get_cookie("login", secret='2525'))
    if observador['tipo'] == '2':
        escola = facade.search_estrutura_id_facade(int(observador['vinculo_escola']))
        return dict(escolas=escola, observador_tipo = observador['tipo'])
    elif observador['tipo'] == '1':
        escola = []
        escolas = facade.read_estrutura_facade(tipo_estrutura='2')
        for e in escolas:
            if e['vinculo_rede'] is observador['vinculo_rede']:
                escola.append(e)

        return dict(escolas=escola, observador_tipo=observador['tipo'])
    elif observador['tipo'] == '0':
        escola = facade.read_estrutura_facade(tipo_estrutura='2')
        return dict(escolas=escola, observador_tipo=observador['tipo'])

@route('/turma/turma_update', method='POST')
def view_update_turma():
    """
    Pagina de cadastro de turma , mostra as escolas ja cadastradas no banco de dados
    metodos usados: read_escola_facade
    :return:o dicionario com as escolas
    """
    id = request.forms['id_turma']

    turma = facade.search_turma_id_facade(int(id))
    aluno = facade.search_aluno_escola_facade(turma['escola'])
    alunos = []
    for a in aluno:
        if a['vinculo_turma'] == '0':
            alunos.append(a)

    professor = facade.search_observador_professor_by_escola_facade(turma['escola'])
    professores = []
    for p in professor:
        if p['vinculo_turma'] is '0':
            professores.append(p)

    return template('turma/turma_update', turma=turma, aluno = alunos, professor = professores)

@route('/turma/turma_update_controller', method='POST')
def controller_update_turma():

    teste = request.forms

    turma = request.forms['turma']
    alunos = [aluno.split('_')[1] for aluno in teste if 'aluno' in aluno]
    professores = [professor.split('_')[1] for professor in teste if 'professor' in professor]

    if alunos is not '' or alunos is not []:
        for a in alunos:
            facade.aluno_in_turma_facade(id_aluno=int(a),vinculo_turma=turma)

    if professores is not '' or professores is not []:
        for p in professores:
            facade.obser(id_aluno=int(a),vinculo_turma=turma)


    redirect('/turma')

@route('/turma/cadastro_turma', method='POST')
def controller_create_turma():
    """
    """
    turma = request.forms['turma_nome']
    serie = request.forms['serie']
    escola = request.forms['escola']
    facade.create_estrutura_facade(nome=turma, tipo_estrutura='3',quem_criou=request.get_cookie("login", secret='2524'), serie=serie, vinculo_escola=escola)
    redirect('/turma')


def controller_read_turma():
    """
    Direciona para a pagina que mostra a turma e nomeia as series
    metodos usados: read_turma_facade
    :return: a entrada de dicionario que contem o id e o turma_nome
    """
    turmas = facade.read_estrutura_facade(tipo_estrutura='3')
    if turmas == None:
        return None
    else:

        turma = []
        for t in turmas:
            escola = facade.search_estrutura_id_facade(int(t['escola']))
            t['escola'] = escola['nome']
            t['serie'] = serie(t['serie'])
            turma.append(t)

        return turma


"""Turma Delete"""


@get('/deletar_turma')
def deletar_turma():
    """
    nao implementado
    :return:
    """
    facade.delete_turma_facade(request.params['id'])
    redirect('/turma')

def serie(id_serie):
    if id_serie == '0':
        return "Pré-escola"
    elif id_serie == '1':
        return "1ª Ano"
    elif id_serie == '2':
        return "2ª Ano"
    elif id_serie == '3':
        return "3ª Ano"
    elif id_serie == '4':
        return "4ª Ano"
    elif id_serie == '5':
        return "5ª Ano"