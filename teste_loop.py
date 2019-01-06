# Loop While

i = 0
fator = 3
while i <= 10:
    mult = fator * i
    msg = str(fator) + ' x ' + str(i) + " = \t" + str(mult)
    print(msg)
    i = i+1

# Utilizando laços para remover valores duplicados de uma lista
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)