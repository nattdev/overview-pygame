import pygame
import sys

pygame.init()

SIZE_SCREEN = (800, 500);

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Creamos ventana
screen = pygame.display.set_mode(SIZE_SCREEN);

while True:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    # Rellenar el color de fondo
    screen.fill(WHITE)
    ## Zona de dibujo
    pygame.draw.line(screen, GREEN, [0, 100], [0, 200], 10)
    # (Donde dibujar, color, [inicio], [final], grosor)
    pygame.draw.rect(screen, BLACK, (100, 100, 80, 80))
    # (x, y, w, h)
   
    # Actualizar pantalla
    pygame.display.flip()
