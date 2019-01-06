#
#
#

from random import randint


class Die():
    """Uma classe que representa um único dado."""
    
    # O método __init__() aceita um
    # argumento opcional. Com essa classe, quando uma instância de nosso dado for
    # criada, o número de lados sempre será seis se nenhum argumento for
    # incluído. Se um argumento for incluído, esse valor será usado para definir
    # o número de lados do dado u. (Os dados são nomeados de acordo com o seu
    # número de lados: um dado de seis lados é um D6, um dado de oito lados é um
    # D8, e assim por diante.)
    def __init__(self, num_sides=6):
        """Supõe que seja um dado de seis lados."""
        self.num_sides = num_sides

    # O método roll() usa a função randint() para
    # devolver um número aleatório entre 1 e o número de lados v. Essa função
    # pode devolver o valor inicial (1), o valor final (num_sides) ou qualquer
    # inteiro entre eles.
    def roll(self):
        """"Devolve um valor aleatório entre 1 e o número de lados."""
        return randint(1, self.num_sides)