# Recebendo entrada do usuário

idade = 0
ano = 0

idade = input('Qual sua idade hoje? ')
ano = input('Em que ano estamos? ')

idade = int(idade)
ano = int(ano)

ano_nasc = ano - idade

print('Você nasce eim: ' + str(ano_nasc))

if idade >= 18:
    print('Já vai pode ir preso!')
