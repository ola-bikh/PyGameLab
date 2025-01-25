import pygame

class Player:
    def __init__(self, color, start_pos, path_y):
        self.color = color
        self.position = start_pos
        self.path_y = path_y

    def move(self, steps, board_size):
        self.position += steps
        self.position = min(self.position, board_size - 1)

    def draw(self, ekran, cell_width):
        x = self.position * cell_width + cell_width // 2
        y = self.path_y + 25
        pygame.draw.circle(ekran, self.color, (x, y), 15)

