from .aluno_facade import AlunoFacade 
from .observador_facade import ObservadorFacade 
# from .escola_facade import EscolaFacade
# from .historico_facade import HistoricoFacade
# from .loja_facade import LojaFacade
# from .turma_facade import TurmaFacade
# from .rede_facade import RedeFacade
# from .medalha_facade import MedalhaFacade


class Facade(AlunoFacade, ObservadorFacade):  # , HistoricoFacade, EscolaFacade, LojaFacade, TurmaFacade, RedeFacade, MedalhaFacade):

    def __init__(self):
        """
        método para utilização do banco de dados
        """

        super(Facade, self).__init__()
        '''
        super(ObservadorFacade, self).__init__()
        super(EscolaFacade , self).__init__()
        super(HistoricoFacade, self).__init__()
        super(LojaFacade, self).__init__()
        super(TurmaFacade, self).__init__()
        super(MedalhaFacade, self).__init__()
        super(RedeFacade, self).__init__()
        '''
