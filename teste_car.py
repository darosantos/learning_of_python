class Car():
    # """Uma tentativa simples de representar um carro."""
    def __init__(self, make, model, year):
        # """Inicializa os atributos que descrevem um carro."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 100

    def get_descriptive_name(self):
        # """Devolve um nome descritivo, formatado de modo elegante."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        # """Exibe uma frase que mostra a milhagem docarro."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        # """Define o valor de leitura do hodômetro com o valor especificado Rejeita
        # a alteração se for tentativa de definir um valor menor para o hodômetro""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        # """Soma a quantidade especificada ao valor de leitura do hodômetro."""
        self.odometer_reading += miles

    def fill_gas_tank(self, qtd_gas=0):
        if qtd_gas < 0:
            print('Not value negative')
        elif qtd == 0:
            print('Empty gasoline')
        else:
            if self.gas_tank == 100:
                print('Full tank')
            else:
                empty_tank = 100 - self.gas_tank
                if empty_tank >= qtd_gas:
                    self.gas_tank = self.gas_tank + qtd_gas
                else:
                    diff_gas = (self.gas_tank + qtd_gas) - 100
                    self.gas_tank = 100
                    print('Full tank, diff gas = ' + str(diff_gas))


# Quando atingir esse ponto,
# você perceberá que, muitas vezes, não há abordagens certas ou erradas
# para modelar situações do mundo real. Algumas abordagens são mais
# eficientes que outras, mas descobrir as representações mais eficientes
# exige prática.

# Importe várias classes de um módulo
# separando cada classe com uma vírgula. Depois que importar as classes de
# que precisará, você poderá criar quantas instâncias de cada classe quantas
# forem necessárias.