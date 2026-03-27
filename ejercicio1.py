import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejercicio 1 - Puntos - Graficación USM")

# Colores
#NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

corriendo = True

while corriendo:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # === Dibujar todo ===
    pantalla.fill((0, 0, 0))                    # Fondo negro (CORREGIDO)

    # Dibujar los puntos (círculos pequeños)
    pygame.draw.circle(pantalla, BLANCO, (200, 300), 5)
    pygame.draw.circle(pantalla, ROJO,   (600, 300), 8)
    pygame.draw.circle(pantalla, VERDE,  (450, 150), 6)
    pygame.draw.circle(pantalla, AZUL,   (400, 300), 3)
    pygame.draw.circle(pantalla, (255, 255, 0), (700, 500), 10)

    # Actualizar la pantalla (forma correcta)
    pygame.display.flip()

# Cerrar el programa correctamente
pygame.quit()
sys.exit()