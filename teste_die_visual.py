#
#
#

import pygal
import time as lib_tm

from teste_die import Die


# Cria um D6
die = Die()

# Parte 1
# Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)

# Parte 2
# Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analisa os resultados
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)


# Com uma lista de frequências, podemos criar um histograma dos
# resultados. Um histograma é um gráfico de barras que mostra a
# frequência da ocorrência de determinados resultados


# Geramos um gráfico de barras criando uma instância de pygal.Bar(), que
# armazenamos em hist u. Então definimos o atributo title de hist (apenas
# uma string que usamos para dar nome ao histograma), usamos os resultados
# possíveis do lançamento de um D6 como rótulos no eixo x v e adicionamos um
# título para cada um dos eixos. Usamos add() para acrescentar uma série de
# valores ao gráfico em w (passando-lhe um rótulo para o conjunto de valores
# a ser adicionado e uma lista dos valores que aparecerão no gráfico). Por
# fim, renderizamos o gráfico em um arquivo SVG, que espera um nome de
# arquivo com a extensão .svg.
# Observe que o Pygal fez o gráfico ser interativo: passe o cursor sobre
# qualquer barra do gráfico e você verá o dado associado a ela. Esse
# recurso é particularmente útil quando plotamos vários conjuntos de
# dados no mesmo gráfico.

# Visualiza os resultados
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6', frequencies)
# hist.render_to_file('die_visual.svg')


# Parte 3
coded_time = str(lib_tm.localtime().tm_hour) + '_' + str(lib_tm.localtime().tm_min) + '_' + str(lib_tm.localtime().tm_sec)
filename = 'die_visual_' + coded_time + '.svg'

hist2 = pygal.Bar()
hist2.title = "Results of rolling one D6 1000 times."
hist2.x_labels = ['1', '2', '3', '4', '5', '6']
hist2.x_title = "Resultado"
hist2.y_title = "Frequência por resultado"
hist2.add('D1', frequencies[0])
hist2.add('D2', frequencies[1])
hist2.add('D3', frequencies[2])
hist2.add('D4', frequencies[3])
hist2.add('D5', frequencies[4])
hist2.add('D6', frequencies[5])
hist2.render_to_file(filename)