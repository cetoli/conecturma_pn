<%
    for i in usuarios:
%>
    <div class="row">
        <div class="col-md-2">
            {{i['nome']}}
        </div>
        <div class="col-md-2">
            {{i['cpf']}}
        </div>
        <div class="col-md-2">
            {{i['vinculo_escola']}}
        </div>
        <div class="col-md-2">
            {{i['vinculo_rede']}}
        </div>
        <div class="col-md-2">
            {{i['tipo']}}
        </div>
    </div>
<%
    end
%>