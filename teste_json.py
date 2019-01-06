# O módulo json permite descarregar estruturas de dados Python
# simples em um arquivo e carregar os dados desse arquivo na próxima
# vez que o programa executar. Também podemos usar json para
# compartilhar dados entre diferentes programas Python. Melhor ainda, o
# formato de dados JSON não é específico de Python, portanto podemos
# compartilhar dados armazenados em formato JSON com pessoas que
# trabalhem com várias outras linguagens de programação. É um formato
# útil e portável, além de ser fácil de aprender.

# O formato JSON (JavaScript Object Notation, ou Notação de Objetos
# JavaScript) foi originalmente desenvolvido para JavaScript. Apesar disso,
# tornou-se um formato comum, usado por muitas linguagens, incluindo
# Python.

# A função json.dump() aceita dois argumentos: um dado para armazenar
# e um objeto arquivo que pode ser usado para armazenar o dado.

import json


numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)


# se json.load() para ler a lista de volta para a memória
with open(filename) as f_obj:
    numbers = json.load(f_obj)
    print(numbers)


username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
print("We'll remember you when you come back, " + username + "!")


with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")


filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")


# Com frequência você chegará a um ponto em que seu código
# funcionará, mas reconhecerá que ele poderia ser melhorado se fosse
# dividido em uma série de funções com tarefas específicas. Esse processo
# se chama refatoração. A refatoração deixa seu código mais limpo, mais
# fácil de compreender e de estender.


def get_stored_username():
    """Obtém o nome do usuário já armazenado se estiver disponível."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Pede um novo nome de usuário."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Saúda o usuário pelo nome."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()

# Essa separação do
# trabalho em compartimentos é uma parte essencial na escrita de um código
# claro, que seja fácil de manter e de estender.

