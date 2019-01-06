#
#
# usar o Pygal para modelar o lançamento de
# dados nos proporciona uma liberdade considerável para explorar esse
# fenômeno. Em apenas alguns minutos, você pode simular um número
# excepcional de lançamentos usando uma grande variedade de dados.

import pygal
import time as lib_tm

from teste_die import Die

# Cria dois dados D6
die_1 = Die()
die_2 = Die(10)

# Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analisa os resultados

coded_time = str(lib_tm.localtime().tm_hour) + '_' + str(lib_tm.localtime().tm_min) + '_' + str(lib_tm.localtime().tm_sec)
filename = 'die_visual_' + coded_time + '.svg'

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza os resultados
hist = pygal.Bar()
hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D10', frequencies)
hist.render_to_file(filename)


# 394