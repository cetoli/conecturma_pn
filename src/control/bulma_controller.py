from bottle import route, view, request, redirect,response, template
from facade.facade_main import *
from control.classes.permissao import Login_Observador, Login_Aluno,algum_usuario_logado

facade = Facade()

from bottle import route, view, request, redirect, response
from facade.facade import Facade
__version__ = "0.0.1"
facade = Facade()

LOGIN = dict(
    titulo="Reconhecendo você",
    subtitulo="Identifique-se para prosseguir.",
    action="login",
    submit="Entre",
    alterurl="formulario_cadastro",
    altertit="Cadastro",
    version=__version__,
)
CADASTRO = dict(
    titulo="Cadastrando você",
    subtitulo="Crie sua Identificação para prosseguir.",
    action="cadastro",
    submit="Cadastrar",
    alterurl="/",
    altertit="Entrar",
    version=__version__,
)
ADM_CLASS = dict(aluno=['Aluno'], admin='Aluno Professor, Observador, Localização'.split())

@route('/user_menu')
# @view('index')
@view('corpo/corpo')
def index():
    clazz = request.get_cookie("login", secret='2524')
    if clazz:
        return dict(crud_classes=ADM_CLASS[clazz])
    else:
        redirect('/')


@route('/')
# @view('index')
@view('corpo/login')
def index():
    if request.get_cookie("login", secret='2524'):
        redirect('/user_menu')
    else:
        return LOGIN



@route('/login', method='POST')
def login():
    """
    faz o login na conta do usuário recebendo o usuário e senha
    :return: da acesso ao menu , caso o usuário e senha digitados estejam certos
    """
    nome = request.params['aluno_nome']
    senha = request.params['senha']

    if valida_login(nome, senha):
        nome = 'aluno'
        create_cookie(nome)
        redirect('/user_menu')
    else:
        print("deu ruim no valida login")
        redirect('/')


def valida_login(nome, senha):
    retorno = facade.search_aluno_nome_facade(nome)
    if retorno:
        print("valida_login",retorno['nome'], retorno['senha'] )
        if retorno['nome'] == nome and retorno['senha'] == senha:
            return True
        else:
            return False
    else:
        return False


def create_cookie(parametro):
    response.set_cookie("login", parametro, secret='2524')


facade.create_aluno_facade('egg', matricula='avulsa', escola='avulsa', vinculo_rede='avulsa', senha='spam')
