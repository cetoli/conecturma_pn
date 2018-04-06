<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Conecturma - Plataforma Educacional - Login</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" integrity="sha256-eZrrJcwDc/3uDhsdt61sL2oOBY362qM3lon1gyExkL0=" crossorigin="anonymous" />
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,700" rel="stylesheet">
  <!-- Bulma Version 0.6.0 -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.6.0/css/bulma.min.css" integrity="sha256-HEtF7HLJZSC3Le1HcsWbz1hDYFPZCqDhZa9QsCgVUdw=" crossorigin="anonymous" />
  <link rel="stylesheet" type="text/css" href="static/corpo.css">
</head>
<body>
  <section class="hero is-success is-fullheight">
    <div class="hero-body">
      <div class="container has-text-centered">
        <div class="column is-4 is-offset-4">
          <h3 class="title has-text-grey">{{titulo}}</h3>
          <p class="subtitle has-text-grey">{{subtitulo}}</p>
          <div class="box">
            <figure class="avatar">
              <img src="https://i.imgur.com/GgLXdfE.jpg" width="200px">
            </figure>
            <form action="{{action}}" method='POST'>
              <div class="field">
                <div class="control">
                  <input class="input is-large" type="text" placeholder="Sua Identificação" autofocus="" name="aluno_nome">
                </div>
              </div>

              <div class="field">
                <div class="control">
                  <input class="input is-large" type="password" placeholder="Sua Senha" name="senha">
                </div>
              </div>
              <div class="field">
                <label class="checkbox">
                  <input type="checkbox">
                  Lembre minha identidade
                </label>
              </div>
              <button class="button is-block is-info is-large is-fullwidth">{{submit}}</button>
            </form>
          </div>
          <p class="has-text-grey">
            <a href="{{alterurl}}">{{altertit}}</a> &nbsp;·&nbsp;
            <a href="../">Esqueci a Senha</a> &nbsp;·&nbsp;
            <a href="../">Precisa de Ajuda?</a>
          </p>
          <p class="has-text-grey">
            versão {{version}}
          </p>
        </div>
      </div>
    </div>
  </section>
  <script async type="text/javascript" src="../js/bulma.js"></script>
</body>
</html>
