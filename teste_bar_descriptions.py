#
#
# No Pygal, passar o cursor sobre uma barra individual faz com que as
# informações representadas pela barra sejam exibidas. Elas são
# comumente chamadas de dicas de contexto (tooltips) e, nesse caso,
# mostram o número de estrelas que um projeto tem. Criaremos uma dica
# de contexto personalizada que mostre também a descrição de cada
# projeto.

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Em u definimos uma lista chamada plot_dicts, que contém três dicionários:
# um para o projeto HTTPie, um para o projeto Django e outro para o Flask.
# Cada dicionário tem duas chaves: 'value' e 'label'. O Pygal usa o número
# associado a 'value' para descobrir a altura que cada barra deve ter, e
# utiliza a string associada a 'label' para criar a dica de contexto de cada
# barra. Por exemplo, o primeiro dicionário em v criará uma barra que
# representa um projeto com 16.101 estrelas, e sua dica de contexto conterá
# Description of httpie (Descrição de httpie).
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']
plot_dicts = [ {'value': 16101, 'label': 'Description of httpie.'}, {'value': 15028,
'label': 'Description of django.'}, {'value': 14798, 'label': 'Description of flask.'}, ]

# O método add() precisa de uma string e de uma lista. Quando
# chamamos esse método, passamos a lista de dicionários que representa
# as barras (plot_dicts)
chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions_2.svg')