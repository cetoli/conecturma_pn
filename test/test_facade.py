# coding: utf-8
import unittest

# from unittest.mock import MagicMock
# from src.model.estrutura_model import DbEstrutura
"""possivel erro de importaçao de DbAluno acima"""
from src.facade.aluno_facade import AlunoFacade
from src.facade.observador_facade import ObservadorFacade
from src.facade.rede_facade import RedeFacade
from src.facade.escola_facade import EscolaFacade
from src.facade.turma_facade import TurmaFacade
from src.facade.loja_facade import LojaFacade
from src.facade.medalha_facade import MedalhaFacade
from src.facade.historico_facade import HistoricoFacade
from src.facade.Facade_main import Facade


class FacadeTest(unittest.TestCase):
    def setUp(self):
        self.facade = Facade()

    """TESTE USUARIO/ALUNO"""

    def _create_aluno(self):

        aluno1 = self.facade.create_aluno_facade("egg", "Escola Conecturma", "123")
        self.assertEqual(aluno1, True)

    def _create_aluno_senha_vazia(self):
        aluno = self.facade.create_aluno_facade("Brian", "")
        self.assertTrue(aluno, TypeError)

    def _create_aluno_aluno_vazio(self):
        aluno = self.facade.create_aluno_facade(" ", " 123")
        self.asserrTrue(TypeError, True)

    def _create_aluno_fail(self):
        aluno = self.facade.create_aluno_facade("Brian", "123")
        self.assertEqual(aluno, TypeError)

        aluno = self.facade.create_aluno_facade("egg", "")
        self.assertEqual(aluno, True)

    def _pesquisa_aluno(self):
        aluno = self.facade.pesquisa_aluno_facade("Brian")
        self.assertIs(aluno, aluno)
        aluno = self.facade.pesquisa_aluno_facade("Sily walk")
        self.assertIs(aluno, None)

    def _pontos_jogo(self):
        aluno = self.facade.ponto_jogo_facade("Brian", "j1", 1)
        self.assertIs(aluno, True)
        aluno = self.facade.ponto_jogo_facade("Brian", "j1", None)
        self.assertIs(aluno, False)

    def _delete_alunos(self):
        alunos = self.facade.read_aluno_facade()
        escolhidos = []
        for alunos in alunos:
            escolhidos.append(alunos['id'])
        self.facade.delete_aluno_facade(escolhidos)

    def _update_aluno(self):
        self._create_aluno()
        aluno1 = self.facade.pesquisa_aluno_facade("egg")
        x = aluno1.id
        self.facade.update_aluno_facade(aluno1.id, "knight", "321")
        aluno2 = self.facade.pesquisa_aluno_facade("knight")
        y = aluno2.id
        self.assertEqual(x, y)
        self._delete_alunos()

    def _read_aluno(self):
        self._create_aluno()
        aluno4 = self.facade.pesquisa_aluno_facade("egg")
        self.assertIn(aluno4.id, self.facade.read_aluno_facade()[-1].values())
        # self.assertIn(aluno4.id,self.facade.read_aluno_facade()[0].values())

    def _anotacoes_no_aluno(self):
        self._create_aluno()
        mensagem = "Isto é uma mensagem de teste"
        aluno1 = self.facade.pesquisa_aluno_facade("egg")
        self.facade.anotacoes_aluno_facade(aluno1.id, mensagem)
        self.assertEqual(aluno1.anotacoes_aluno[0], mensagem.encode('utf-8'))

    def _read_anotaçoes_no_aluno(self):
        self._anotacoes_no_aluno()
        aluno1 = self.facade.pesquisa_aluno_facade("egg")
        read = self.facade.read_anotacoes_aluno_facade(aluno1.id)
        self.assertIn("Isto é uma mensagem de teste", read)
        self._delete_alunos()

    def _aluno_in_turma(self):
        self._create_turma()
        self._create_aluno()
        aluno1 = self.facade.pesquisa_aluno_facade("egg")
        self.facade.create_aluno_facade("Ni", "123", "Escola Conecturma")
        aluno2 = self.facade.pesquisa_aluno_facade("Ni")
        escolhidos = [aluno1, aluno2]
        # print("escolhidos",escolhidos)
        turma1 = self.facade.search_turma_facade("Knight")
        # print("turma1,func",turma1)
        self.facade.aluno_in_turma_facade(escolhidos, turma1)
        aluntest = self.facade.pesquisa_aluno_facade("egg")
        aluntest2 = self.facade.pesquisa_aluno_facade('Ni')
        # print("aluntest",aluntest.vinculo_turma)
        self.assertEqual(aluntest.turma_do_aluno, turma1['nome'])
        self.assertEqual(aluntest2.turma_do_aluno, turma1['nome'])

    def _comprar_item(self):
        self._create_item()
        self._create_aluno()
        aluno1 = self.facade.pesquisa_aluno_facade("egg")
        item1 = self.facade.pesquisa_item_facade_nome("burroquandofoge")
        self.facade.compra_item_facade(aluno1.id, item1['id'])
        self.assertIn(str(item1['id']), aluno1.itens_comprados[-1].decode('utf-8'))

    def _ver_iten_comprado(self):
        self._comprar_item()
        aluno1 = self.facade.pesquisa_aluno_facade("egg")
        iten = self.facade.ver_item_comprado_facade(aluno1.id)
        self.assertEqual([int(aluno1.itens_comprados[0].decode('utf-8'))], iten)


    def _equipar_item_facade(self):
        self._comprar_item()
        aluno1 = self.facade.pesquisa_aluno_facade("egg")
        iten = self.facade.pesquisa_item_facade_nome("burroquandofoge")
        self.facade.equipar_item_facade(aluno1.id, iten)
        aluno2 = self.facade.pesquisa_aluno_facade("egg")
        self.assertEqual(aluno2.cor, iten['id'])

    def _mostrar_avatar(self):
        self._equipar_item_facade()
        aluno1 = self.facade.pesquisa_aluno_facade("egg")
        self.facade.avatar_facade(aluno1.id)
        iten1=self.facade.pesquisa_item_facade_nome("burroquandofoge")
        self.assertEqual(self.facade.avatar_facade(aluno1.id)['cor'], iten1['id'])
        self._delete_item()
        self._delete_alunos()

    def test_update_aluno(self):
        self._update_aluno()

    def test_read_aluno(self):
        self._read_aluno()
        self._delete_alunos()

    def test_delete_aluno(self):
        self._create_aluno()
        self._delete_alunos()

    def test_anotacoes_no_aluno(self):
        self._create_aluno()
        self._anotacoes_no_aluno()

    def test_read_anotacoes_aluno(self):
        self._read_anotaçoes_no_aluno()

    def test_aluno_in_turma(self):
        self._aluno_in_turma()

    def test_compra_item(self):
        self._comprar_item()
        self._delete_item()

    def test_ver_itens_comprados(self):
        self._ver_iten_comprado()

    def test_equipar_item(self):
        self._equipar_item_facade()

    def test_ver_avatar(self):
        self._mostrar_avatar()

    def test_create_delete_aluno(self):
        self._create_aluno()
        self._delete_alunos()

    def _test_create_aluno_senha_vazia(self):
        self._create_aluno_senha_vazia()

    @unittest.expectedFailure
    def test_all_aluno(self):
        self._create_aluno_fail()
        self._update_aluno()
        self._pesquisa_aluno()
        self._pontos_jogo()
        self._create_aluno_aluno_vazio()
        self._delete_alunos()

    def _test_create_aluno_fail(self):
        self._create_aluno_fail()

    def _test_create_update_aluno(self):
        self._update_aluno()

    def _test_pesquisa_aluno(self):
        self._pesquisa_aluno()

    def _test_pontos_jogo(self):
        self._pontos_jogo()

    def _test_delete_alunos(self):

        self._delete_alunos()

    def _test_all_aluno(self):
        self._create_aluno_fail()
        self._update_aluno()
        self._pesquisa_aluno()
        self._pontos_jogo()
        self._delete_alunos()

    """FIM TESTE USUARIO/ALUNO"""

    """INICIO TESTE OBSERVADOR"""

    def _create_observador(self):
        observador1 = self.facade.create_observador_facade(nome='Egg', senha='span', telefone='(21)9999-9999',
                                                           cpf='123456789', email='egg@span.com.br', rede=0, escola=0,
                                                           tipo='ADMINISTRADOR')

        observador_professor = self.facade.create_observador_facade(nome='Monty', senha='python',
                                                                    telefone='(21)9999-9999',
                                                                    cpf='123456789', email='Monty@python.com.br',
                                                                    tipo='3', rede=0, escola=0)

        self.assertIs(observador1, True)
        self.assertIs(observador_professor, True)

    def _update_observador(self):
        observador1 = self.facade.search_observador_facade('Egg')
        observador_update = self.facade.update_observador_facade(id=observador1['id'], nome='Knight',
                                                                 telefone='(11)8888-8888', cpf='999999999',
                                                                 email='knight@ni.com')
        observador2 = self.facade.search_observador_facade('Knight')
        self.assertEqual(observador2['nome'], 'Knight')
        self.assertEqual(observador2['telefone'], '(11)8888-8888')
        self.assertEqual(observador2['cpf'], '999999999')
        self.assertEqual(observador2['email'], 'knight@ni.com')

    def _search_observador(self):
        observador1 = self.facade.search_observador_facade('Egg')
        self.assertEqual(observador1['nome'], 'Egg')
        self.assertEqual(observador1['senha'], 'span')
        self.assertEqual(observador1['telefone'], '(21)9999-9999')
        self.assertEqual(observador1['cpf'], '123456789')
        self.assertEqual(observador1['email'], 'egg@span.com.br')
        self.assertEqual(observador1['tipo'], 'ADMINISTRADOR')
        observador2 = self.facade.search_observador_facade('Ni')
        self.assertIs(observador2, None)

    def _delete_observador(self):
        observador1 = self.facade.read_observador_facade()
        escolhidos = []
        for observados in observador1:
            escolhidos.append(observados['id'])
        self.facade.delete_observador_facade(escolhidos)

    def test_create_delete_observador(self):
        self._create_observador()
        self._delete_observador()

    def test_create_search_delete_observador(self):
        self._create_observador()
        self._search_observador()
        self._delete_observador()

    def test_create_update_delete_observador(self):
        self._create_observador()
        self._update_observador()
        self._delete_observador()

    """FIM TESTE OBSERVADOR"""



    """TESTE REDE"""

    def _create_rede(self):
        rede = self.facade.create_rede_facade("egg", "(21)9999-9999")
        rede2 = self.facade.search_rede_facade("egg")
        self.assertIsNot(rede, None)
        self.assertIsNot(rede2, None)

    def _update_rede(self):
        rede = self.facade.create_rede_facade("egg", "(21)9999-9999")
        rede = self.facade.search_rede_facade("egg")
        self.facade.update_rede_facade(rede['id'], nome="Ni", telefone="(11)8888-8888")
        rede = self.facade.search_rede_facade("Ni")
        self.assertEqual(rede['nome'], "Ni")
        self.assertEqual(rede['telefone'], "(11)8888-8888")

    def _pesquisa_rede(self):
        rede = self.facade.search_rede_facade("Ni")
        self.assertIs(rede, rede)
        rede = self.facade.search_rede_facade("Sily walk")
        self.assertIs(rede, None)

    def _delete_rede(self):
        rede = self.facade.read_rede_facade()
        escolhidos = []
        for redes in rede:
            escolhidos.append(redes['id'])
        self.facade.delete_rede_facade(escolhidos)

    def test_create_rede(self):
        self._create_rede()

    def test_update_rede(self):
        self._update_rede()

    def test_pesquisa_rede(self):
        self._pesquisa_rede()

    def test_delete_rede(self):
        self._update_rede()
        self._delete_rede()

    """FIM TESTE REDE"""

    """TESTE FACADE ESCOLA"""

    def _create_escola(self):
        escola = self.facade.create_escola_facade('Do bairro', 'de baixo', '2266 6622', '21 ', 'RJ', 'Pindamonhagaba',
                                                  'cep 22287111')
        self.assertIsNot(escola, None)

    def _update_escola(self):
        escola = self.facade.search_escola_facade("Do bairro")
        self.facade.update_escola_facade(escola['id'], nome="Ni", telefone="33355567", vinculo_rede="abelhinha",
                                         cep="22270 999", endereco="rua do teste ",numero='666', cidade="RIO DE JANEIRO",
                                         estado='RJ')
        escola2 = self.facade.search_escola_facade("Ni")
        self.assertEqual(escola2['nome'], "Ni")
        self.assertEqual(escola2['endereco'], "rua do teste ")
        self.assertEqual(escola2['numero'], '666')
        self.assertEqual(escola2['vinculo_rede'], "abelhinha")
        self.assertEqual(escola2['telefone'], "33355567")


    def _pesquisa_escola(self):
        escola = self.facade.search_escola_facade("Do bairro")
        self.assertIs(escola, escola)
        escola = self.facade.search_escola_facade("Sily walk")
        self.assertIs(escola, None)

    def _delete_escola(self):
        escola = self.facade.read_escola_facade()
        escolhidos = []
        for escola in escola:
            escolhidos.append(escola['id'])
        self.facade.delete_escola_facade(escolhidos)

    def test_create_delete_escola(self):
        self._create_escola()
        self._delete_escola()

    def test_pesquisa_escola(self):
        self._pesquisa_escola()
        self._delete_escola()

    def test_update_escola(self):
        self._create_escola()
        self._update_escola()
        self._delete_escola()

    def test_pesquisa_escola(self):
        self._pesquisa_escola()

    def test_delete_escola(self):
        self._update_rede()
        self._delete_rede()

    """FIM TESTE ESCOLA"""
    """TESTE TURMA"""

    def _create_turma(self):
        turma1 = self.facade.create_turma_facade(nome="Knight", login="Ni", serie=1, escola="1")
        # print("turma1",turma1)
        self.assertIsNot(turma1, None)

    def _search_turma(self):
        turma1 = self.facade.search_turma_facade("Knight")
        self.assertIn(turma1['nome'], "Knight")
        self.assertIn(turma1['criador'], "Ni")

    def _vincular_professor_turma(self):
        turma = self.facade.search_turma_facade("Knight")
        professor = self.facade.search_observador_facade("Monty")
        self.facade.vincular_professor_turma_facade(turma['id'], professor['id'])

    def _ver_professor_turma(self):
        turma = self.turma.search_turma_facade("Knight")
        professor_vinculado = self.turma.ver_professor_turma_facade(turma['id'])
        for p in professor_vinculado:
            prof = p
        professor = self.turma.search_observador_id_facade(prof)

        self.assertEqual(professor.nome, 'Monty')
        self.assertEqual(professor.email, 'Monty@python.com.br')

    def _delete_turma(self):
        turmas = self.facade.read_turma_facade()
        escolhidos = []
        for turmas in turmas:
            escolhidos.append(turmas['id'])
        self.facade.delete_turma_facade_test(escolhidos)

    def test_create_delete_turma(self):
        self._create_turma()
        self._delete_turma()

    def _test_vincular_professor_turma(self):
        self._create_turma()
        self._create_observador()
        self._vincular_professor_turma()
        self._ver_professor_turma()
        self._delete_observador()
        self._delete_turma()

    def test_create_search_delete_turma(self):
        self._create_turma()
        self._search_turma()
        # self._delete_turma()

    """FIM TESTE TURMA """

    """TESTE FACADE HISTORICO"""

    def _create_historico(self):
        self.facade.create_historico_facade("Egg", "ADMINISTRADOR")

    def _read_historico(self):
        historico = self.facade.read_historico_facade()
        self.assertIsNot(historico, [])

    def test_create_historico(self):
        self._create_aluno()

    def test_read_historico(self):
        self._read_historico()

    """FIM TESTE FACADE HISTORICO"""

    """TESTE FACADE MEDALHAS"""

    def _create_medalha(self):
        medalha = self.facade.create_medalha_facade('cheese',tipo="1")
        print("medalha",medalha)
        self.assertIsNot(medalha, None)

    def _read_medalha(self):
        medalha =self.facade.read_medalha_facade()
        medalha1=self.facade.pesquisa_medalha_facade('cheese')
        self.assertIn(medalha1['id'],medalha[-1].values())

    def _delete_medalha(self):
        medalhas = self.facade.read_medalha_facade()
        escolhidos = []
        for medalhas in medalhas:
            escolhidos.append(medalhas['id'])
        self.facade.delete_medalha_facade(escolhidos)

    def test_create_delete_medalha(self):
        self._create_medalha()
        self._delete_medalha()

    def test_read_medalha(self):
        self._create_medalha()
        self._read_medalha()
        self._delete_medalha()



    """FIM DE TESTE FACADE MEDALHAS"""

    """INICIO DE TESTE FACADE DE LOJA"""

    def _create_item(self):
        iten1 = self.facade.criar_item_loja_facade(nome="burroquandofoge", tipo='1', preco=0)
        self.assertIsNot(iten1, None)

    def _read_item(self):
        self._create_item()
        item1 = self.facade.read_item_loja_facade()

    def _delete_item(self):
        itens = self.facade.read_item_loja_facade()
        escolhidos = []
        for itens in itens:
            escolhidos.append(itens['id'])
        self.facade.deletar_item(escolhidos)

    def test_create_delete_iten(self):
        self._create_item()
        self._delete_item()

    def test_read_item(self):
        self._read_item()

if __name__ == '__main__':
    unittest.main()