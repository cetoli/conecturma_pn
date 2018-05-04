from bottle import route, view, request, redirect, response
from facade.aluno_facade import AlunoFacade

facade = AlunoFacade()

@route('/')
@view('index')
def view_login_index():
    """
    Cria um cookie com base no usuario que loga , sendo diferentes os cookies para o aluno e para os observadores
    :return:
    """
    if request.get_cookie("login", secret='2524'):
        redirect('/jogar_conecturma')
    elif request.get_cookie("login", secret='2525'):
        redirect('/gestao_aprendizagem')
    else:
        return

@route('/sair')
def controller_login_sair():
    """
    Deleta o cookie
    :return:
    """
    response.delete_cookie("login")
    redirect('/')
