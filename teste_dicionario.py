# Um dicionário em Python é uma coleção de pares chave-valor. Cada chave
# é conectada a um valor, e você pode usar uma chave para acessar o valor
# associado a ela. O valor de uma chave pode ser um número, uma string,
# uma lista ou até mesmo outro dicionário. De fato, podemos usar
# qualquer objeto que possa ser criado em Python como valor de um
# dicionário.

# Dicionário em python é similar a uma struct em c ou um array indexado por strings

# Criando um dicionário

cliente = {'nome': 'Danilo', 'sobrenome': 'Santos', 'email': 'danilo_santosrs@hotmail.com', 'telefone': 'null'}

print(cliente)

# Acessando chaves do dicionário
print(cliente['nome'])

# Modificando valores em chaves
cliente['nome'] = 'Daro'

print(cliente)

# Adicionando novas chaves e valores
cliente['cpf'] = 'null'

print(cliente)

# Observe que a
# ordem dos pares chave-valor não coincide com a ordem em que os
# adicionamos. Python não se importa com a ordem em que armazenamos
# cada par chave-valor; ele só se importa com a conexão entre cada chave
# e seu valor.

# Criando um dicionário vazio

cadastro = {}

print(cadastro)

# Removendo um valor permanentemente do dicionário
print(cliente)

del cliente['cpf']

print(cliente)

# Podemos percorrer todos os pares chave-valor de um
# dicionário usando suas chaves ou seus valores.

# Loop em um dicionário
# O método items deve ser usado para retornar a lista dos pares armazenados
for key, value in cliente.items():
    print("key = " + key + ' value = ' + value + "\n")

# Percorrendo as chaves de um dicionário
for name in cliente.keys():
    print(name + "\n")

for name in cliente:
    print(name + "\n")

# Ordenando as chaves de uma lista com a função sorted
print(cliente)
for field in sorted(cliente.keys()):
    print(field.title() + "\t")

# Obtendo uma lista com todos os valores de um dicionário
for dataField in cliente.values():
    print(dataField.capitalize() + "\t")

# Um conjunto é semelhante a uma lista, exceto que cada item de um conjunto deve ser único
# Quando colocamos set() em torno de uma lista que contenha itens duplicados, Python identifica
# os itens únicos na lista e cria um conjunto a partir desses itens
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# Podemos aninhar um conjunto de dicionários em uma lista, uma lista de itens em um dicionário ou até
# mesmo um dicionário em outro dicionário. Aninhar informações é um recurso eficaz, como mostrarão os próximos exemplos.
