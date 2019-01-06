# Durante a execução de um caso de teste, Python exibe um caractere
# para cada teste de unidade à medida que ele terminar. Um teste que
# passar exibe um ponto, um teste que resulte em erro exibe um E e um
# teste que resultar em uma asserção com falha exibe um F. É por isso que
# você verá um número diferente de pontos e de caracteres na primeira
# linha da saída quando executar seus casos de teste. Se um caso de teste
# demorar muito para executar por conter muitos testes de unidade, você
# poderá observar esses resultados para ter uma noção de quantos testes
# estão passando
#
#


import unittest

from survey import AnonymousSurvey


# Quando um método setUp() é incluído em uma classe TestCase, Python executa
# esse método antes de qualquer método cujo nome comece com test_.
# Qualquer objeto criado no método setUp() estará disponível a todos os
# métodos de teste que você escrever.


class TestAnonmyousSurvey(unittest.TestCase):
    # """Testes para a classe AnonymousSurvey"""

    def setUp(self):
        # """ Cria uma pesquisa e um conjunto de respostas que
        # poderão ser usados em todos os métodos de teste. """

        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        # """Testa se uma única resposta é armazenada de forma apropriada."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        # """Testa se três respostas individuais são armazenadas de forma apropriada."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()