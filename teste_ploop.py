# Loops For
# O Python tem dois tipos de loops - loops for e loops while. Um loop for é 
# utilizado para iterar um iterável.
# Um iterável é um objeto que pode retornar um de seus elementos de cada vez. 
# Isso pode incluir tipos de sequência, como strings, listas e tuplas, bem como 
# os tipos não sequenciais, como dicionários e arquivos.

# iterável de cidades
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

# loop for que realiza uma iteração sobre a lista cities (cidades)
for city in cities:
    print(city.title())
	
# Componentes de um loop for
# A primeira linha do loop começa com a palavra-chave for, que sinaliza que se 
# trata de um loop for
# Depois disso, vem iteration_variable in iterable, que indica que o iterável 
# está passando por um ciclo de processamento (loop) e qual nome usar para o 
# elemento do iterável que está sendo atualmente processado. Neste exemplo, 
# a variável de iteração, city, seria “new york city” na primeira iteração e 
# "mountain view" na segunda.
# A abertura de um loop for sempre termina com dois pontos :.
# Após a abertura de um loop for vem um bloco de código indentado que deve ser 
# executado a cada iteração do loop for. Neste bloco, podemos usar a variável de 
# iteração para acessar o valor do elemento que está sendo atualmente processado.

# Você pode nomear variáveis de iteração do jeito que preferir. Um padrão comum 
# é dar à variável de iteração e ao iterável o mesmo nome, com exceção das 
# versões singulares e plurais, respectivamente (por exemplo, 'cidade' e 'cidades').

# Alterar uma lista é um pouco mais complicado e requer o uso de uma nova
# função: range().

# range() é uma função interna usada para criar sequências imutáveis de números. 
# Ela tem três argumentos, que devem ser números inteiros.

# range(start=0, stop, step=1)
# 'Start' é o primeiro número da sequência, 'stop' é 1 a mais do que o último 
# número da sequência e 'step' é a diferença entre cada número na sequência. Se 
# não for especificado, o 'start' padrão é 0, e o 'passo' padrão é 1 (que é o que 
# '= 0' e '= 1' nos diz acima).

# Se você especificar um número inteiro dentro do parênteses com range(), ele 
# é usado como o valor para 'stop', e os padrões são usados para os outros dois.
# E.g. list(range(4)) returns [0, 1, 2, 3]
# Se você especificar dois números inteiros dentro do parênteses com range(), 
# eles serão usados como o valor para 'start' e 'stop', e o padrão será utilizado para 'step'.
# E.g. list(range(2, 6)) returns [2, 3, 4, 5]
# Ou você pode especificar todos os três inteiros para 'start', 'stop' e 'step'.
# E.g. list(range(1, 10, 2)) returns [1, 3, 5, 7, 9]
# Observe que, nesses exemplos, envolvemos range em uma lista. Isso ocorre porque 
# a saída de range em si é apenas um objeto range. Podemos ver o conjunto de 
# valores no objeto range ao convertê-lo em uma lista ou iterar por meio dele em um loop for.

# Nós podemos usar a função range para gerar os índices para cada valor na lista 
# cities. Isso nos permite acessar os elementos da lista usando cities[índice], 
# para podermos alterar os valores em cada posição da lista cities.

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    cities[index] = cities[index].title()

# Enquanto alteração de lista é uma aplicação da função range, essa não é a única 
# coisa útil. Você frequentemente usará range com um loop for para repetir uma ação 
# um certo número de vezes.

for i in range(3):
    print("Hello!")
	
###
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    tmp_name = name.lower()
    tmp_name = tmp_name.replace(' ', '_')
    usernames.append(tmp_name)

print(usernames)

###

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for index in range(len(tokens)):
    if tokens[index].find('<') == 0:
        count += 1

print(count)

####
tokens = ['<greeting>', 'Hello World!', '</greeting>']

count = 0
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)

####
items = ['first string', 'second string']

html_str = "<ul>\n"
for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)

####
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}

for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
		
#####
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}

for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1
	
