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
</head>
<body>
<!-- Nav tabs -->
<input type="radio" id="ajuda" name="nav-tab" style="display: none;" >
<input type="radio" id="quem_somos" name="nav-tab" style="display: none;" >
<input type="radio" id="doc" name="nav-tab" style="display: none;" >
% for item in range(9):
<input type="radio" id="{{'vnav-{}'.format(item)}}" name="nav-tab" style="display: none;" >
% end
% for item in crud_classes:
<input type="radio" id="{{'menu-item{}'.format(item)}}" name="nav-tab" style="display: none;" >
% end

  <!-- START NAV -->
  <nav class="navbar is-white">
    <div class="container">
      <div class="navbar-brand">
        <a class="navbar-item brand-text" href="../">
            <figure class="avatar">
              <img src="https://i.imgur.com/UDSgtyS.jpg" width="200px">
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
              <label for="{{item.lower()}}">
                  <a class="navbar-item">

                    {{item}}
                  </a></label>
		  % end
          <label for="quem_somos">
              <a class="navbar-item">

                Quem Somos
              </a></label>
          <label for="ajuda">
              <a class="navbar-item">

                Ajuda
              </a></label>
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
      <div class="column is-3 tab-content">
          <div class="tab-pane content-ajuda">
                % include('corpo/aluno_menu.tpl')
          </div>
          <div class="tab-pane content-quem_somos">
                % include('corpo/quem_menu.tpl')
          </div>
          <div  class="tab-pane content-aluno">
                % include('corpo/aluno_menu.tpl')
          </div>
      </div>
      <div class="column is-9 tab-content">
        <div id="box-one" class="tab-pane content-ajuda">
            % include('corpo/form.tpl')
	    </div>
        <div id="box-two" class="tab-pane content-aluno">
            % include('corpo/badges.tpl')
	    </div>
        <div id="box-three" class="tab-pane content-quem_somos">
            % include('corpo/quem.tpl')
	    </div>
      </div>
    </div>
  </div>
  <script async type="text/javascript" src="../js/bulma.js"></script>
</body>
</html>
