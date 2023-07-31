import pygame
import sys
import random

pygame.init()

SIZE_SCREEN = (800, 500);

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (250, 0, 0)
BLUE = (0, 0, 255)

# Creamos ventana
screen = pygame.display.set_mode(SIZE_SCREEN);

# Reloj - Controlar FPS
clock = pygame.time.Clock()

# Visibilidad de mouse
pygame.mouse.set_visible(0)


# Coord de Rect
coord_x = 400
coord_y = 200

# Velocidad
speed_x = 3
speed_y = 3

coord_list = []

# Coord Circulos
for i in range (60) :
    x = random.randint(0, 800)
    y = random.randint(0, 500)
    coord_list.append( [x, y] )

while True:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            sys.exit()
    if (coord_x > 720 or coord_x < 0):
        speed_x *= -1

    if (coord_y > 420 or coord_y < 0):
        speed_y *= -1

    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]
    print(mouse_pos)

    coord_x += speed_x
    coord_y += speed_y
    # Rellenar el color de fondo
    screen.fill(WHITE)
    ## Zona de dibujo --- ##
    ## Dibujos con for 

    pygame.draw.circle(screen, BLUE, (x, y), 20)

        ## Dibujando circulos aleatorios
    for j in coord_list :
        x = j[0]
        y = j[1]
        pygame.draw.circle(screen, RED, (x, y), 2)
        j[1] += 1
        if j[1] > 500:
            j[1] = 0

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
