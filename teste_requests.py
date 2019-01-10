#
#
#
# O pacote requests permite que um programa Python solicite facilmente
# informações a um site e analise a resposta devol

import requests

# Em u importamos o
# módulo requests. Em v armazenamos o URL da chamada da API e então usamos
# requests para fazer a chamada w. Chamamos get(), passamos o URL e
# armazenamos o objeto com a resposta na variável r. O objeto com a
# resposta tem um atributo chamado status_code, que nos informa se a
# requisição foi bem-sucedida. (Um código de status igual a 200 indica
# sucesso na resposta.) Em x exibimos o valor de status_code para garantir
# que a chamada foi realizada com sucesso.
#
# Faz uma chamada de API e armazena a resposta
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
# Como o código
# de status é 200, sabemos que a requisição teve sucesso.
#
print("Status code:", r.status_code)
# A API devolve as informações em formato JSON, portanto usamos o
# método json() y para convertê-las em um dicionário Python.
# Armazenamos o dicionário resultante em response_dict.
#
# Armazena a resposta da API em uma variável
response_dict = r.json()
# Processa o resultado
print(response_dict.keys())
print("Total repositories:", response_dict['total_count'])
# Explora informações sobre os repositórios
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))
# Analisa o primeiro repositório
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
print("\nSelected information about first repository:")
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])
print('Description:', repo_dict['description'])

#
# Exibimos uma mensagem introdutória em u. Em v
# percorremos todos os dicionários em repo_dicts com um laço. Nesse laço
# exibimos o nome de cada projeto, o seu proprietário, quantas estrelas o
# projeto recebeu, seu URL no GitHub e a sua descrição
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])