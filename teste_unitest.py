# O módulo unittest da biblioteca-padrão de Python oferece as
# ferramentas para testar seu código. Um teste de unidade verifica se um
# aspecto específico do comportamento de uma função está correto. Um
# caso de teste é uma coleção de testes de unidade que, em conjunto, prova
# que uma função se comporta como deveria em todas as situações que
# você espera que ela trate. Um bom caso de teste considera todos os
# tipos possíveis de entradas que uma função poderia receber e inclui
# testes para representar cada uma dessas situações. Um caso de teste com
# cobertura completa é composto de uma variedade de testes de unidade
# que inclui todas as possíveis maneiras de usar uma função. Atingir a
# cobertura completa em um projeto de grande porte pode ser
# desanimador. Em geral, é suficiente escrever testes para os
# comportamentos críticos de seu código e então visar a uma cobertura
# completa somente se o projeto começar a ter uso disseminado.

# Para escrever um caso de teste para uma função,
# importe o módulo unittest e a função que você quer testar. Em seguida
# crie uma classe que herde de unittest.TestCase e escreva uma série de
# métodos para testar diferentes aspectos do comportamento de sua
# função.

# Qualquer método
# que comece com test_ será executado de modo automático


import unittest


from name_function import get_formatted_name, get_formatted_name2


class NamesTestCase(unittest.TestCase):
    # """Testes para 'name_function.py'."""
    def test_first_last_name(self):
        """Nomes como 'Janis Joplin' funcionam?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        """Nomes como 'Janis Joplin' funcionam?"""
        formatted_name = get_formatted_name2('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Nomes como 'Wolfgang Amadeus Mozart' funcionam?"""
        formatted_name = get_formatted_name2('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


unittest.main()
unittest.TestLoader


# Em 37 usamos um dos recursos mais úteis de unittest: um método de
# asserção. Os métodos de asserção verificam se um resultado recebido é
# igual ao resultado que você esperava receber.

# A linha unittest.main() diz a Python para executar os testes desse
# arquivo.


#  Python disponibiliza vários métodos de asserção na classe
# unittest.TestCase. Com esses métodos, podemos verificar se os valores devolvidos são ou
# não são iguais aos valores esperados, se os valores são True ou False e se
# os valores estão (in) ou não estão (not in) em uma dada lista. Você pode
# usar esses métodos somente em uma classe que herde de
# unittest.TestCase

# assertEqual(a, b) Verifica se a == b
# assertNotEqual(a, b) Verifica se a != b
# assertTrue(x) Verifica se x é True
# assertFalse(x) Verifica se x é False
# assertIn(item, lista) Verifica se item está em lista
# assertNotIn(item, lista) Verifica se item não está em lista
