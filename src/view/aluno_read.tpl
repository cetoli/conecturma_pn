<!doctype html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    <title>Conecturma</title>
    <style>
        .id{
            text-align:center;
            float:left;
        }
        .nome{
            text-align:center;
            margin-left:10px;
            float:left;
        }
    </style>
</head>
<body>
    <h1>Ver Alunos</h1>
    <div class="id">
        <h4>ID</h4>
        % for id in aluno_id:
            {{id}}
            <br>
        % end
    </div>
    <div class="nome">
        <h4>Turma nome</h4>
        % for nome in serie:
            {{nome}}
            <br>
        % end
    </div>
    <br>
    <br>
    <br>
    <br>

    <a href="/"><button>Voltar</button></a>
</body>
</html>