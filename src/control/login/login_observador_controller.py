from bottle import route, request, redirect, response
from datetime import datetime
from facade.Facade_main import Facade

facade = Facade()

@route('/login_observador', method='POST')
def controller_login_entrar_observador():
    """
    Faz o login na conta do usuário recebendo o usuário e senha

    :return: da acesso a pagina de gestao de aprendizagem(menu), caso o usuário e senha digitados estejam certos
    """
    nome = request.params['usuario']
    senha = request.params['senha']
    observador = valida_login_observador(nome, senha)
    if observador:
        create_cookie(nome)
        now = datetime.now()
        facade.login_date_facade(observador['id'], now)
        facade.create_historico_facade(observador['nome'], observador['tipo'])
        redirect('/gestao_aprendizagem')
    else:
        redirect('/')



def valida_login_observador(nome, senha):

    """
    Valida o login do aluno ,
    :param nome: nome de login
    :param senha: senha do usuario
    :return: true se o observador existir e se estiver com usuario e a senha certa
    """
    retorno = facade.search_observador_facade(nome)
    if retorno:
        if retorno['nome'] == nome and retorno['senha'] == senha:
            return retorno
        else:
            return False
    else:
        return False

def create_cookie(parametro):
    response.set_cookie("login", parametro, secret='2525')
