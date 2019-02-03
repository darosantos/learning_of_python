# Escopo de variável se refere a quais partes de um programa uma 
# variável pode ser referenciada ou utilizada.
# É importante considerar o escopo quando usamos variáveis em 
# funções. Se uma variável é criada dentro de uma função, só 
# pode ser usada dentro dessa função. Não é possível acessá-la 
# ora dessa função.

# ainda podemos acessar o valor da variável global word dentro 
# dessa função. No entanto, o valor de uma variável global não 
# pode ser modificado dentro da função. Se você quiser modificar 
# o valor da variável dentro dessa função, ele deve ser passado 
# como um argumento. Você verá mais sobre isso no próximo quiz.

# Recomendação: é melhor definir variáveis no menor escopo em 
# que elas serão necessárias. Enquanto funções podem se referir 
# a variáveis definidas em um escopo maior, isso raramente é uma 
# boa ideia, já que você pode não saber quais são as variáveis 
# que definiu, se seu programa tiver muitas variáveis.

# A documentação é usada para tornar seu código mais fácil de 
# entender e usar. As funções em especial são legíveis porque, 
# muitas vezes, elas usam documentação de strings, ou docstrings. 
# Docstrings são um tipo de comentário usado para explicar a 
# finalidade de uma função e como ela deve ser utilizada. Aqui 
# está uma função de densidade populacional com uma docstring.

def population_density(population, land_area):
    """Calculate the population density of an area. """
    return population / land_area
	
# Docstrings estão rodeadas por aspas triplas. A primeira linha 
3 da docstring é uma breve explicação do propósito da função. 
# Se você acha que a documentação é suficiente, pode encerrar 
# a docstring neste ponto; docstrings de linha única são 
# perfeitamente aceitáveis, como no exemplo acima.

# Expressões lambda
# Você pode usar expressões lambda para criar funções anônimas. Ou seja, 
# funções que não têm um nome. Elas são úteis para a criação de funções 
# rápidas que não serão necessárias posteriormente em seu código. Isso 
# pode ser especialmente útil para funções de ordem superior ou aquelas 
# que aceitam outras funções como argumentos.

# Com uma expressão lambda, esta função:

def multiply(x, y):
    return x * y

# pode ser reduzida para:

multiply = lambda x, y: x * y

# Ambas estas funções são usadas da mesma maneira. Em ambos os casos,
#  podemos chamar multiply assim:

multiply(4, 7)

# Componentes de uma função lambda
# A palavra-chave lambda é utilizada para indicar que se trata de uma 
# expressão lambda.
# separados por vírgulas e seguidos por dois pontos :. Semelhante às 
# funções, a maneira como os argumentos são nomeados em uma expressão 
# lambda é arbitrária.
# Por último está uma expressão que é avaliada e devolvida nessa 
# função. Isto se parece muito com uma expressão que você pode ver 
# como declaração de retorno em uma função.
# Com essa estrutura, as expressões lambda não são ideais para 
# funções complexas, mas podem ser muito úteis para funções curtas e simples.

# map() é uma função interna de ordem superior que aceita uma função 
# e um iterável como entradas e devolve um iterador que aplica a 
# função para cada elemento do iterável. O código abaixo usa map()
# para encontrar a média de cada lista em numbers e criar a lista average
# Em outras palavras: map recebe qualquer função como primeiro 
# parâmetro e uma lista como segundo parâmetro, nesse exemplo a 
# função mean e a lista numbers, e aplica a função a todos elementos 
# da lista, um a um. O resultado obtido é um objeto do tipo map com 
# as médias de cada lista em numbers. Na linha 11, o retorno da 
# função é convertido de volta para list.

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)


# filter() é uma função interna de ordem superior que aceita uma função
# e um iterável como entradas e devolve um iterador com os elementos do
# iterável para os quais a função retorna o valor true. O código abaixo
# usa filter() para obter os nomes em cities que possuem menos de 10 
# caracteres de tamanho para criar a lista short_cities

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)

#### 
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)

####
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)

###
# Iteradores E Geradores
# Iteráveis são objetos que podem retornar um de seus elementos de cada vez, 
# assim como uma lista. Muitas das funções internas que usamos até agora,
# como enumerate, retornam um iterador.

# Um iterador é um objeto que representa uma corrente de dados. Isso é 
# diferente de uma lista, que também é um iterável, mas não um iterador,
# porque não é uma corrente de dados.

# Geradores são uma maneira simples de criar iteradores usando funções. 
# Você também pode definir os iteradores usando classes.

# Aqui está um exemplo de uma função de gerador chamado my_range, 
# que produz um iterador que é uma corrente de números de 0 até (x - 1).

def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1

# Observe que, em vez de usar a palavra-chave return, ele usa yield. 
# Isso permite que a função devolva um valor de cada vez, começando de 
# onde parou a cada vez que recorremos a ele. A palavra-chave yield é 
# o que diferencia um gerador de uma função típica.

# Lembre que, desde que retorne um iterador, podemos convertê-lo em 
# uma lista ou iterar por meio dele com um loop para visualizar seu 
# conteúdo. Por exemplo, este código:

for x in my_range(5):
    print(x)
	
###
# Por que geradores?
# ocê pode estar se perguntando por que usaríamos geradores em vez 
# de listas. Aqui está um trecho de uma página do Stack Overflow 
# que aborda isso:

# Geradores são uma maneira preguiçosa de construir iteráveis. 
# Eles são úteis quando a lista completamente preenchida não 
# caberia na memória ou quando o custo para calcular cada elemento 
# da lista é alto e você quer deixar para fazer o mais tarde possível. 
# Mas, só podemos iterar sobre eles uma vez.

####
Implementando my_enumerate
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    count = start
    for element in iterable:
        yield count, element
        count += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
	

####
def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

for chunk in chunker(range(25), 4):
    print(list(chunk))
	
####
# Gerador de expressões
# Aqui está um conceito legal que combina geradores e compreensão de 
# listas! Na verdade, você pode criar um gerador da mesma maneira 
# que normalmente escreveria uma compreensão da lista, utilizando 
# parênteses em vez de colchetes. Por exemplo:

sq_list = [x**2 for x in range(10)]  # isto produz uma lista de quadrados

sq_iterator = (x**2 for x in range(10))  # isto produz um iterador de quadrados

# Isso pode ajudá-lo a economizar tempo e criar um código eficiente!