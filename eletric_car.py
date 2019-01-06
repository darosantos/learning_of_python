import teste_car as tc


class ElectricCar(tc.Car):
    # """Representa aspectos específicos de veículos elétricos."""
    def __init__(self, make, model, year):
        # """Inicializa os atributos da classe-pai."""
        super().__init__(make, model, year)
        # """ Inicializa os atributos da classe pai Em seguida, inicializa
        # os atributos específicos de um carro elétrico """
        self.battery_size = 70

    def describe_battery(self):
        # """Exibe uma frase que descreve a capacidade da bateria."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self, qtd_gas=0):
        # """Carros elétricos não têm tanques de gasolina."""
        print("This car doesn't need a gas tank!")



# A primeira tarefa de Python ao criar uma instância de uma classe-filha é
# atribuir valores a todos os atributos da classe-pai. Para isso, o método
# __init__() de uma classe-filha precisa da ajuda de sua classe-pai.

# A função super() é uma função especial que ajuda Python a criar
# conexões entre a classe-pai e a classe-filha
# O nome super é derivado
# de uma convenção segundo a qual a classe-pai se chama superclasse e a
# classe-filha é a subclasse.

# Qualquer método da classe-pai que não se enquadre no que você estiver
# tentando modelar com a classe-filha pode ser sobrescrito. Para isso,
# defina um método na classe-filha com o mesmo nome do método da
# classe-pai que você deseja sobrescrever. Python desprezará o método da
# classe-pai e só prestará atenção no método definido na classe-filha.