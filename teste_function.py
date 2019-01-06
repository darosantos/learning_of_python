def hello_word_fuction():
    print('Hello World!')

# Name é um parÂmetro, ou seja, uma variável que indica qual informação é necessária para trabalhar
# O valor passado em NAME É O argumento
def hello_word_function_param(name):
    print('Hello World! Hi ' + name)

hello_word_fuction()

hello_word_function_param('Danilo')

# Os argumentos podem ser passados para as funções de várias maneiras. Podemos usar argumentos posicionais, que devem estar
# na mesma ordem em que os parâmetros foram escritos, argumentos nomeados (keyword arguments), em que cada argumento é
# constituído de um nome de variável e de um valor, ou por meio de listas e dicionários de valores

# A variável username na definição de greet_user() é um exemplo de
# parâmetro – uma informação de que a função precisa para executar sua
# tarefa. O valor 'jesse' em greet_user('jesse') é um exemplo de
# argumento. Um argumento é uma informação passada para uma função
# em sua chamada. Quando chamamos a função, colocamos entre
# parênteses o valor com que queremos que a função trabalhe. Nesse
# caso, o argumento 'jesse' foi passado para a função greet_user() e o
# valor foi armazenado no parâmetro username.

# Os argumentos podem ser passados para as funções de
# várias maneiras. Podemos usar argumentos posicionais, que devem estar
# na mesma ordem em que os parâmetros foram escritos, argumentos
# nomeados (keyword arguments), em que cada argumento é constituído
# de um nome de variável e de um valor, ou por meio de listas e
# dicionários de valores.

# Quando chamamos uma função, Python precisa fazer a correspondência
# entre cada argumento da chamada da função e um parâmetro da
# definição. A maneira mais simples de fazer isso é contar com a ordem
# dos argumentos fornecidos. Valores cuja correspondência seja feita
# dessa maneira são chamados de argumentos posicionais.
# Podemos usar tantos argumentos posicionais quantos forem
# necessários nas funções. Python trabalha com os argumentos fornecidos
# na chamada da função e faz a correspondência de cada um com o
# parâmetro associado na definição da função.

# Um argumento nomeado (keyword argument) é um par nome-valor
# passado para uma função. Associamos diretamente o nome e o valor no
# próprio argumento para que não haja confusão quando ele for passado
# para a função
# Argumentos nomeados fazem com que você não precise se preocupar com
# a ordem correta de seus argumentos na chamada da função e
# deixam claro o papel de cada valor na chamada.


def describe_pet(animal_type, pet_name):
    # """Exibe informações sobre um animal de estimação."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(animal_type='hamster', pet_name='harry')


# função describe_pet() não mudou. Entretanto, quando chamamos a função, dizemos
# explicitamente a Python a qual parâmetro cada argumento deve
# corresponder. Quando Python lê a chamada da função, ele sabe que deve
# armazenar o argumento 'hamster' no parâmetro animal_type e o argumento
# 'harry' em pet_name. A saída mostra corretamente que temos um hamster
# chamado Harry.


# Quando usar argumentos nomeados, lembre-se de usar os nomes exatos dos
# parâmetros usados na definição da função.

# Ao escrever uma função, podemos definir um valor default para cada
# parâmetro. Se um argumento para um parâmetro for especificado na
# chamada da função, Python usará o valor desse argumento. Se não for,
# o valor default do parâmetro será utilizado. Portanto, se um valor default
# for definido para um parâmetro, você poderá excluir o argumento
# correspondente, que normalmente seria especificado na chamada da
# função. Usar valores default pode simplificar suas chamadas de função e
# deixar mais claro o modo como suas funções normalmente são
# utilizadas.


def describe_pet_2(pet_name, animal_type='dog'):
    # """Exibe informações sobre um animal de estimação."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# Observe que a ordem dos parâmetros na definição da função precisou
# ser alterada. Como o uso do valor default faz com que não seja
# necessário especificar um tipo de animal como argumento, o único
# argumento restante na chamada da função é o nome do animal de
# estimação. Python continua interpretando esse valor como um
# argumento posicional, portanto, se a função for chamada somente com
# o nome de um animal de estimação, esse argumento corresponderá ao
# primeiro parâmetro listado na definição da função. Esse é o motivo pelo
# qual o primeiro parâmetro deve ser pet_name.


# Como os argumentos posicionais, os argumentos nomeados e os valores
# default podem ser usados em conjunto, e com frequência você terá
# várias maneiras equivalentes de chamar uma função.
# O estilo de chamada que você usar realmente não importa. Desde que
# suas chamadas de função gerem a saída desejada, basta usar o estilo que
# achar mais fácil de entender.

# Argumentos sem correspondência ocorrem quando fornecemos menos ou mais
# argumentos necessários à função para que ela realize sua tarefa.

# Valores default podem ser usados para deixar um argumento opcional.
# Valores opcionais permitem que as funções tratem uma grande
# variedade de casos de uso, ao mesmo tempo que simplificam ao máximo
# as chamadas de função


def get_formatted_name(first_name, last_name):
    # """Devolve um nome completo formatado de modo elegante."""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# Python interpreta strings não vazias como True
# Uma função pode devolver qualquer tipo de valor necessário, incluindo
# estruturas de dados mais complexas como listas e dicionários


def build_person(first_name, last_name, age=''):
    # """Devolve um dicionário com informações sobre uma pessoa."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix')
print(musician)


# Você pode enviar uma cópia de uma lista para uma função assim:
# nome_da_função(nome_da_lista[:]) A notação de fatia [:] cria uma
# cópia da lista para ser enviada à função.
# Para uma função, é mais eficiente trabalhar com uma lista
# existente a fim de evitar o uso de tempo e de memória necessários para criar uma cópia
# separada, em especial quando trabalhamos com listas  grandes.


def make_pizza(*toppings):
    # """Apresenta apizza que estamos prestes a preparar."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print('- ' + str(topping))


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# O asterisco no nome do parâmetro *toppings diz a Python para
# criar uma tupla vazia chamada toppings e reunir os valores recebidos nessa tupla.
# A função no próximo exemplo tem um parâmetro *toppings, mas esse parâmetro agrupa tantos
# argumentos quantos forem fornecidos na linha de chamada

# Se quiser que uma função aceite vários tipos de argumentos, o
# parâmetro que aceita um número arbitrário de argumentos deve ser
# colocado por último na definição da função. Python faz a
# correspondência de argumentos posicionais e nomeados antes, e depois
# agrupa qualquer argumento remanescente no último parâmetro.


def build_profile(first, last, **user_info):
    # """Constrói um dicionário contendo tudo que sabemos sobre um usuário."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

# Os asteriscos duplos antes do parâmetro **user_info fazem Python criar um dicionário vazio chamado
# user_info e colocar quaisquer pares nome-valor recebidos nesse
# dicionário. Nessa função, podemos acessar os pares nome-valor em
# user_info como faríamos com qualquer dicionário.

# Podemos misturar valores posicionais, nomeados e arbitrários de
# várias maneiras diferentes quando escrevermos nossas próprias funções


