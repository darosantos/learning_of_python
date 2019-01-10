#
#
#

from pygal_maps_world import maps as pgm


# Inicialmente crie uma instância
# de Worldmap e defina um título. Então utilize o método add(), mas desta
# vez passe um dicionário como segundo argumento em vez de passar uma lista
# u. O dicionário contém os códigos de duas letras do Pygal para os países
# como chaves e as populações como valores. O Pygal utiliza automaticamente
# esses números para sombrear os países, variando da cor mais clara (menos
# populosos) para a cor mais escura (mais populosos)
wm = pgm.World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.render_to_file('na_populations.svg')