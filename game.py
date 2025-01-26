import pygame
import random
from player import Player
from board import Board
from die import Die
from simple_popup import show_simple_popup


class Game:
    def __init__(self):
        pygame.init()
        self.SZEROKOSC, self.WYSOKOSC = 800, 600  # Screen dimensions
        self.ROZMIAR_PLANSZY = 20  # Number of cells on the board
        self.SZEROKOSC_POLA = self.SZEROKOSC // self.ROZMIAR_PLANSZY  # Cell width
        self.ekran = pygame.display.set_mode((self.SZEROKOSC, self.WYSOKOSC))
        pygame.display.set_caption("Gra planszowa")
        self.clock = pygame.time.Clock()

        # Players and board
        self.board = Board(self.ROZMIAR_PLANSZY, self.SZEROKOSC, self.WYSOKOSC)
        self.players = [
            Player(color=(255, 0, 0), start_pos=0, path_y=self.WYSOKOSC // 3),
            Player(color=(0, 0, 255), start_pos=0, path_y=(self.WYSOKOSC // 3) * 2)
        ]
        self.current_player = 0
        self.font = pygame.font.Font(None, 36)

        # Die
        self.die = Die(650, 50, 50)

    def display_turn(self):
        """Display the current player's turn."""
        tekst_gracza = f"Tura Gracza {self.current_player + 1} (Naciśnij SPACJĘ, aby rzucić)"
        powierzchnia_tekstu = self.font.render(tekst_gracza, True, (0, 0, 0))
        self.ekran.blit(powierzchnia_tekstu, (50, 20))

    def check_winner(self):
        """Check if the current player has won."""
        if self.players[self.current_player].position >= self.ROZMIAR_PLANSZY:
            tekst_zwyciezcy = f"Gracz {self.current_player + 1} wygrał!"
            wynik = show_simple_popup(self.ekran, tekst_zwyciezcy)
            if wynik == "exit":
                pygame.quit()
                exit()  # Stop the game
            else:
                self.reset_game()
        return False

    def reset_game(self):
        """Reset the game state."""
        for player in self.players:
            player.position = 0
        self.current_player = 0

    def run(self):
        """Run the main game loop."""
        running = True
        while running:
            self.ekran.fill((255, 255, 255))
            self.board.draw(self.ekran)
            for player in self.players:
                player.draw(self.ekran, self.SZEROKOSC_POLA)
            self.die.draw(self.ekran)
            self.display_turn()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.die.roll()
                    print(f"Gracz {self.current_player + 1} wylosował {self.die.value}")
                    self.players[self.current_player].move(self.die.value, self.ROZMIAR_PLANSZY)

                    # Check if the current player has won
                    if self.players[self.current_player].position >= self.ROZMIAR_PLANSZY:
                        tekst_zwyciezcy = f"Gracz {self.current_player + 1} wygrał!"
                        wynik = show_simple_popup(self.ekran, tekst_zwyciezcy)
                        if wynik == "exit":
                            running = False
                            break
                        else:
                            # Reset the game
                            for player in self.players:
                                player.position = 0
                            self.current_player = 0
                            continue  # Restart the loop for the reset state

                    # Switch to the next player
                    self.current_player = 1 - self.current_player

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()