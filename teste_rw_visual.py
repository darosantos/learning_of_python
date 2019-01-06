# Testa os passos aleatórios

import matplotlib.pyplot as plt

from teste_randomwalk import RandomWalk


# Cria um passeio aleatório e plota os pontos
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.axis([-200, 200, -200, 200])
plt.show()
