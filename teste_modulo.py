# Armazenar suas funções em um arquivo separado permite ocultar os
# detalhes do código de seu programa e se concentrar na lógica de nível
# mais alto. Também permite reutilizar funções em muitos programas
# diferentes. Quando armazenamos funções em arquivos separados,
# podemos compartilhar esses arquivos com outros programadores sem a
# necessidade de compartilhar o programa todo. Saber como importar
# funções também possibilita usar bibliotecas de funções que outros
# programadores escreveram.


import teste_function


teste_function.make_pizza('tomate seco', 'orégano extra', 'ovo cozido')


# Quando Python lê esse arquivo, a linha import lhe diz para abrir o arquivo e copiar todas as
# funções dele para esse programa. Você não vê realmente o código sendo
# copiado entre os arquivos porque Python faz isso internamente, à medida que o programa executa.

# Podemos também importar uma função específica de um módulo. Eis a
# sintaxe geral para essa abordagem: from nome_do_módulo import
# nome_da_função Você pode importar quantas funções quiser de um
# módulo separando o nome de cada função com uma vírgula


from teste_function2 import show_confirm_dialog


# Com essa sintaxe não precisamos usar a notação de ponto ao chamar uma função.
# Como importamos explicitamente a função a instrução import, podemos chamá-la pelo nome quando ela
# for utilizada.


show_confirm_dialog('Deseja continuar: ')


# Se o nome de uma função que você importar puder entrar em conflito
# com um nome existente em seu programa ou se o nome da função for
# longo, podemos usar um alias único e conciso, que é um nome
# alternativo, semelhante a um apelido para a função


from teste_function3 import show_confirm_dialog as scd


scd('Pq parar? ')


# Também podemos fornecer um alias para um nome de módulo. Dar um alias conciso a um módulo,
# por exemplo, p para pizza, permite chamar mais rapidamente as funções do módulo.

# A sintaxe geral para essa abordagem é: import nome_do_módulo as nm


import teste_function4 as tf


tf.show_confirm_dialog2('Seu nome é Danilo: ')


# Podemos dizer a Python para importar todas as funções de um módulo
# usando o operador asterisco (*): from pizza import *

# Como todas as funções são importadas, podemos chamar qualquer função pelo
# nome, sem usar a notação de ponto. No entanto, é melhor não usar essa
# abordagem quando trabalhar com módulos maiores, que não foram escritos
# por você: se o módulo tiver um nome de função que seja igual a um nome
# existente em seu projeto, você poderá ter alguns resultados inesperados.
# Python poderá ver várias funções ou variáveis com o mesmo nome e, em vez
# de importar todas as funções separadamente, ele as sobrescreverá.


from teste_function5 import *

show_confirm_dialog5('Vamos continuar: ')


# A melhor abordagem é importar a função ou as funções que você
# quiser ou importar o módulo todo e usar a notação de ponto. Isso
# resulta em um código claro, mais fácil de ler e de entender.