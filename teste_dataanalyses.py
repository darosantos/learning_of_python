#
#
# A capacidade de analisar esses dados permite descobrir
# padrões e conexões que ninguém mais percebeu.

# Os arquivos CSV podem ser complicados
# para os seres humanos lerem, mas são fáceis para os programas
# processarem e extraírem valores, o que agiliza a operação de análise de
# dados.

# Os arquivos CSV podem ser complicados
# para os seres humanos lerem, mas são fáceis para os programas
# processarem e extraírem valores, o que agiliza a operação de análise de
# dados.

import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Depois de importar o módulo csv, armazenamos
# o nome do arquivo com que estamos trabalhando em filename. Então abrimos o
# arquivo e armazenamos o objeto arquivo resultante em f u. Em seguida,
# chamamos csv.reader() e lhe passamos o objeto arquivo como argumento a fim
# de criar um objeto reader associado a esse arquivo v. Armazenamos o objeto
# reader em reader.
#
# O módulo csv contém uma função next(), que devolve a próxima linha
# do arquivo quando recebe o objeto reader.
#
# reader processa a primeira linha de valores separados por vírgula do
# arquivo e armazena cada um deles como um item em uma lista.
#
# Usamos enumerate() na lista para obter o índice de cada
# item, assim como o valor.

def highs_lows():
    filename = 'sitka_weather_07-2014.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        # print(header_row)
        for index, column_header in enumerate(header_row):
            print(index, column_header)

# Como já lemos a
# linha com o cabeçalho, o laço começará na segunda linha, em que os dados
# propriamente ditos têm início. A cada passagem pelo laço concatenamos os
# dados do índice 1 – a segunda coluna – em highs
#
# Extraímos a temperatura máxima de cada dia e as armazenamos de
# modo organizado em uma lista na forma de strings. Em seguida, converta
# essas strings em números usando int() para que eles possam ser lidos
# pelo matplotlib
#
# Vamos acrescentar um toque
# final no gráfico usando sombreamento para mostrar a variação entre as
# temperaturas mínima e máxima a cada dia. Para isso usaremos o método
# fill_between(), que aceita uma série de valores de x e duas séries de
# valores de y, e preenche o espaço entre as duas séries de valores de y
def highs_lows_temperature():
    # Obtém as datas e as temperaturas máximas e mínimas do arquivo
    filename = 'sitka_weather_2014.csv'
    dates, highs, lows = [], [], []
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            high = str(row[1]).strip()
            high = int(high)
            highs.append(high)
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            dates.append(current_date)
            low = str(row[3]).strip()
            low = int(low)
            lows.append(low)
        print(highs)
    # Faz a plotagem dos dados
    # Plotaremos as temperaturas máximas em vermelho e as mínimas em azul.
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    # passamos para fill_between() a lista dates para os valores de x e
    # então as duas séries com valores de y, highs e lows. O argumento
    # facecolor determina a cor da região sombreada, e lhe fornecemos um
    # valor baixo de alpha, igual a 0,1, para que a região preenchida conecte as
    # duas séries de dados sem provocar distrações na informação que elas
    # representam.
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    # Formata o gráfico
    plt.title("Daily high and low temperatures - 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel("Temperature (F)", fontsize = 12)
    # A chamada a fig.autofmt_xdate() desenha
    # os rótulos com as datas na diagonal para evitar que se sobreponham.
    fig.autofmt_xdate()
    plt.tick_params(axis='both', which='major', labelsize=12)
    plt.show()


def highs_lows_temperature_2():
    # Obtém as datas e as temperaturas máximas e mínimas do arquivo
    filename = 'death_valley_2014.csv'
    dates, highs, lows = [], [], []
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            current_date = ''
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
        print(highs)
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    # Formata o gráfico
    title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
    plt.title(title, fontsize=20)
    plt.title("Daily high and low temperatures - 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel("Temperature (F)", fontsize = 12)
    fig.autofmt_xdate()
    plt.tick_params(axis='both', which='major', labelsize=12)
    plt.show()


highs_lows_temperature_2()