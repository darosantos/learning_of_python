# Testa os passos aleatórios

import matplotlib.pyplot as plt

from teste_randomwalk import RandomWalk


# Continua criando novos passeios enquanto o programa estiver ativo
# Esse código gera um passeio aleatório, exibe esse passeio no
# visualizador do matplotlib e faz uma pausa com o visualizador aberto.
# Quando você o fechar, uma pergunta será feita para saber se você quer gerar
# outro passeio. Responda y e você poderá gerar passeios que permaneçam
# próximos ao ponto de partida, que se afastam em uma direção principal, que
# têm seções mais finas conectadas a grupos maiores de pontos, e assim por
# diante. Quando quiser encerrar o programa, digite n.
while True:
    # Cria um passeio aleatório e plota os pontos
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
