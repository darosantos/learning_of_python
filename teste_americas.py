#
#
#

from pygal_maps_world import maps as pgm

# Em u criamos uma instância da classe
# Worldmap e definimos o atributo title do mapa. Em v usamos o método add(),
# que aceita um rótulo e uma lista de códigos de países que queremos
# destacar. Cada chamada a add() define uma nova cor para o conjunto de
# países e acrescenta essa cor a uma legenda à esquerda da imagem, com o
# rótulo especificado nessa chamada. Queremos que toda a região da América do
# Norte seja representada com uma cor, portanto colocamos 'ca', 'mx' e 'us'
# na lista que passamos para a primeira chamada a add() a fim de dar destaque
# ao Canadá, ao México e aos Estados Unidos em conjunto. Então fizemos o
# mesmo para os países da América Central e da América do Sul.

wm = pgm.World()
wm.title = 'North, Central, and South America'
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.render_to_file('americas.svg')