###
# Iterando dicionários com loops for
# Quando você iterar um dicionário usando um loop for, fazer do jeito normal 
# (for n in some_dict) vai apenas dar acesso às chaves do dicionário - que é 
# o que queremos em algumas situações. Em outros casos, queremos iterar as _
# chaves_e_valores_ do dicionário. Vamos ver como isso é feito a partir de um 
# exemplo

# Se quiser iterar tanto as chaves como os valores, você pode usar o método 
# interno items desta forma:

for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))
	
# O items é um método incrível que retorna as tuplas de pares chave-valor, 
# que você pode usar para iterar dicionários em loops for.

# Loops While
# Loops for são um exemplo do significado de “iteração definida”, com o 
# corpo do loop sendo executado um número pré-definido de vezes. Isso 
# difere da "iteração indefinida", que é quando um loop é repetido um 
# número desconhecido de vezes e só termina quando alguma condição for 
# atendida, que é o que acontece em um loop while

card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand)  <= 17:
    hand.append(card_deck.pop())
	
# Este exemplo apresenta duas novas funções. sum retorna a soma dos 
# elementos em uma lista, e pop é um método de lista que remove o último 
# elemento de uma lista e o retorna.	

###
manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

####
# Zip E Enumeração
# zip e enumerate (enumerar) são funções internas úteis que podem vir a 
# calhar quando se lida com loops.

# Zip
# zip retorna um iterador que combina múltiplos iteráveis em uma sequência 
# de tuplas. Cada tupla contém os elementos nessa posição de todos os iteráveis. 
# Por exemplo, exibindo

list(zip(['a', 'b', 'c'], [1, 2, 3])) 

# geraria a saída [('a', 1), ('b', 2), ('c', 3)].
# Como fizemos para range(), precisamos converter em uma lista ou iterar 
# por meio dela com um loop para ver os elementos.
# Você pode desempacotar cada tupla em um loop for como este.

letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

# Além de compactar duas listas juntas, você também pode descompactar 
# uma lista usando um asterisco.

some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)

# Isso criaria as listas de letters e nums que vimos anteriormente.

###
# Enumerate
# enumerate é uma função interna que devolve um iterador de tuplas contendo
# índices e valores para um lista. Você vai usar isso muitas vezes quando quiser 
# o índice junto a cada elemento de um iterável em um loop.

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)

# Este código gera a saída:
# 0 a
# 1 b
# 2 c
# 3 d
# 4 e

#####
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for labels, x_coord, y_coord, z_coord in zip(labels, x_coord, y_coord, z_coord):
    points.append('{}: {}, {}, {}'.format(labels, x_coord, y_coord, z_coord))

for point in points:
    print(point)
	
	
####
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))

for point in points:
    print(point)
	

####
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)

####
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

names, heights = zip(*cast)
print(names)
print(heights)

####
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)

####
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, character in enumerate(cast):
    cast[i] = character + " " + str(heights[i])

print(cast)

####
# Compreensão De Listas
# Em Python, você pode criar listas rapidamente e de forma concisa com 
# compreensão de listas. Este exemplo anterior:

capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())

# pode ser reduzido para:

capitalized_cities = [city.title() for city in cities]

# Condicionais na compreensão de listas
# Você também pode adicionar condicionais para compreensão de listas 
# (listcomps). Após o iterável, você pode usar a palavra-chave if para 
# verificar uma condição em cada iteração.

squares = [x**2 for x in range(9) if x % 2 == 0]

# O código acima define squares como a lista [0, 4, 16, 36, 64], 
# já que x para a potência de 2 é avaliada somente se x for par. 
# Se você quiser adicionar um else, receberá um erro de sintaxe fazendo isso.

squares = [x**2 for x in range(9) if x % 2 == 0 else x + 3]

# Se quiser adicionar else, você deve mover condicionais para o 
# início de listcomp, logo após a expressão, desta forma.

squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]

# Compreensão de listas não é encontrada em outras linguagens, 
# mas é muito comum em Python

####
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)

####
multiples_3 = [x * 3 for x in range(1, 21)]
print(multiples_3)

####
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score >= 65]
print(passed)



