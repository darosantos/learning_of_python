#
#
#
import json

from pygal_maps_world import i18n

#  Antes de podermos nos concentrar no mapeamento, devemos tratar um
# último aspecto dos dados. A ferramenta de mapeamento do Pygal espera
# dados em um formato particular: os países devem ser fornecidos na
# forma de códigos e as populações como valores. Vários conjuntos
# padronizados de códigos de países são usados com frequência quando
# trabalhamos com dados geopolíticos; os códigos incluídos em
# population_data.json são códigos de três letras, mas o Pygal utiliza
# códigos de duas letras. Precisamos de uma maneira de descobrir o
# código de duas letras a partir do nome do país.
# Os códigos dos países no Pygal estão armazenados em um módulo
# chamado i18n, que é uma abreviatura para internationalization
# (internacionalização). O dicionário COUNTRIES contém os códigos de duas
# letras dos países como chaves e os nomes dos países como valores. Para
# ver esses códigos, importe o dicionário do módulo i18n e exiba suas
# chaves e valores

# No laço for, dizemos a Python para colocar as chaves em ordem alfabética
# Então exibimos o código de cada país e o nome associado a ele
#
# for country_code in sorted(i18n.COUNTRIES.keys()):
#    print(country_code, i18n.COUNTRIES[country_code])

#
# Passamos o nome do
# país para get_country_code() e o armazenamos no parâmetro country_name
# u. Em seguida, percorremos os pares de código-nome do país em COUNTRIES
# com um laço v. Se o nome do país for encontrado, o código desse país
# será devolvido w. Adicionamos uma linha depois do laço para devolver
# None se o nome do país não for encontrado x. Por fim, passamos os nomes
# de três países para conferir se a função está correta. Como esperado, o
# programa mostra os códigos de duas letras para três países
# def get_country_code(country_name):
#    """Devolve o código de duas letras do Pygal para um país, dado o seu nome."""
#    for code, name in i18n.COUNTRIES.items():
#        if name == country_name:
#            return code
#        # Se o país não foi encontrado, devolve None
#        return None
#
# print(get_country_code('Andorra'))
# print(get_country_code('United Arab Emirates'))
# print(get_country_code('Afghanistan'))

def get_country_code(country_name):
    """Devolve o código de duas letras do Pygal para um país, dado o seu nome."""
    for code, name in i18n.COUNTRIES.items():
        if name == country_name:
            return code
       # Se o país não foi encontrado, devolve None
        return None

# Inicialmente importamos o
# módulo json para que seja possível carregar os dados do arquivo de forma
# apropriada e, em seguida, armazenamos esses dados em pop_data em u. A
# função json.load() converte os dados em um formato com que Python possa
# trabalhar: nesse caso, em uma lista. Em v percorremos cada item de
# pop_data com um laço. Cada item é um dicionário com quatro pares chavevalor,
# e o armazenamos em pop_dict
#
# Carrega os dados em uma lista
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
    # Exibe a população de cada país em 2010
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            # population = pop_dict['Value']
            # print(country_name + ": " + population)
            # Todas as chaves e valores em population_data.json estão armazenados
            # como strings. Para trabalhar com os dados referentes às populações,
            # devemos converter as strings com as populações em valores numéricos.
            # Agora armazenamos o valor de cada população em um formato
            # numérico em u. Quando exibimos o valor da população, devemos convertê-lo
            # para uma string em v.
            # A função float() transforma a string em um decimal, e a
            # função int() remove a parte decimal do número e devolve um inteiro.
            population = int(float(pop_dict['Value']))
            # Depois de
            # extrair o nome do país e a população, armazenamos o código desse país em
            # code, ou None se nenhum código estiver disponível u. Se um código for
            # devolvido, o código e a população do país serão exibidos v. Se o código
            # não estiver disponível, exibimos uma mensagem de erro com o nome do país
            # cujo código não encontramos
            code = get_country_code(country_name)
            if code:
                print(code + ": " + str(population))
            else:
                print('ERROR - ' + country_name)