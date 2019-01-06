# Testa os passos aleatórios

import matplotlib.pyplot as plt

from teste_randomwalk import RandomWalk


#  Além de colorir os pontos para mostrar as suas posições no decorrer do
# passeio, seria interessante ver em que lugar cada passeio começa e
# termina. Para isso, podemos plotar o primeiro e o último ponto
# individualmente depois que a série principal for plotada. Deixaremos os
# pontos de início e de fim maiores e usaremos cores diferentes para
# destacá-los

while True:
    # Cria um passeio aleatório e plota os pontos
    rw = RandomWalk()
    rw.fill_walk()
    # Usamos range() para gerar uma lista de números igual ao
    # número de pontos do passeio Então armazenamos esses números na
    # lista point_numbers, que usaremos para definir a cor de cada ponto do
    # passeio
    point_numbers = list(range(rw.num_points))
    # Passamos point_numbers para o argumento c, usamos o colormap
    # Blues e passamos edgecolor=none para eliminar o contorno preto de cada
    # ponto.
    plt.scatter(rw.x_values,
                rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break