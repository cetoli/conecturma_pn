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

  <!-- START NAV -->
  <nav class="navbar is-white">
    <div class="container">
      <div class="navbar-brand">
        <a class="navbar-item brand-text" href="../">
            <figure class="avatar">
              <img src="https://s9.postimg.org/85iwr8l5b/CONECTURMA.png" width="200px">
            </figure>
        </a>
        <div class="navbar-burger burger" data-target="navMenu">
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
      <div id="navMenu" class="navbar-menu">
        <div class="navbar-start">
		  % for item in crud_classes:
          <a class="navbar-item" href="admin.html">
            {{item}}
          </a>
		  % end
          <a class="navbar-item" href="admin.html">
            Quem Somos
          </a>
          <a class="navbar-item" href="admin.html">
            Ajuda
          </a>
        </div>
        <div class="navbar-end">
          <div class="navbar-item has-dropdown">
            <a class="navbar-link">
              Conta
            </a>

            <div class="navbar-dropdown">
              <a class="navbar-item">
                Painel
              </a>
              <a class="navbar-item">
                Perfil
              </a>
              <a class="navbar-item">
                Configurações
              </a>
              <hr class="navbar-divider">
              <div class="navbar-item">
                Sair
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </nav>
  <!-- END NAV -->
  <div class="container">
    <div class="columns">
      <div class="column is-3">
        <aside class="menu">
          <p class="menu-label">
            Painel
          </p>
          <ul class="menu-list">
            <li><a class="is-active">Principal</a></li>
          </ul>
          <p class="menu-label">
            Jogos
          </p>
          <ul class="menu-list">
            <li><a href="#box-two">Favoritos</a></li>
            <li><a href="#box-one">>Descrição</a></li>
          </ul>
          <p class="menu-label">
            Loja
          </p>
          <ul class="menu-list">
            <li><a>Meus Itens</a></li>
            <li><a>Vestuário</a></li>
            <li><a>Itens</a></li>
          </ul>
          <p class="menu-label">
            Conquistas
          </p>
          <ul class="menu-list">
            <li><a>Medalhas</a></li>
            <li><a>Pontuação</a></li>
            <li><a>Jogos</a></li>
            <li><a>Partidas</a></li>
          </ul>
        </aside>
      </div>
      <div class="column is-9 tab-pane">
	<div id="box-one">
        % include('corpo/form.tpl')
	</div>
	<div id="box-two">
        % include('corpo/badges.tpl')
	</div>
      </div>
    </div>
  </div>
  <script async type="text/javascript" src="../js/bulma.js"></script>
</body>
</html>
