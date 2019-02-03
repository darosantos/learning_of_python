# Podemos também interpretar a entrada do usuário como 
# uma expressão Python usando a função interna eval. Esta 
# função avalia uma string como uma linha de Python.

result = eval(input("Enter an expression: "))
print(result)


####
# Especificando exceções
# Podemos especificar com qual erro queremos lidar em um 
# blocoexcept desta maneira:

try:
    # some code
except ValueError:
    # some code

# Agora, ele pega a exceção ValueError, mas não as outras exceções. 
# Se queremos que esse tratador lide com mais de um tipo de exceção, 
# nós podemos incluir uma tupla após except com as exceções.

try:
    # some code
except ValueError, KeyboardInterrupt:
    # some code

# Ou, se quisermos executar diferentes blocos de código dependendo 
# da exceção, você pode ter vários blocos except.

try:
    # some code
except ValueError:
    # some code
except KeyboardInterrupt:
    # some code
	
###
# Acessando as mensagens de erro
# Quando você lida com uma exceção, ainda pode acessar sua mensagem 
# de erro desta forma:

try:
    # some code
except ZeroDivisionError as e:
   # some code
   print("ZeroDivisionError occurred: {}".format(e))
   
###
# Então, você ainda pode acessar as mensagens de erro, mesmo que 
# lide com eles para evitar que seu programa seja interrompido!

# Se você não tiver um erro específico com o qual está lidando, 
# ainda pode acessar a mensagem assim:

try:
    # some code
except Exception as e:
   # some code
   print("Exception occurred: {}".format(e))
   
# Exception é a classe base para todas as exceções internas


####
# Convenientemente, o Python executará um loop sobre as linhas do 
# arquivo utilizando a sintaxe for line in file. Eu posso usar isso 
# para criar uma lista de linhas no arquivo. Como cada linha ainda
# tem o seu caractere de nova linha anexado, eu removo-o usando .strip().

camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)

###
# Utilizando um bloco principal
# Para evitar a execução de declarações executáveis de um script qu
# linhas em um bloco if __name__ == "__main__". Ou, alternativamente
# inclua-os em uma função chamada main() e utilize-a no bloco if main.

# Sempre que podemos executar um script como este, o Python na verdade
#  define uma variável interna especial chamada __name__ para qualquer
# módulo. Quando executamos um script, o Python reconhece este módulo
# como o programa principal e define a variável __name__ para este módulo
# para a string “__main__”. Para quaisquer módulos importados neste script,
# essa variável interna __name__ só é definida para o nome desse módulo.
# Portanto, a condição de if __name__ == "__main__" só está checando 
# se este módulo é o programa principal.

###
# A biblioteca padrão do Python tem vários módulos! Para ajudar você 
# a se familiarizar com o que está disponível, aqui está uma seleção 
# de nossos módulos favoritos da biblioteca padrão do Python e por 
# que os usamos!

# csv: muito conveniente para ler e gravar arquivos csv
# collections: extensões úteis dos tipos comuns de dados, incluindo 
# OrderedDict, defaultdict e namedtuple
# random: gera números pseudoaleatórios, mistura sequências 
# aleatoriamente e seleciona itens de maneira aleatória
# string: mais funções para strings. Este módulo também contém 
# coleções úteis de letras como string.digits (uma string que contém 
# todos os caracteres que são dígitos válidos).
#re: correspondência de padrões em strings através de expressões 
# regulares
# math: algumas funções matemáticas padrão
# os: interagindo com sistemas operacionais
# os.path: submódulo de os para alterar o nome de caminhos
# sys: trabalha diretamente com o interpretador do Python
# json: bom para ler e escrever arquivos json (bom para trabalhos na web)

# Use an import statement at the top

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)

def generate_password_2():
    return ''.join(random.sample(word_list,3))
	
# test your function
print(generate_password())

####
# Módulos, pacotes e nomes
# Para gerenciar melhor o código, os módulos da biblioteca padrão 
# do Python estão divididos em submódulos que estão contidos 
# dentro de um pacote. Um pacote é simplesmente um módulo que 
# contém submódulos. Um submódulo é especificado com a notação 
# habitual de ponto.

