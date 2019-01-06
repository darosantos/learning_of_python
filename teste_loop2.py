listaClientes = []
while True:
    cadastrar = input('Deseja inserir um novo cliente S/N: ').upper()
    if cadastrar == 'N':
        break
    else:
        nome = input('Qual o nome do cliente: ')
        sobrenome = input('Qual o sobrenome do cliente: ')
        email = input('Qual o e-mail do cliente: ')
        telefone = input('Qual o telefone do cliente: ')
        confirma = input('Confirma o cadastro do cliente S/N ').upper()
        if confirma == 'N':
            continue
        else:
            new_cliente = {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'telefone': telefone}
            listaClientes.append(new_cliente)

print(listaClientes)