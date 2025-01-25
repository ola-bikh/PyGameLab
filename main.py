import pygame
import random
from kostka_do_gry import draw_die
from simple_popup import show_simple_popup

# Kolory
BIALY = (255, 255, 255)
CZARNY = (0, 0, 0)
CZERWONY = (255, 0, 0)
NIEBIESKI = (0, 0, 255)



class Die:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.value = 1

    def roll(self):
        self.value = random.randint(1, 6)

    def draw(self, ekran):
        draw_die(ekran, self.x, self.y, self.size, self.value)


class Game:
    def __init__(self):
        pygame.init()
        self.SZEROKOSC, self.WYSOKOSC = 800, 600
        self.ekran = pygame.display.set_mode((self.SZEROKOSC, self.WYSOKOSC))
        pygame.display.set_caption("Gra planszowa Aleksandry Bikhit")
        self.clock = pygame.time.Clock()

        # Obiekty gry
        self.board = Board(20, self.SZEROKOSC, self.WYSOKOSC)
        self.players = [
            Player(CZERWONY, 0, self.WYSOKOSC // 3),
            Player(NIEBIESKI, 0, (self.WYSOKOSC // 3) * 2)
        ]
        self.die = Die(650, 50, 50)
        self.current_player = 0
        self.font = pygame.font.Font(None, 36)

    def display_turn(self):
        tekst_gracza = f"Tura Gracza {self.current_player + 1} (Naciśnij SPACJĘ, aby rzucić)"
        powierzchnia_tekstu = self.font.render(tekst_gracza, True, CZARNY)
        self.ekran.blit(powierzchnia_tekstu, (50, 20))

    def check_winner(self):
        if self.players[self.current_player].position >= self.board.size:
            tekst_zwyciezcy = f"Gracz {self.current_player + 1} wygrał!"
            wynik = show_simple_popup(self.ekran, tekst_zwyciezcy)
            if wynik == "exit":
                return True  # Wyjście z gry
            else:
                self.reset_game()
        return False

    def reset_game(self):
        for player in self.players:
            player.position = 0
        self.current_player = 0

    def run(self):
        running = True
        while running:
            self.ekran.fill(BIALY)
            self.board.draw(self.ekran)
            for player in self.players:
                player.draw(self.ekran, self.board.cell_width)
            self.die.draw(self.ekran)
            self.display_turn()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.die.roll()
                    print(f"Gracz {self.current_player + 1} wylosował {self.die.value}")
                    self.players[self.current_player].move(self.die.value, self.board.size)

                    if self.check_winner():
                        running = False
                        break

                    # Zmiana gracza
                    self.current_player = 1 - self.current_player

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()


if __name__ == "__main__":
    gra = Game()
    gra.run()





