import sys

import pygame
print('Você iniciou o jogo!')
pygame.init()

window = pygame.display.set_mode(size=(800, 600))
print('Você Finalizou o jogo!')

while True:
    pygame.event.get()
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # close window - fechar a janela
            quit() #finalizar o jogo
