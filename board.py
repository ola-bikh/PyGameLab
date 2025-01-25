import pygame

# Kolory
BIALY = (255, 255, 255)
CZARNY = (0, 0, 0)
CZERWONY = (255, 0, 0)
NIEBIESKI = (0, 0, 255)

class Board:
    def __init__(self, size, width, height):
        self.size = size
        self.cell_width = width // size
        self.width = width
        self.height = height

    def draw(self, ekran):
        for i in range(self.size):
            # Górna ścieżka
            pygame.draw.rect(ekran, CZARNY, (i * self.cell_width, self.height // 3, self.cell_width, 50), 1)
            # Dolna ścieżka
            pygame.draw.rect(ekran, CZARNY, (i * self.cell_width, (self.height // 3) * 2, self.cell_width, 50), 1)

