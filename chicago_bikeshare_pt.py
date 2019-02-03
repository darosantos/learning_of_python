# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt
import sys

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

# Vamos mudar o data_list para remover o cabeçalho dele.

data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

##
# Faz uuma cópia da lista e armazena para ser usado posteriormente
# Assim o processo de lidar em cada trecho com os dados fica mais fácil
# Percorre a matriz de dados e substitui as espreções em branco por NULL
range_data_list = data_list[:20]
for index, line_values in enumerate(range_data_list):
    line_values = ['NULL' if len(str(lv)) == 0 else lv for lv in line_values]
    range_data_list[index] = line_values

# Implementação da tarefa 1
for index, line_values in enumerate(range_data_list):
    line_values.insert(0, index)
    message: str = "{0[0]!s} - Start Time: {0[1]!s};\tEnd Time: {0[2]!s};\tTrip Duration: {0[3]!s};\t" \
                   "Start Duration: {0[4]!s};\tEnd Station: {0[5]!s};\tUser Type: {0[6]!s};\t" \
                   "Gender: {0[7]!s};\tBirth Year: {0[8]!s}"
    message = message.format(tuple(line_values))
    print(message)

# sys.exit(0)

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")


# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

gender_list = []
for index, line_values in enumerate(range_data_list):
    gender_list.append(line_values[7])
    print(str(index) + " - " + str(line_values[7]))

# sys.exit(0)

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """
    Função que copia uma coluna de uma matriz
    Argumentos:
        data: a matriz do qual a coluna será extraida
        index: posição da coluna na matriz
    Retorna:
        Uma lista composta pelos valores da referida coluna
    """
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for data_line in data:
        column_list.append(data_line[index])

    return column_list

def column_to_list_method_2(data, index):
    """
        Função que copia uma coluna de uma matriz fazendo uma implementação
            com compresão de listas
        Argumentos:
            data: a matriz do qual a coluna será extraida
            index: posição da coluna na matriz
        Retorna:
            Uma lista composta pelos valores da referida coluna
    """
    column_list = [data_list[index] for data_list in data]
    return column_list

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

#sys.exit(0)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

#sys.exit(0)

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0

for data_line in data_list:
    if data_line[-2] == 'Male':
        male+=1
    else:
        if data_line[-2] == 'Female':
            female+=1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# sys.exit(0)
# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

#sys.exit(0)

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
        Função que conta as ocorrências de gêneros masculino e feminino
        Argumentos:
            data: o dicionário de dados
        Retorna:
            Uma tupla com o quantitativo por genero
    """
    male = 0
    female = 0
    for data_line in data_list:
        if data_line[-2] == 'Male':
            male += 1
        else:
            if data_line[-2] == 'Female':
                female += 1

    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

# sys.exit(0)

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):
    """
        Função que verifica qual o gênero mais popular
        Argumentos:
            data: o dicionário de dados
        Retorna:
            Uma strng indicando o gênero mais popular
    """
    answer = ""
    gender = count_gender(data_list)
    if gender[0] > gender[1]:
        answer = "Male"
    elif gender[0] < gender[1]:
        answer = "Female"
    else:
        answer = "Equal"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# sys.exit(0)

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

# sys.exit(0)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")
def count_type_list(type_list):
    """
        Função que conta quais os tipos presentes em uma lista e seu quantitativo
        Argumentos:
            type_list: ouma lista com os dados para contagem
        Retorna:
            Um dicionário com os dados mapeados, as chaves são os tipos encontrados
            e os valores seu quantitativo de ocorrências
    """
    count_types = {}
    for types in type_list:
        if types in count_types:
            count_types[types] += 1
        else:
            count_types[types] = 1

    return count_types


# Data Manipulation
user_type_list = column_to_list(data_list, -3)
type_for_list_user = count_type_list(user_type_list)
list_label_user_type = [key_type for key_type in type_for_list_user.keys()]
list_value_user_type = [value_type for value_type in type_for_list_user.values()]

# Plot Graph
y_pos = list(range(len(list_label_user_type)))
plt.bar(y_pos, list_value_user_type, color="green", align="center", width=0.7)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Usuário')
plt.xticks(y_pos, list_label_user_type)
plt.title('Quantidade por Tipo de Usuário')
plt.show(block=True)

#sys.exit(0)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque existem registros que o campo Gender é vazio e portanto desprezado para análise"
print("resposta:", answer)

# sys.exit(0)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

# sys.exit(0)

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

def list_to_valueint(data_list):
    """
        Função que verifica converte os valores de uma lista em numeros inteiros
        Argumentos:
            data_list: uma lista com os dados
        Retorna:
            Uma lista com todos os valores em tipo inteiro
    """
    list_of_int = [int(element) for element in data_list]
    return list_of_int

# Acha o minimo
copy_tdl = list_to_valueint(trip_duration_list[:])
min_trip = copy_tdl.pop(0)
for tdl in copy_tdl:
    if min_trip > int(tdl):
        min_trip = tdl
del copy_tdl[:]

# Acha o máximo
copy_tdl = list_to_valueint(trip_duration_list[:])
max_trip = copy_tdl.pop(0)
for tdl in copy_tdl:
    if max_trip < tdl:
        max_trip = tdl
del copy_tdl[:]

# Calcula a média
copy_tdl = list_to_valueint(trip_duration_list[:])
for tdl in copy_tdl:
    mean_trip += float(tdl)
mean_trip = mean_trip / len(copy_tdl)
del copy_tdl[:]

# Calcula a mediana
copy_tdl = list_to_valueint(trip_duration_list[:])
copy_tdl.sort()
length_tdl = len(copy_tdl)
if length_tdl % 2 == 0:
    mean_one = length_tdl / 2
    mean_two = mean_one + 1
    median_trip = (copy_tdl[mean_one] + copy_tdl[mean_two]) / 2.0
else:
    mean_pos = int(length_tdl / 2) + 1
    median_trip = copy_tdl[mean_pos]
del copy_tdl[:]

#sys.exit(0)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

# sys.exit(0)

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations_list = column_to_list(data_list, 3)
start_stations = set(start_stations_list )

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

# sys.exit(0)

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
# """
# Função de exemplo com anotações.
# Argumentos:
# param1: O primeiro parâmetro.
# param2: O segundo parâmetro.
# Retorna:
# Uma lista de valores x.
# """

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    item_types = []
    count_items = []

    count_type = count_type_list(column_list)
    item_types = count_type.keys()
    count_items = count_type.values()

    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
