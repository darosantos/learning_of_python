# A funçõa range gera numero aleatórios dentro do intervalo especificado

# isto aqui não funciona
print(range(1, 5))

for value in range(1, 5):
    print(value)

# Converte os números gerados em sequência em um array
random_numbers = list(range(1, 5))

print(random_numbers)

# Alterando o incremento em range, o ultimo parâmetro informa de quanto em quanto
# será incrementado o valor até alcaçar seu limite
random_numbers = list(range(1, 13, 3))

print(random_numbers)

# Funções estatísticas com números
vector_numbers = list(range(1, 100))

print(min(vector_numbers)) # minimo
print(max(vector_numbers)) # maximo
print(sum(vector_numbers)) # soma de todos

# List comprehensions - gera lista aleatórios em uma única espressão
number_quadract_perfect = [value**2 for value in range(1, 11)]

print(number_quadract_perfect)

# Selecionando um conjunto do vetor
print(vector_numbers[0:3])
print(vector_numbers[40:50])
print(vector_numbers[70:98])

# Loop em um subconjunto dos dados
for vcs in vector_numbers[70:98]:
    print(vcs**2)

# Copiando listas
cp_vcn =  vector_numbers[40:50]

print(cp_vcn)

# Copiando inteiramente uma lista
cp_vcn1 = vector_numbers[:]
cp_vcn2 = vector_numbers[:]

cp_vcn1.append(20)
cp_vcn2.append(30)

print(cp_vcn1)
print(cp_vcn2)

# A situação abaixo não cria uma cópia da lista, mas uma nova variável que faz referência a mesma lista
pvector_numbers = vector_numbers

pvector_numbers.append(50)
print(vector_numbers)
print(pvector_numbers)

# Tuplas = são como listas, porém seus valores não podem ser mudados depois de atribuidos
rectagle_dimensions = (200, 100)

print(rectagle_dimensions)
print(rectagle_dimensions[0])
print(rectagle_dimensions[1])
