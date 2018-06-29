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
"""

Painel

    Principal

Jogos

    Favoritos
    Descrição

Loja

    Meus Itens
    Vestuário
    Itens

Conquistas

    Medalhas,Pontuação,Jogos,Partidas

"""
COMMON_TABS='Painel,Quem Somos,Ajuda'.split(',')
FRONTEND = dict(
    Aluno=dict(
        tabs=COMMON_TABS,
        side=dict(
            Informação='Principal',
            Jogos="Favoritos,Descrição".split(','),
            Lojas="Meus Itens,Vestuário,Itens".split(','),
            Conquistas="Medalhas,Pontuação,Jogos,Partidas".split(','),

        )
    )
)

class TabbedPane:
    def __init__(self, tabs="Principal,Quem Somos,Ajuda".split(",")):
        class Tab:
            def __init__(self, title, sider):
                class MenuHead:
                    def __init__(self, title):
                        self.title = title

                        class MenuItem:
                            def __init__(self, title):
                                self.title = title
                                pass
                        self.sider = [MenuItem(items) for items in sider.items()]

                self.title = title
                self.sider = [MenuHead(head, items) for head, items in sider.items()]
