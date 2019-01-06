# Declara uma variável e atribui um texto a ela
message = 'Hello Word in Python... Start for beginners'

# Imprime na tela uma string
print( message )

# Método capitalize coloca somente a primeira letra da palavra em maíuscula
print( message.capitalize() )

# Método capitalize coloca somente a primeira letra da palavra em minúscula
print( message.casefold() )

# Método capitalize coloca somente a primeira letra da palavra em minúscula
print( message.lower() )

# Método capitalize coloca somente a primeira letra da palavra em maiuscula
print( message.upper() )

# Concatena strings
a = 'Programmer Daro'
b = ' - ' + message
print( a + ' ' + b )

# Usa caracteres de espaço \n \t
print("Nome \t Sobrenome \t Email \t Telefone \n Danilo \t Santos \t danilo.santosrs@hotmail.com \t null")

# Remove espaço em brando do final da string
message = message.rstrip()

# Remove espaço em branco do inicio da string
message = message.lstrip()

# Remove espaços em branco em ambos os lados
message = message.strip()

# Str é uma função que converte para tipo string
idade = 25
print( 'Minha idade e = ' + str(idade))

# O método split() separa uma string em partes sempre que encontra
# um espaço, e armazena todas as partes da string em uma lista. O
# resultado é uma lista de palavras da string, embora algumas pontuações
# possam também aparecer com determinadas palavras.
palavras = message.split()
print(palavras)

# o método count() para descobrir quantas vezes uma palavra ou expressão aparece em uma string
t_palavras = message.count()
print(t_palavras)