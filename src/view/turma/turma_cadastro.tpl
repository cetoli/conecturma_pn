% include('./header.tpl', title = 'Conecturma')
    <div class="row">
        <div align="center" class="col-md-12">
            <h1>Cadastro de Turmas</h1>
             <form action="/cadastro_turma" method="post">
                 Turma:  <input type="text" name="turma_nome"/>
                 <button type="submit">Enviar</button>
            </form>
            <a href="/turma"><button>Voltar</button></a>
        </div>
    </div>
% include('./footer.tpl')