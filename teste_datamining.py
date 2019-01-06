#
#
# A visualização de dados envolve a exploração de dados
# por meio de representações visuais. Ela está intimamente
# relacionada ao data mining (mineração de dados), que
# usa código para explorar padrões e conexões em um
# conjunto de dados. Um conjunto de dados pode ser
# apenas uma pequena lista de números que caiba em uma
# linha de código ou podem ser muitos gigabytes de dados.
# Criar belas representações de dados vai muito além de gerar imagens
# bonitas. Quando você tem uma representação simples e visualmente
# atraente de um conjunto de dados, seu significado se torna evidente a
# quem os vê. As pessoas perceberão padrões e significados em seus
# conjuntos de dados, que elas nem sequer sabiam que existiam.


import matplotlib.pyplot as plt
import time as lib_tm

coded_time = str(lib_tm.localtime().tm_hour) + '_' + str(lib_tm.localtime().tm_min) + '_' + str(lib_tm.localtime().tm_sec)


# O módulo pyplot contém várias funções que ajudam a gerar gráficos e
# plotagens.
# Criamos uma lista para armazenar os quadrados e então a passamos
# para a função plot(), que tentará plotar os números de forma
# significativa. plt.show() abre o visualizador do matplotlib e exibe o
# gráfico,
def mpl_squares():
    squares = [1, 4, 9, 16, 25]
    # Os parâmetros fontsize, que aparecem repetidamente pelo código,
    # controlam o tamanho do texto no gráfico.
    # O parâmetro linewidth controla a espessura da linha gerada por plot()
    plt.plot(squares, linewidth=5)
    # Define o título do gráfico e nomeia os eixos
    plt.title("Square Numbers", fontsize=24)
    # As funções xlabel() e ylabel() permitem definir um título para cada um
    # dos eixos
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    # Define o tamanho dos rótulos das marcações
    # A função tick_params() estiliza as marcações nos eixos
    plt.tick_params(axis='both', labelsize=14)
    plt.show()


# Quando fornecemos uma sequência de números a plot(), ele supõe
# que o primeiro ponto de dado corresponde a um valor de coordenada x
# igual a 0, mas nosso primeiro ponto corresponde a um valor de x igual a
# 1. Podemos sobrescrever o comportamento-padrão fornecendo a plot()
# os valores tanto de entrada quanto de saída usados para calcular os
# quadrados
def mpl_squares_2():
    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    plt.plot(input_values, squares, linewidth=5)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    plt.tick_params(axis='both', labelsize=14)
    plt.show()


# Para plotar um único ponto, utilize a função scatter(). Passe o único
# par (x, y) do ponto em que você estiver interessado para scatter(), e esse
# valor deverá ser plotado
#
def mpl_point_libre():
    input_point = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
    for points in input_point:
        # chamamos scatter() e usamos o argumento s para definir o
        # tamanho dos pontos usados para desenhar o gráfico
        plt.scatter(points[0], points[1], s=200)
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    # Define o tamanho dos rótulos das marcações
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.show()


def mpl_point_libre_2():
    input_point_x = [1, 2, 3, 4, 5]
    input_point_y = [2, 3, 4, 5, 6]
    plt.scatter(input_point_x, input_point_y, s=100)
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    plt.tick_params(axis='both', wh4ich='major', labelsize=14)
    plt.show()


# Como esse é um conjunto bem grande de dados, usamos um tamanho
# menor de ponto e utilizamos a função axis() para especificar o intervalo
# de cada eixo. A função axis() exige quatro valores: os valores mínimo
# e máximo para o eixo x e para o eixo y. Nesse caso, o eixo x varia de 0 a
# 1.100, e o eixo y, de 0 a 1.100.000.
def mpl_plot_range():
    x_values = list(range(1, 1001))
    # uma list comprehension gera os valores de y
    y_values = [x ** 2 for x in x_values]
    plt.scatter(x_values, y_values, s=40)
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    plt.tick_params(axis='both', wh4ich='major', labelsize=14)
    # Define o intervalo para cada eixo
    plt.axis([0, 1100, 0, 1100000])
    plt.show()


# O matplotlib permite colorir os pontos individualmente em um gráfico
# de dispersão. O padrão – pontos azuis com um contorno preto –
# funciona bem para gráficos com poucos pontos. Porém, ao plotar vários
# pontos, os contornos pretos podem se misturar. Para remover os
# contornos dos pontos, passe o argumento edgecolor='none' quando
# chamar scatter()
def mpl_plot_range_2():
    x_values = list(range(1, 1001))
    # uma list comprehension gera os valores de y
    y_values = [x ** 2 for x in x_values]
    plt.scatter(x_values, y_values, edgecolor='none', s=40)
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    plt.tick_params(axis='both', wh4ich='major', labelsize=14)
    # Define o intervalo para cada eixo
    plt.axis([0, 1100, 0, 1100000])
    plt.show()

