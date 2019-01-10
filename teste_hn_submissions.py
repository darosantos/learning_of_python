#
#
# Inicialmente fizemos a chamada de API e exibimos o status da resposta u.
# Essa chamada de API devolve uma lista contendo os IDs dos 500 artigos mais
# populares do Hacker News no momento em que a chamada foi feita. Então
# convertemos o texto da resposta em uma lista Python em v, que armazenamos
# em submission_ids. Usaremos esses IDs para criar um conjunto de dicionários
# em que cada um armazenará informações sobre um dos artigos submetidos.
# Criamos uma lista vazia chamada submission_dicts em w para
# armazenar esses dicionários. Então percorremos os IDs dos 30
# principais artigos submetidos com um laço. Fazemos uma nova
# chamada de API para cada artigo gerando um URL que inclui o valor
# atual de submission_id x. Exibimos o status de cada requisição para que
# possamos ver se ela foi bem-sucedida.
import requests
from operator import itemgetter

# Faz uma chamada de API e armazena a resposta
url = 'https://hackernews.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Em y criamos um dicionário para o artigo submetido processado no
# momento, no qual armazenamos o título do artigo e um link para a
# página de discussão desse item. Em z armazenamos o número de
# comentários no dicionário. Se um artigo ainda não teve nenhum
# comentário, a chave 'descendants' não estará presente. Quando você não
# tiver certeza de que uma chave existe em um dicionário, utilize o método
# dict.get(), que devolve o valor associado à chave especificada se ela
# existir, ou o valor que você fornecer se ela não existir (0 nesse exemplo).
# Por fim, concatenamos cada submission_dict à lista submission_dicts
# Processa informações sobre cada artigo submetido
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Cria uma chamada de API separada para cada artigo submetido
    url = ('https://hackernews.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()
    submission_dict = {'title': response_dict['title'], 'link': 'http://news.ycombinator.com/item?id=' + str(submission_id), 'comments': response_dict.get('descendants', 0) }
    submission_dicts.append(submission_dict)
    # Queremos ordenar a lista de dicionários de
    # acordo com o número de comentários. Para isso, usamos uma função
    # chamada itemgetter() {, proveniente do módulo operator. Passamos a
    # chave 'comments' a essa função e ela extrai o valor associado a essa chave
    # de cada dicionário da lista. A função sorted() então utiliza esse valor
    # como base para ordenar a lista. Ordenamos a lista na ordem inversa para colocar
    # as histórias mais comentadas antes.
    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])