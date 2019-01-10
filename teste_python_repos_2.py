#
#
#
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

# Em u
# criamos uma instância chamada my_config da classe Config do Pygal;
# modificar os atributos de my_config personalizará a aparência do gráfico.
# Definimos os dois atributos x_label_rotation e show_legend v,
# originalmente passados como argumentos nomeados quando criamos uma
# instância de Bar. Em w definimos o tamanho da fonte para o título do
# gráfico e para os rótulos menores e maiores. Os rótulos menores nesse
# gráfico são os nomes dos projetos ao longo do eixo x e a maior parte dos
# números no eixo y. Os rótulos maiores são apenas os rótulos do eixo y que
# marcam incrementos de 5.000 estrelas. Esses rótulos serão maiores, e é
# por isso que os diferenciamos. Em x usamos truncate_label para reduzir
# os nomes de projeto mais longos a 15 caracteres. (Quando você passar o
# mouse sobre um nome de projeto truncado na tela, o nome completo
# aparecerá.) Em seguida, ocultamos as linhas horizontais do gráfico
# definindo show_y_guides com False y. Por fim, em z, definimos uma
# largura personalizada para que o gráfico use mais do espaço disponível no
# navegador.
#
# Cria a visualização
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')