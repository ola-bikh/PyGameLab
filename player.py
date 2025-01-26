import pygame

class Player:
    def __init__(self, color, start_pos, path_y):
        self.color = color
        self.position = start_pos
        self.path_y = path_y

    def move(self, steps, board_size):
        """Move the player by the specified number of steps."""
        self.position += steps
          # Keep within board limits

    def draw(self, ekran, cell_width):
        """Draw the player on the board."""
        x = self.position * cell_width + cell_width // 2
        y = self.path_y + 25
        pygame.draw.circle(ekran, self.color, (x, y), 15)