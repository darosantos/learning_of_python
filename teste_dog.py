class Dog:
    # """Uma tentativa simples de modelar um cachorro."""
    def __init__(self, name, age):
        # """Inicializa os atributos name e age."""
        self.name = name
        self.age = age

    def sit(self):
        # """Simula um cachorro sentando em resposta a um comando."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        # """Simula um cachorro rolando em resposta a um comando."""
        print(self.name.title() + " rolled over!")


# Por convenção, nomes com a primeira letra maiúscula referem-se a classes em Python. Os parênteses na
# definição da classe estão vazios porque estamos criando essa classe do zero


# O método __init__() em é um método especial que Python
# executa automaticamente sempre que criamos uma nova instância
# baseada na classe

# O parâmetro self é obrigatório na definição do método e deve
# estar antes dos demais parâmetros. Deve estar incluído na definição,
# pois, quando Python chama esse método __init__() depois (para criar
# uma instância de Dog), a chamada do método passará o argumento self
# automaticamente. Toda chamada de método associada a uma classe
# passa self, que é uma referência à própria instância, de modo
# automático; ele dá acesso aos atributos e métodos da classe à instância
# individual. Quando

# Qualquer variável
# prefixada com self está disponível a todos os métodos da classe; além
# disso, podemos acessar essas variáveis por meio de qualquer instância
# criada a partir da classe. self.name = name usa o valor armazenado no
# parâmetro name e o armazena na variável name, que é então associada à
# instância criada. O mesmo processo ocorre com self.age = age. Variáveis
# como essas, acessíveis por meio de instâncias, são chamadas de
# atributos.

# método __init__() cria uma instância que representa esse cachorro em
# particular e define os atributos name e age com os valores que fornecemos.
# Esse método não tem uma instrução return explícita, mas Python devolve
# automaticamente uma instância que representa esse cachorro


# Podemos modificar os atributos de uma
# instância diretamente, ou escrever métodos que atualizem os atributos
# de formas específicas.

# Todo atributo de uma classe precisa de um valor inicial, mesmo que esse
# valor seja 0 ou uma string vazia. Em alguns casos, por exemplo, quando
# definimos um valor default, faz sentido especificar esse valor inicial no
# corpo do método __init__(); se isso for feito para um atributo, você não
# precisará incluir um parâmetro para ele.

# Você pode alterar o valor de um atributo de três maneiras: podemos
# modificar o valor diretamente por meio de uma instância, definir o valor
# com um método ou incrementá-lo (somar um determinado valor a ele).

# Se a classe que você estiver escrevendo for uma versão especializada de
# outra classe já criada, a herança poderá ser usada. Quando uma classe
# herda de outra, ela assumirá automaticamente todos os atributos e
# métodos da primeira classe. A classe original se chama classe-pai e a nova
# classe é a classe-filha. A classe-filha herda todos os atributos e método de
# sua classe-pai, mas também é livre para definir novos atributos e
# métodos próprios.

