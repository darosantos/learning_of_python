# Aprender a trabalhar com arquivos e a salvar dados deixará seus
# programas mais fáceis de usar. Os usuários poderão escolher quais
# dados devem fornecer e quando. As pessoas podem executar seu
# programa, fazer alguma tarefa e então fechá-lo e retomá-lo mais tarde,
# do ponto em que pararam. Aprender a tratar exceções ajudará você a
# lidar com situações em que os arquivos não existam e com outros
# problemas que possam fazer seus programas falharem. Isso deixará seus
# programas mais robustos quando dados ruins forem encontrados, sejam
# eles provenientes de erros inocentes ou de tentativas maliciosas de fazer
# seus programas falharem.


# Lê um arquivo por completo
with open('my_file.txt') as file_object:
    contents = file_object.read()
    print(contents)


# função open() precisa de
# um argumento: o nome do arquivo que você quer abrir. Python procura
# esse arquivo no diretório em que o programa executando no momento
# está armazenado.
# A função open() devolve um objeto que
# representa o arquivo. Nesse caso, open('pi_digits.txt') devolve um
# objeto que representa pi_digits.txt. Python armazena esse objeto em
# file_object, com o qual trabalharemos posteriormente no programa

# A palavra reservada with fecha o arquivo depois que não for mais
# necessário acessá-lo.

# Para fazer Python abrir arquivos de um diretório que não seja
# aquele em que seu arquivo de programa está armazenado, é preciso
# fornecer um path de arquivo, que diz a Python para procurar em um local
# específico de seu sistema.

# Lê um arquivo linha a linha
# para este exemplo um caractere invisível de
# quebra de linha está no final de cada linha do arquivo-texto
filename = 'my_file.txt'
i = 1
with open(filename) as file_object:
    for line in file_object:
        printed = '>>> ' + str(i) + ' - ' + line
        print(printed.rstrip())
        i = i + 1


# Usamos a sintaxe with para deixar Python abrir e fechar o arquivo de modo apropriado
# Quando usamos with, o objeto arquivo devolvido por open() estará
# disponível somente no bloco with que o contém.

# O exemplo a seguir armazena as linhas de pi_digits.txt em uma lista no
# bloco with e, em seguida, exibe as linhas fora desse bloco

with open(filename) as file_object:
    lines = file_object.readlines()

py_line = ''

for line in lines:
    py_line = line.rstrip()
    print(line.rstrip())

# O método readlines() armazena cada linha do arquivo em uma lista.

# Operador in pode ser utilizado para pesquisar em uma string
if 'danilo' in py_line:
    print('A string buscada existe em py_line')