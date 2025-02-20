import random
from kostka_do_gry import draw_die

class Die:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.value = 1

    def roll(self):
        """Roll the die to get a random value."""
        self.value = random.randint(1, 6)

    def draw(self, ekran):
        """Draw the die on the screen."""
        draw_die(ekran, self.x, self.y, self.size, self.value)