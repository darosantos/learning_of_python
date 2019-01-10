#
#
# Começamos
# importando o pygal e os estilos do Pygal de que precisaremos para o
# gráfico. Continuamos exibindo o status da resposta da chamada à API e o
# número total de repositórios encontrados para que possamos saber caso haja
# algum problema com a chamada da API. Não exibimos mais as informações sobre
# os projetos específicos devolvidos, pois elas serão incluídas na
# visualização.
#
# Em u criamos duas listas vazias para armazenar os dados que
# incluiremos no gráfico. Precisaremos do nome de cada projeto para
# rotular as barras e do número de estrelas para determinar a altura delas.
# No laço, concatenamos nessas listas o nome de cada projeto e o número
# de estrelas que ele tem v.
# Em seguida, definimos um estilo usando a classe LightenStyle (alias LS)
# e usamos um tom de azul-escuro como base w. Também passamos o
# argumento base_style para utilizar a classe LightColorizedStyle (alias LCS).
# Então usamos Bar() para criar um gráfico de barras simples e lhe
# passamos my_style x. Além disso, passamos outros dois argumentos de
# estilo: definimos a rotação dos nomes ao longo do eixo x em 45 graus
# (x_label_rotation=45) e ocultamos a legenda, pois estamos plotando
# apenas uma série no gráfico (show_legend=False). Então fornecemos um
# título ao gráfico e definimos o atributo x_labels com a lista names.
#
# Como não é necessário nomear essa série de dados, passamos uma
# string vazia para o rótulo quando adicionamos os dados

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# Faz uma chamada de API e armazena a resposta
URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'
r = requests.get(URL)
print("Status code:", r.status_code)
# Armazena a resposta da API em uma variável
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])
# Explora informações sobre os repositórios
repo_dicts = response_dict['items']

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Cria a visualização
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')