# Podemos especificar vários argumentos ao usar plot() e utilizar
# diversas funções para personalizar seus gráficos

# Para mudar a cor dos pontos, passe c para scatter()
#  com o nome de uma cor a ser usada
# Você também pode definir cores
# personalizadas usando o modelo de cores RGB. Para definir uma cor,
# passe uma tupla para o argumento c, com três valores decimais (um
# valor para cada cor, isto é, para vermelho, verde e azul), utilizando
# valores entre 0 e 1 - Valores mais próximos de 0 geram cores
# escuras enquanto valores mais próximos de 1 produzem cores mais
# claras.
def mpl_point_color():
    # Plota a primeira série
    input_point_x = [1, 2, 3, 4, 5]
    input_point_y = [2, 3, 4, 5, 6]
    plt.scatter(input_point_x, input_point_y, c='red', edgecolor='none', s=40)
    # Plota a segunda série
    input_point_x = [2, 3, 4, 5, 6]
    input_point_y = [4, 5, 6, 7, 8]
    plt.scatter(input_point_x, input_point_y, c=(0, 0, 0.9), edgecolor='none', s=40)

    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    plt.tick_params(axis='both', wh4ich='major', labelsize=14)
    plt.show()


# Um colormap é uma série de cores em um gradiente que varia de uma cor
# inicial até uma cor final. Os colormaps são usados em visualizações para
# enfatizar um padrão nos dados. Por exemplo, você pode deixar os
# valores menores com uma cor clara e os valores maiores com uma cor
# mais escura. O módulo pyplot inclui um conjunto de colormaps embutidos. Para
# usar um desses colormaps, especifique de que modo o pyplot deve
# atribuir uma cor para cada ponto do conjunto de dados.
# Passamos a lista de valores de y para c e, em seguida, informamos ao
# pyplot qual é o colormap a ser usado por meio do argumento cmap. Esse
# código pinta os pontos com valores menores de y com azul claro e os
# pontos com valores maiores de y com azul escuro
def mpl_colormap():
    x_values = list(range(1001))
    y_values = [x ** 2 for x in x_values]
    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)
    # Define o título do gráfico e nomeia os eixos
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    plt.tick_params(axis='both', wh4ich='major', labelsize=14)
    plt.show()

# Se quiser que seu programa salve automaticamente o gráfico em um
# arquivo, você poderá substituir a chamada a plt.show() por uma
# chamada a plt.savefig(): plt.savefig('squares_plot.png',
# bbox_inches='tight') O primeiro argumento é o nome de um arquivo
# para a imagem do gráfico, que será salvo no mesmo diretório que
# scatter_squares.py. O segundo argumento remove espaços em branco
# extras do gráfico. Se quiser ter espaços em branco extras ao redor do
# gráfico, você poderá omitir esse argumento.
def mpl_colormap_2():
    name_file = 'squares_plot_' + coded_time + '.png'
    print(name_file)

    x_values = list(range(1001))
    y_values = [x ** 2 for x in x_values]
    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    plt.tick_params(axis='both', wh4ich='major', labelsize=14)
    plt.savefig('squares_plot_' + coded_time + '.png', bbox_inches='tight')

# Menu Principal para testar as funções
while True:
    print('Qual algoritmo deseja chamar: ')
    print('1 - Mpl Squares')
    print('2 - Mpl Squares 2')
    print('3 - Mpl Point libre')
    print('4 - Mpl Point libre 2')
    print('5 - Mpl Point Range')
    print('6 - Mpl Point Range 2')
    print('7 - Mpl Color')
    print('8 - Mpl Colormap')
    print('9 - Mpl Colormap 2')
    algoritmo = input('Digite q para sair: ')
    if algoritmo == 'q':
        break
    else:
        algoritmo = int(algoritmo)
        if algoritmo == 1:
            mpl_squares()
        elif algoritmo == 2:
            mpl_squares_2()
        elif algoritmo == 3:
            mpl_point_libre()
        elif algoritmo == 4:
            mpl_point_libre_2()
        elif algoritmo == 5:
            mpl_plot_range()
        elif algoritmo == 6:
            mpl_plot_range_2()
        elif algoritmo == 7:
            mpl_point_color()
        elif algoritmo == 8:
            mpl_colormap()
        elif algoritmo == 9:
            mpl_colormap_2()
        else:
            continue
        break;
