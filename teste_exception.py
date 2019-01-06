# As exceções são tratadas com blocos try-except. Um bloco try-except
# pede que Python faça algo, mas também lhe diz o que deve ser feito se
# uma exceção for levantada. Ao usar blocos try-except, seus programas
# continuarão a executar, mesmo que algo comece a dar errado. Em vez
# de tracebacks, que podem ser confusos para os usuários lerem, os
# usuários verão mensagens de erro simpáticas escritas por você.

# Se houver mais código depois do bloco try-except, o programa
# continuará executando, pois dissemos a Python como o erro deve ser
# tratado.

try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Qualquer código que
# dependa do bloco try executar com sucesso deve ser colocado no bloco
# else:


print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

# O único código que deve
# estar em uma instrução try é aquele que pode fazer uma exceção ser
# levantada. Às vezes, você terá um código adicional que deverá ser
# executado somente se o bloco try tiver sucesso; esse código deve estar no
# bloco else. O bloco except diz a Python o que ele deve fazer, caso uma
# determinada exceção ocorra quando ele tentar executar o código que está
# na instrução try

filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # Conta o número aproximado de palavras no arquivo
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")


def count_words(filename):
    """Conta o número aproximado de palavras em um arquivo."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not"
        print(msg)
    else:
        # "Conta o número aproximado de palavras no arquivo"
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


filename = 'alice.txt'
count_words(filename)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)


# Às vezes, queremos que o programa falhe silenciosamente
# quando uma exceção ocorrer e continue como se nada tivesse
# acontecido. Para fazer um programa falhar em silêncio, escreva um
# bloco try como seria feito normalmente, mas diga de forma explícita a
# Python para não fazer nada no bloco except. Python tem uma instrução
# pass que lhe diz para não fazer nada em um bloco

def count_words2(filename):
    """Conta o número aproximado de palavras em um arquivo."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # "Conta o número aproximado de palavras no arquivo"
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


# A instrução pass também atua como um marcador. É um lembrete de
# que você optou por não fazer nada em um ponto específico da execução
# de seu programa, mas talvez queira fazer algo nesse local, no futuro

