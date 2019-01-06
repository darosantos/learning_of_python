# Para escrever um texto em um arquivo, chame open() com um segundo
# argumento que diga a Python que você quer escrever dados no arquivo

import time as lib_tm

coded_time = str(lib_tm.localtime().tm_hour) + '_' + str(lib_tm.localtime().tm_min) + '_' + str(lib_tm.localtime().tm_sec)
filename = 'programming' + coded_time + '.txt'
with open(filename, 'w') as file_object:
    msg = lib_tm.asctime() + "\t I love programming."
    file_object.write(msg)


# A chamada a open() nesse exemplo tem dois argumentos. O
# primeiro argumento ainda é o nome do arquivo que queremos abrir. O segundo
# argumento, 'w', diz a Python que queremos abrir o arquivo em modo de
# escrita. Podemos abrir um arquivo em modo de leitura ('r'), em modo de
# escrita ('w'), em modo de concatenação ('a') ou em um modo que permita ler
# e escrever no arquivo ('r+'). Se o argumento de modo for omitido, por
# padrão Python abrirá o arquivo em modo somente de leitura.

# Python escreve apenas strings em um arquivo-texto. Se quiser
# armazenar dados numéricos em um arquivo-texto, será necessário
# converter os dados em um formato de string antes usando a função
# str()

# tome cuidado ao abrir
# um arquivo em modo de escrita ('w') porque se o arquivo já existir,
# Python o apagará antes de devolver o objeto arquivo

# A função write() não acrescenta nenhuma quebra de linha ao texto que
# você escrever. Portanto, se escrever mais de uma linha sem incluir
# caracteres de quebra de linha, seu arquivo poderá não ter a aparência
# desejada

