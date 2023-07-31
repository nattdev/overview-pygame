import pygame
import sys

pygame.init()

SIZE_SCREEN = (800, 500);

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Creamos ventana
screen = pygame.display.set_mode(SIZE_SCREEN);

# Reloj - Controlar FPS
clock = pygame.time.Clock()

# Coord de Rect
coord_x = 400
coord_y = 200

# Velocidad
speed_x = 3
speed_y = 3


while True:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if (coord_x > 720 or coord_x < 0):
        speed_x *= -1

    if (coord_y > 420 or coord_y < 0):
        speed_y *= -1

    coord_x += speed_x
    coord_y += speed_y
    # Rellenar el color de fondo
    screen.fill(WHITE)
    ## Zona de dibujo --- ##
    ## Dibujos con for 

    for i in range (100, 700, 100): # (inicio, fin, incremento)
        pygame.draw.rect(screen, GREEN, (i, 230, 50, 50))

    pygame.draw.line(screen, GREEN, [0, 100], [0, 200], 10)
    # (Donde dibujar, color, [inicio], [final], grosor)
    pygame.draw.rect(screen, BLACK, (coord_x, coord_y, 80, 80))
    # (x, y, w, h)
   
    ## Fin de Zona de dibujo --- ##
    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)
