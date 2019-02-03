# C nhecendo atay

# Cria o array
frutas = ['laranja','banana','maçã']

print(frutas)

# Adiciona um elemento no final do array
frutas.append('mamão')

print(frutas)

# Insere um elemento em alguma posição do array
frutas.insert(3, 'melancia')
frutas.insert(0, 'melão')

print(frutas)

# Remove permanentemente um elemento do array
del frutas[4]

print(frutas)

# Remove um item do final da lista e retorna ele
popped_fruit = frutas.pop()

print(popped_fruit)
print(frutas)

# Remove um item da posição x da lista e retorna ele
popped_fruit = frutas.pop(2)

print(popped_fruit)
print(frutas)

# Remove a primeira ocorrência de um valor contido no array
frutas.append('laranja')
frutas.remove('laranja')

print(frutas)

# Ordena a lista em ordem alfabética
frutas.sort()

print(frutas)

# Ordena a lista em ordem alfabética inversa/decrescente
frutas.sort(reverse=True)

print(frutas)

# Ordena o array e retorna uma cópia ordenda do mesmo sem modificar o original
ordened_fruit = sorted(frutas)

print(frutas)
print(ordened_fruit)

# Inverte os elementos de uma lista
frutas.reverse()

print(frutas)

# Determina o tamanho de um array
fruit_length = len(frutas)

print('Quantidade de frutas = ' + str(fruit_length))

# Loop For em array
fruits = ['laranja','banana','maçã', 'melancia', 'mamão', 'melão']

for fruit in fruits:
    print(fruit)