# Módulos que são submódulos são especificados pelo nome do pacote
# seguido pelo nome do submódulo separados por um ponto. Você pode 
# importar o submódulo assim.

import package_name.submodule_name

# Bibliotecas de terceiros

# Existem dezenas de milhares de bibliotecas de terceiros escritas 
# por desenvolvedores independentes! Você pode instalá-las usando o pip, 
# um gerenciador de pacotes que está incluso no Python 3. 
# O pip é o gerenciador de pacotes padrão para o Python, mas não é o 
# único. Uma alternativa popular é o Anaconda, que é projetado 
# especificamente para ciência de dados.

# Para instalar um pacote usando o pip, basta digitar "pip install" 
# seguido do nome do pacote em sua linha de comando, assim: 
# pip install package_name. Isso baixa e instala o pacote para 
# que ele esteja disponível para importação em seus programas. Uma 
# vez instalado, você pode importar pacotes de terceiros usando 
# a mesma sintaxe usada para importar da biblioteca padrão.

# Usando um arquivo requirements.txt
# Programas maiores em Python podem depender de dezenas de pacotes 
# de terceiros. Para facilitar o compartilhamento desses programas, 
# os programadores frequentemente listam as dependências do 
# projeto em um arquivo chamado requirements.txt. Este é um 
# exemplo de um arquivo requirements.txt.

# beautifulsoup4==4.5.1
# bs4==0.0.1
# pytz==2016.7
# requests==2.11.1
# Cada linha do arquivo inclui o nome de um pacote e seu número de versão. 
# O número de versão é opcional, mas geralmente é incluído. 
# Bibliotecas podem mudar sutilmente ou drasticamente entre as 
# versões, por isso, é importante usar as mesmas versões de 
# biblioteca que foram utilizadas para escrever o programa.

# Você pode usar o pip para instalar todas as dependências do 
# projeto ao mesmo tempo, digitando 
# pip install -r requirements.txt em sua linha de comando.

####
# Pacotes úteis de terceiros
# Ser capaz de instalar e importar bibliotecas de terceiros é útil, 
# mas, para ser um programador eficaz, você também precisa saber 
# quais bibliotecas estão disponíveis uso. As pessoas geralmente 
# aprendem sobre novas bibliotecas úteis por meio de recomendações 
# online ou de colegas. Se você for um programador novo em Python, 
# pode não ter muitos colegas, então, para começar, aqui está uma 
# lista de pacotes que são populares entre os engenheiros da Udacity.

# IPython - um interpretador interativo do Python.
# requests - fornece métodos fáceis de usar para fazer solicitações 
# na web. Útil para acessar APIs da web.
# Flask - uma estrutura leve para fazer aplicações web e APIs.
# Django - uma estrutura mais recheada de recursos para criar 
# aplicações web. O Django é particularmente bom para projetar 
# aplicações web complexas e com muito conteúdo.
# Beautiful Soup - usado para analisar HTML e extrair 
# informações a partir daí. Ótimo para web scraping.
# pytest - estende os módulos de assertivas internas e testes de 
# unidade (unittest) do Python.
# PyYAML - para ler e gravar arquivos YAML.
# NumPy - o pacote fundamental para a computação científica com 
# Python. Ele contém, entre outras coisas, um poderoso objeto 
# array N-dimensional e capacidades úteis para álgebra linear.
# pandas - uma biblioteca contendo ferramentas de alto desempenho, 
# para estruturas de dados e de análise de dados. O Pandas, 
# em especial, fornece dataframes!
# matplotlib - uma biblioteca de plotagem 2D que produz figuras 
# com qualidade de publicação em uma variedade de formatos em 
# papel e ambientes interativos.
# ggplot - outra biblioteca de plotagem 2D, com base na biblioteca 
# ggplot2 do software R.
# Pillow - a biblioteca de imagens do Python adiciona capacidades 
# de processamento de imagens a seu interpretador Python.
# pyglet - uma estrutura de aplicação multiplataforma voltada 
# ao desenvolvimento de jogos
# Pygame - um conjunto de módulos Python projetados para 
# escrever jogos.
# pytz - definições de fuso horário do mundo para Python

