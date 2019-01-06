# Um passeio aleatório (random
# walk) é um caminho que não tem uma direção clara; ele é determinado
# por uma série de decisões aleatórias, em que cada uma é deixada
# totalmente ao acaso. Você pode imaginar um passeio aleatório como o
# caminho que uma formiga faria se tivesse enlouquecido e desse cada
# passo em uma direção aleatória.
# Passeios aleatórios têm aplicações práticas na natureza, em física,
# biologia, química e economia. Por exemplo, um grão de pólen
# flutuando sobre uma gota d’água se move pela superfície porque é
# constantemente empurrada pelas moléculas de água. O movimento
# molecular em uma gota d’água é aleatório, portanto o caminho traçado
# por um grão de pólen na superfície é um passeio aleatório. O código
# que estamos prestes a escrever modela muitas situações do mundo real.

from random import choice


# Para implementar um passeio aleatório, criaremos uma classe RandomWalk,
# que tomará decisões aleatórias sobre a direção que o passeio deve
# seguir. A classe precisa de três atributos: uma variável para armazenar o
# número de pontos do passeio e duas listas para armazenar os valores das
# coordenadas x e y de cada ponto do passeio. Usaremos apenas dois métodos
# na classe RandomWalk: o método
# __init__() e fill_walk(), que calculará os pontos do passeio.
class RandomWalk():
    # Para tomar decisões aleatórias, armazenaremos possíveis opções em
    # uma lista e usaremos choice() para decidir qual opção utilizaremos
    # sempre que uma decisão for tomada u. Então definimos o número
    # default de pontos de um passeio para 5.000 – um valor alto o suficiente
    # para gerar alguns padrões interessantes, mas convenientemente baixo
    # para gerar passeios de modo rápido v. Em seguida, em w, criamos
    # duas listas para armazenar os valores de x e de y e começamos cada
    # passeio no ponto (0, 0).

    """Uma classe para gerar passeios aleatórios."""
    def __init__(self, num_points=5000):
        """Inicializa os atributos de um passeio."""
        self.num_points = num_points
        # Todos os passeios começam em (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    # Usaremos fill_walk(), como mostrado a seguir, para preencher nosso
    # passeio com pontos e determinar a direção de cada passo.
    # A parte principal desse método diz a Python como
    # simular quatro decisões aleatórias: O passeio seguirá para a direita ou
    # para a esquerda? Qual a distância a ser percorrida nessa direção? O
    # passeio seguirá para cima ou para baixo? Qual a distância a ser
    # percorrida nessa direção?
    def fill_walk(self):
        """Calcula todos os pontos do passeio."""
        # Continua dando passos até que o passeio alcance o tamanho desejado u
        while len(self.x_values) < self.num_points:
            # Decide direção a ser seguida e distância a ser percorrida nessa direção
            # Usamos choice([1, -1]) para escolher um valor para x_direction, que
            # devolve 1 para um movimento à direita ou -1 para a esquerda
            x_direction = choice([1, -1])
            # diz a Python qual é a distância a ser percorrida nessa direção
            # inclusão de 0 nos permite dar passos ao longo do
            # eixo y, além dos passos com movimentos ao longo dos dois eixos.
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            # Rejeita movimentos que não vão a lugar nenhum
            if x_step == 0 and y_step == 0:
                continue
            # Calcula os próximos valores de x e de y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)