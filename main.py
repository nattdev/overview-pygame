import pygame
import sys

pygame.init()

SIZE_SCREEN = (800, 500);

# Creamos ventana
screen = pygame.display.set_mode(SIZE_SCREEN);

while True:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
