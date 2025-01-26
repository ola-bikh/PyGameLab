import pygame

class Board:
    def __init__(self, size, width, height):
        self.size = size
        self.cell_width = width // size
        self.width = width
        self.height = height

    def draw(self, ekran):
        """Draw the board grid."""
        for i in range(self.size):
            pygame.draw.rect(ekran, (0, 0, 0), (i * self.cell_width, self.height // 3, self.cell_width, 50), 1)
            pygame.draw.rect(ekran, (0, 0, 0), (i * self.cell_width, (self.height // 3) * 2, self.cell_width, 50), 1)