import math
import pygame
from agente import Agente

# Inicialización
pygame.init()
ANCHO = 800
ALTO = 600
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Agente Móvil - Rotación y Traslación con Matrices")
clock = pygame.time.Clock()

# Crear agente
agente = Agente(400, 300, 60, angulo=30)

# Constantes
VELOCIDAD_MOVIMIENTO = 5.0
VELOCIDAD_ROTACION = 4.0  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Movimiento
    dx = 0
    dy = 0
    moving = False

    rad = math.radians(agente.angulo)

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        dx = VELOCIDAD_MOVIMIENTO * math.cos(rad)
        dy = -VELOCIDAD_MOVIMIENTO * math.sin(rad)
        moving = True

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        dx = -VELOCIDAD_MOVIMIENTO * math.cos(rad)
        dy = VELOCIDAD_MOVIMIENTO * math.sin(rad)
        moving = True

    if moving:
        agente.x += dx
        agente.y += dy

    # Rotación
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        agente.angulo += VELOCIDAD_ROTACION

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        agente.angulo -= VELOCIDAD_ROTACION

    # Rebote en bordes
    margen = agente.tamano * 1.1

    if agente.x < margen:
        agente.x = margen
        agente.angulo = 180 - agente.angulo

    if agente.x > ANCHO - margen:
        agente.x = ANCHO - margen
        agente.angulo = 180 - agente.angulo

    if agente.y < margen:
        agente.y = margen
        agente.angulo = -agente.angulo

    if agente.y > ALTO - margen:
        agente.y = ALTO - margen
        agente.angulo = -agente.angulo

    agente.angulo %= 360

    # Dibujar
    screen.fill((0, 0, 0))
    agente.dibujar(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()