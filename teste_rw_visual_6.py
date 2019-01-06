# Testa os passos aleatórios

import matplotlib.pyplot as plt

from teste_randomwalk import RandomWalk


while True:
    # Cria um passeio aleatório e plota os pontos
    rw = RandomWalk(50000)
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
                rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    # Enfatiza o primeiro e o último ponto
    plt.scatter(0, 0, c='green', edgecolors = 'none', s = 100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 100)
    # Remove os eixos
    # Para modificar os eixos, use a função plt.axes() u para definir a
    # visibilidade de cada um deles com False. À medida que continuar a
    # trabalhar com visualizações, você verá essa cadeia de métodos com
    # frequência.
    plt.axes().get_yaxis().set_visible(False)
    # Define o tamanho da janela de plotagem
    plt.figure(figsize=(10, 6))
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break