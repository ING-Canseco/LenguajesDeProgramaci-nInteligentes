import math
import pygame
import numpy as np  # Añadido para matrices de transformación

class Agente:
    def __init__(self, x, y, tamano, angulo=30):
        """
        Inicializa el agente con posición (x, y), tamaño y ángulo inicial diferente de 0.
        """
        self.x = x
        self.y = y
        self.tamano = tamano
        self.angulo = angulo  # en grados

    def dibujar(self, screen, color_base=(0, 180, 0), color_frente=(255, 50, 50)):
        """
        Dibuja el triángulo rotado alrededor de su centro usando matrices NumPy (Sesión 4).
        - Cuerpo en color_base (verde oscuro)
        - Círculo rojo en el vértice frontal para indicar dirección de movimiento
        """
        # Vértices locales (triángulo simétrico apuntando "arriba" en reposo)
        vertices_locales = np.array([
            [0, -self.tamano],                     # frente (punta, dirección del agente)
            [-self.tamano / 2, self.tamano / 2],   # izquierda
            [self.tamano / 2, self.tamano / 2]     # derecha
        ])

        
        # Matriz de rotación
        
        rad = math.radians(self.angulo)
        rot_matrix = np.array([
            [math.cos(rad), -math.sin(rad)],
            [math.sin(rad), math.cos(rad)]
        ])
        vertices_rotados = np.dot(vertices_locales, rot_matrix)  # Aplica rotación

        
        # Traslación (posición global)
        
        translacion = np.array([self.x, self.y])
        vertices = vertices_rotados + translacion  # Aplica traslación

        # Dibujar triángulo relleno
        pygame.draw.polygon(screen, color_base, vertices)
        # Borde blanco
        pygame.draw.polygon(screen, (255, 255, 255), vertices, width=3)
        
        # Círculo rojo en el frente (vértice 0: punta que indica la dirección)
        fx, fy = vertices[0]
        pygame.draw.circle(screen, color_frente, (int(fx), int(fy)), 10)