#
#
# Inicialmente importe o pygal.
# Em u criamos um dicionário vazio para armazenar os códigos dos países e
# as populações no formato esperado pelo Pygal. Em v construímos o
# dicionário cc_populations usando o código do país como chave e a
# população como valor sempre que um código é devolvido. Criamos
# uma instância de Worldmap e definimos seu atributo title w.
# Quando chamamos add(), passamos o dicionário com os códigos dos
# países e as populações para esse método

import json

from pygal_maps_world import maps as pgm
from pygal_maps_world import i18n

def get_country_code(country_name):
    """Devolve o código de duas letras do Pygal para um país, dado o seu nome."""
    for code, name in i18n.COUNTRIES.items():
        if name == country_name:
            return code
       # Se o país não foi encontrado, devolve None
        return None

# Carrega os dados em uma lista
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
    # Constrói um dicionário com dados das populações
    cc_populations = {}
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country)
            if code:
                cc_populations[code] = population
    # Agrupa os países em três níveis populacionais
    cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
    for cc, pop in cc_populations.items():
        if pop < 10000000:
            cc_pops_1[cc] = pop
        elif pop < 1000000000:
            cc_pops_2[cc] = pop
        else:
            cc_pops_3[cc] = pop
        # Vê quantos países estão em cada nível
        print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

    print(cc_populations)
    wm = pgm.World()
    wm.title = 'World Population in 2010, by Country'
    wm.add('0-10m', cc_pops_1)
    wm.add('10m-1bn', cc_pops_2)
    wm.add('>1bn', cc_pops_3)
    wm.render_to_file('world_population2.svg')
