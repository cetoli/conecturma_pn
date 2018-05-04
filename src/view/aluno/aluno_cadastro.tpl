%include('./header.tpl', title="Conecturma")
<div class="row">
    <div align="center" class="col-md-12">
        <h1>Cadastro</h1>
        <form action="/aluno_cadastro" method="post">
             Nome do aluno:   <input type="text" name="aluno_nome"/><br>
             Senha :          <input type="password" name="senha"/><br>
             Escola: <select name="escola">
                % if tipo_observador is '2' or tipo_observador is '3':
                    <option value="{{escolas['id']}}">{{escolas['nome']}}</option>
                % else:
                    % for i in escolas:
                        <option value="{{i['id']}}">{{i['nome']}}</option>
                    % end
                % end
            </select><br>
            <button type="submit">Enviar</button>
        </form>
        <a href="/usuario"><button>Voltar</button></a>
    </div>
</div>
%include('footer.tpl')