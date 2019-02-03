# Verificando o tipo de uma variável
axis = 'danilo'
print( type(axis) )

# Repete a string 5 vezes
axis = 'Helo'
print( axis * 5 )

# Armazena o tamanho de uma string
axis = len('Hello my world!')
print( str(axis) )

# Funciona como printf em c 
# Examplo 2
animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))

# Você viu que nós também podemos usar in e not in para retornar um bool que
# afirma se um elemento existe ou não dentro de nossa lista ou se uma string 
# é uma substring de outra.

>>> 'this' in 'this is a string'
True
>>> 'in' in 'this is a string'
True
>>> 'isa' in 'this is a string'
False
>>> 5 not in [1, 2, 3, 4, 6]
True
>>> 5 in [1, 2, 3, 4, 6]
False

# Mutabilidade indica se podemos ou não alterar um objeto depois que ele foi 
# criado. Se um objeto (como uma lista ou string) pode ser alterado (tal qual 
# uma lista pode), então dizemos que ele é mutável. No entanto, se um objeto 
# não pode ser alterado com a criação de um objeto completamente novo 
# como as strings), então o objeto é considerado imutável.
# Há duas coisas a se ter em mente para cada um dos tipos de dados que você está usando:
# Eles são mutáveis?
# Eles são ordenados?
# Tanto strings quanto listas são ordenadas

# len() devolve quantos elementos existem em uma lista.
# max() devolve o maior elemento da lista. A maneira como é determinado o maior elemento de uma lista depende de quais tipos de objetos estão presentes na lista. O elemento máximo em uma lista de números é o maior número. O elemento máximo de uma lista de strings é o elemento que ocorreria por último caso a lista estivesse em ordem alfabética. Isso funciona porque a função máximo é definida em termos do operador de comparação ‘maior do que’. A função máximo é indefinida para listas que contêm elementos de tipos diferentes, incomparáveis.
# min() devolve o menor elemento em uma lista. Mínimo é o oposto de máximo e retorna o menor elemento de uma lista.
# sorted() devolve uma cópia de uma lista, ordenada do menor para o maior, deixando a lista inalterada.

# Método join
# Join é um método de strings que recebe uma lista de strings como argumento e devolve uma string formada pelos elementos da lista unidos por um separador de strings.

new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)

# Método append
# Um método útil chamado append adiciona um elemento ao final de uma lista.

letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)

# Tuplas são semelhantes a listas, pois também armazenam uma coleção ordenada 
# de objetos que podem ser acessados por meio de seus índices. Ao contrário das 
# listas, no entanto, as tuplas são imutáveis - não é possível adicionar e remover 
# itens de tuplas ou classificá-las no lugar.
# As tuplas também podem ser usadas para fazer a atribuição de diversas variáveis de 
# uma forma compacta.
# Os parênteses são opcionais ao definir tuplas, e programadores frequentemente os 
# omitem caso não ajudem a esclarecer o código.

dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))

# Na segunda linha, três variáveis são atribuídas a partir do conteúdo das dimensões 
# tupla. Esse processo é chamado desempacotamento de tupla. Você pode usar o 
# variáveis sem precisar acessá-las uma a uma e executar várias instruções de atribuição.

# Se não precisássemos usar dimensions diretamente, poderíamos encurtar essas duas 
# linhas de código para uma única linha que atribui três variáveis de uma só vez!

length, width, height = 52, 40, 100
print("The dimensions are {} x {} x {}".format(length, width, height))

# Conjuntos
# Um conjunto é um tipo de dados para coleções mutáveis não ordenadas de elementos 
# únicos. Uma aplicação de um conjunto é remover rapidamente duplicatas de uma lista.

numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)

# O que resultaria na saída:
# {1, 2, 3, 6}
# Conjuntos aceitam o operador in da mesma forma que as listas. Você pode adicionar 
# elementos aos conjuntos usando o método add, e removê-los usando o método pop, 
# tal como nas listas. Porém, quando você utiliza pop para remover um elemento de 
# um conjunto, um elemento aleatório é removido. Lembre-se de que conjuntos, ao 
# contrário das listas, não são ordenados, então, não há um “último elemento”.

fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set

print("watermelon" in fruit)  # check for element

fruit.add("watermelon")  # add an element
print(fruit)

