from bottle import *
from facade.facade import *

facade = Facade()


@route('/escola')
@view('escola/index')
def view_escola_index():
    return


@route('/escola/cadastro')
@view('escola/create_escola')
def view_escola_cadastro():
    return


@route('/escola/read_escola')
@view('escola/read_escola')
def view_escola_read():
    escola = controller_escola_read()
    return dict(escola=escola)


@get('/escola/editar')
def view_escola_update():
    nome = request.params['nome']
    escolas = facade.pesquisa_escola_facade(nome)
    return template('escola/update_escola', id=escolas['id'], nome=escolas['nome'], numero=escolas['numero'],estado=escolas['estado'],cidade=['cidade'],
                    telefone=escolas['telefone'], rua=escolas['rua'], rede_pertencente=escolas['rede_pertencente'],
                    cod_identificacao=escolas['cod_identificacao'])


@get('/escola/create_escola')
def controller_escola_cadastro():
    nome = request.params['nome']
    rua = request.params['rua']
    numero = request.params['numero']
    telefone = request.params['telefone']
    estado = request.params['estado']
    cidade = request.params['cidade']
    rede_pertencente = request.params['rede']
    cod_identificacao = request.params['cod_id']

    if filtro_cadastro(nome, rua, numero, telefone, estado, cidade, cod_identificacao):
        facade.create_escola_facade(nome, rua, numero, telefone, estado, cidade, rede_pertencente, cod_identificacao)
        redirect('/escola/cadastro')
    else:
        print("Erro para salvar")


def controller_escola_read():
    escolas = []
    for escola in facade.read_escola_facade():
        # escola['nome'] = escola(escola['nome'])
        escolas.append(escola)

    return escolas


@route('/escola/update_escola', method='POST')
def controller_escola_update():
    facade.update_escola_facade(id=request.params['id'], nome=request.params['nome'], rua=request.params['rua'],
                                  numero=request.params['numero'],
                                  telefone=request.params['telefone'], estado=request.params['estado'],
                                  cidade=request.params['cidade'], rede_pertencente=request.params['rede_pertencente'],
                                  cod_identificacao=request.params['cod_identificacao'])
    redirect('/escola/read_escola')


def filtro_cadastro(nome, telefone, rua, numero, estado, cidade, cod_identificacao):
    if nome == "":
        return False
    elif telefone == "":
        return False
    elif rua == "":
        return False
    elif numero == "":
        return False
    elif estado == "":
        return False
    elif cidade == "":
        return False
    elif cod_identificacao == "":
        return False
    else:
        return True
