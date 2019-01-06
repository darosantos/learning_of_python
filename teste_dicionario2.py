# Código a seguir cria uma lista com três alienígenas: aliens.py

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# No exemplo a seguir, usamos range() para criar uma frota de 30 alienígenas: # Cria uma lista
# vazia para armazenar alienígenas aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# Mostra os 5 primeiros alienígenas
for alien in aliens[:5]:
    print(alien)
    print("...")
# Mostra quantos alienígenas foram criados
print("Total number of aliens: " + str(len(aliens)))