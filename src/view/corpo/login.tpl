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
          Conecturma
        </a>
        <div class="navbar-burger burger" data-target="navMenu">
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
      <div id="navMenu" class="navbar-menu">
        <div class="navbar-start">
          <a class="navbar-item" href="admin.html">
            Login
          </a>
          <a class="navbar-item" href="admin.html">
            Quem Somos
          </a>
          <a class="navbar-item" href="admin.html">
            Ajuda
          </a>
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
            Identificação
          </p>
          <ul class="menu-list">
            <li><a class="is-active">Login</a></li>
            <li><a>Cadastro</a></li>
          </ul>
        </aside>
      </div>
      <div class="column is-9">
        <section class="hero is-info welcome is-small">
          <div class="hero-body">
            <div class="container">
              <h1 class="title">
                Olá, amigo da Conecturma!
              </h1>
              <h2 class="subtitle">
                Desejamos que você esteja tendo um ótimo dia!
              </h2>
            </div>
          </div>
        </section>
        <div class="columns">
          <div class="column is-6">
            <div class="card">
              <header class="card-header">
                <p class="card-header-title">
                  Identificação
                </p>
              </header>
              <div class="card">
                <div class="content">
                  <div class="field">
                    <label class="label">Usuário</label>
                    <div class="control has-icons-left has-icons-right">
                      <input class="input" type="text" placeholder="Identificador do usuário"/>
                      <span class="icon is-small is-left">
                        <i class="fa fa-user"></i>
                      </span>
                      <span class="icon is-small is-right">
                        <i class="fa fa-check"></i>
                      </span>
                    </div>
                  </div>

                  <div class="field">
                    <label class="label">Senha</label>
                    <div class="control has-icons-left has-icons-right">
                      <input class="input" type="password" placeholder="Text input" value="entre a senha">
                      <span class="icon is-small is-left">
                        <i class="fa fa-user"></i>
                      </span>
                      <span class="icon is-small is-right">
                        <i class="fa fa-check"></i>
                      </span>
                    </div>
                    <p class="help is-success"></p>
                  </div>
                </div>
              </div>
              <footer class="card-footer">
                <a class="button is-large is-primary is-pulled-right" href="#">Enviar</a>
              </footer>
            </div>
          </div>
          <div class="column is-6">
            <div class="card">
              <header class="card-header">
                <p class="card-header-title">
                  Busca de Escolas
                </p>
                <a href="#" class="card-header-icon" aria-label="more options">
                  <span class="icon">
                    <i class="fa fa-angle-down" aria-hidden="true"></i>
                  </span>
                </a>
              </header>
              <div class="card-content">
                <div class="content">
                  <div class="control has-icons-left has-icons-right">
                    <input class="input is-large" type="text" placeholder="">
                    <span class="icon is-medium is-left">
                      <i class="fa fa-search"></i>
                    </span>
                    <span class="icon is-medium is-right">
                      <i class="fa fa-check"></i>
                    </span>
                  </div>
                </div>
              </div>
            </div>
            <div class="card">
              <header class="card-header">
                <p class="card-header-title">
                  Busca de Alunos
                </p>
                <a href="#" class="card-header-icon" aria-label="more options">
                  <span class="icon">
                    <i class="fa fa-angle-down" aria-hidden="true"></i>
                  </span>
                </a>
              </header>
              <div class="card-content">
                <div class="content">
                  <div class="control has-icons-left has-icons-right">
                    <input class="input is-large" type="text" placeholder="">
                    <span class="icon is-medium is-left">
                      <i class="fa fa-search"></i>
                    </span>
                    <span class="icon is-medium is-right">
                      <i class="fa fa-check"></i>
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <script async type="text/javascript" src="../js/bulma.js"></script>
</body>
</html>
