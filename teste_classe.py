# Na programação
# orientada a objetos, escrevemos classes que representam
# entidades e situações do mundo real, e criamos objetos
# com base nessas classes. Quando escrevemos uma classe,
# definimos o comportamento geral que toda uma
# categoria de objetos pode ter.
# Quando criamos objetos individuais a partir da classe, cada objeto será
# automaticamente equipado com o comportamento geral; então você
# poderá dar a cada objeto as características únicas que desejar.

# Criar um objeto a partir de uma classe é uma operação conhecida
# como instanciação, e trabalhamos com instâncias de uma classe.

import teste_dog as td
import teste_car as tc
import eletric_car as ec

my_dog = td.Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")


# Para acessar os atributos de uma instância utilize a notação de ponto.
# Em acessamos o valor do atributo name de my_dog escrevendo:
# my_dog.name

# Depois que criarmos uma instância da classe Dog, podemos usar a
# notação de ponto para chamar qualquer método definido nessa classe

# Você pode criar tantas instâncias de uma classe quantas forem
# necessárias, desde que dê a cada instância um nome de variável único
# ou que ela ocupe uma única posição em uma lista ou dicionário


my_new_car = tc.Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(50)
my_new_car.read_odometer()
my_new_car.update_odometer(23)


my_used_car = tc.Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

print("\n\n\n- Eletric Car")
my_tesla = ec.ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()

# 220