print(fruit.pop())  # remove a random element

# Isso produz a saída:

# False
# {'grapefruit', 'orange', 'watermelon', 'banana', 'apple'}
# grapefruit
# {'orange', 'watermelon', 'banana', 'apple'}
# Outras operações que você pode executar com conjuntos incluem aquelas de conjuntos 
# matemáticos. Métodos como união, interseção e diferença são fáceis de realizar com 
# conjuntos e são muito mais rápidos do que esses operadores com outros contentores.

# Quando você remove um elemento de um conjunto, um elemento aleatório é removido 
# (lembre-se de que conjuntos, ao contrário das listas, não são ordenados, então, 
# não há um “último elemento”)

# Dicionários
# Um dicionário é um tipo de dado mutável que armazena mapeamentos de chaves 
# exclusivas para os valores. Aqui está um dicionário que armazena elementos 
# e seus números atômicos.

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

# Os dicionários podem ter chaves de qualquer tipo imutável, como inteiros 
# ou tuplas, não apenas strings. Não é necessário sequer que todas as chaves 
# sejam do mesmo tipo! Podemos procurar por valores ou inserir novos valores 
# no dicionário usando colchetes que contenham a chave.

print(elements["helium"])  # imprime o valor mapeado a "helium"
elements["lithium"] = 3  # insere "lithium" com um valor de 3 no dicionário

# Podemos verificar se um valor está em um dicionário da mesma forma que 
# verificamos se um valor está em uma lista ou conjunto com a palavra-chave in. 
# Os dicionários têm um método relacionado que também é útil, o get. Esse método 
# procura valores em um dicionário, mas, ao contrário de colchetes, devolve none 
# (ou um valor padrão de sua escolha) se a chave não for encontrada.

print("carbon" in elements)
print(elements.get("dilithium"))

# O que resultaria na saída:
# True
# None

# Carbono está no dicionário, então True é exibido. Dilithium não está em nosso 
# dicionário, então none é devolvido por get e depois exibido. Se você espera 
# que as pesquisas às vezes falhem, get pode ser uma ferramenta melhor do que 
# as pesquisas normais com colchetes, porque erros podem quebrar o seu programa.

# Operadores de identidade
# Keyword	Operator is	avalia se ambos os lados têm a mesma identidade
# is not	avalia se ambos os lados têm identidades diferentes
# Você pode verificar se uma chave devolveu none com o operador is. Você pode verificar o oposto utilizando is not.

n = elements.get("dilithium")
print(n is None)
print(n is not None)
O que resultaria na saída:

True
False

# get com um valor padrão
# Os dicionários têm um método relacionado que também é útil, get. get procura por valores 
# em um dicionário, mas, ao contrário de colchetes, devolve none (ou um valor padrão à sua 
# escolha) se a chave não for encontrada. Se você espera que as pesquisas às vezes falhem, 
# get pode ser uma ferramenta melhor do que as pesquisas normais com colchetes.

>>> elements.get('dilithium')
None
>>> elements['dilithium']
KeyError: 'dilithium'
>>> elements.get('kryptonite', 'There\'s no such element!')
"There's no such element!"

# Podemos incluir contentores em outros contentores para criar estruturas de dados 
# compostas. Por exemplo, este dicionário mapeia chaves para valores que são também 
# dicionários!

elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}
						 
# Podemos acessar elementos no dicionário aninhados assim.

helium = elements["helium"]  # pega o dicionário de helium
hydrogen_weight = elements["hydrogen"]["weight"]  # pega o weight (peso) de hydrogen

# Você também pode adicionar uma nova chave ao dicionário de elementos.

oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # cria um novo dicionário oxygen
elements["oxygen"] = oxygen  # coloca 'oxygen' como chave para o dicionário de elementos 
print('elements = ', elements)

###

verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, '\n')

# split verse into list of words
verse_list = verse.split()
print(verse_list, '\n')

# convert list to a data structure that stores unique elements
verse_set = set(verse_list)
print(verse_set, '\n')

# print the number of unique words
num_unique = len(verse_set)
print(num_unique, '\n')

#### 

verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(set(verse_dict.keys()))
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = 'breathe' in verse_dict.keys()
print(contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(sorted_keys[-1]) 