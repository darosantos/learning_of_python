fruits = ['laranja','banana','maçã', 'melancia', 'mamão', 'melão']

for fruit in fruits:
    if fruit == 'melancia':
        print(fruit.upper())
    else:
        print(fruit.lower())


# Operadores lógicos
#   AND
#   OR
# Operadores aritméticos
#   +
#   -
#   *
#   /
# Operadores de igualdade
#   ==
#   !=
# Operadores lógico matemáticos
#   >
#   <
#   >=
#   <=
#   % -> resto da divisão

# Operador in verifica se determinado valor está presente em uma lista e not in o inverso
search_for_fruit = "melão" in fruit
print("Search for fruit: " + str(search_for_fruit))

search_for_fruit = "goiaba" in fruit
print("Search for fruit: " + str(search_for_fruit))

search_for_fruit = "melão" not in fruit
print("Search for fruit: " + str(search_for_fruit))

search_for_fruit = "goiaba" not in fruit
print("Search for fruit: " + str(search_for_fruit))

# Se senão se
for fruit in fruits:
    if fruit == "banana" or fruit == "melao":
        print("Fruta amarela")
    elif fruit == "melancia" or fruit == "maçã":
        print("Fruta vermelha")
    else:
        print("Outra cor de fruta")

# Para verificar se uma lista está vazia basta utilizar o nome dela em uma condição
new_fruits = []
if new_fruits:
    print('Possui elemento em new fruits')
else:
    print('Não possui elementos em new fruits')

if fruits:
    print('Possui elemento em fruits')
else:
    print('Não possui elemento em fruits')