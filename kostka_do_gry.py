import pygame
import random


def draw_die(screen, x, y, size, number):
    """
    Rysuje dwuwymiarową kostkę do gry.

    screen - ekran Pygame.
    x, y - współrzędne lewego górnego rogu kostki.
    size - długość boku kostki.
    number - liczba oczek (1-6).
    """
    # Kolory
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Rysowanie prostokątnej kostki
    pygame.draw.rect(screen, white, (x, y, size, size))  # Front kostki
    pygame.draw.rect(screen, black, (x, y, size, size), 2)  # Obramowanie

    # Rysowanie oczek
    draw_die_dots(screen, x, y, size, number)


def draw_die_dots(screen, x, y, size, number):
    """
    Rysuje oczka na kostce w zależności od liczby oczek.

    screen - ekran Pygame.
    x, y - współrzędne lewego górnego rogu kostki.
    size - długość boku kostki.
    number - liczba oczek (1-6).
    """
    black = (0, 0, 0)
    dot_radius = size // 10
    cx, cy = x + size // 2, y + size // 2  # Środek kostki

    # Współrzędne oczek
    positions = {
        1: [(cx, cy)],
        2: [(x + size // 4, y + size // 4), (x + 3 * size // 4, y + 3 * size // 4)],
        3: [(x + size // 4, y + size // 4), (cx, cy), (x + 3 * size // 4, y + 3 * size // 4)],
        4: [(x + size // 4, y + size // 4), (x + 3 * size // 4, y + size // 4),
            (x + size // 4, y + 3 * size // 4), (x + 3 * size // 4, y + 3 * size // 4)],
        5: [(x + size // 4, y + size // 4), (x + 3 * size // 4, y + size // 4),
            (cx, cy),
            (x + size // 4, y + 3 * size // 4), (x + 3 * size // 4, y + 3 * size // 4)],
        6: [(x + size // 4, y + size // 4), (x + 3 * size // 4, y + size // 4),
            (x + size // 4, cy), (x + 3 * size // 4, cy),
            (x + size // 4, y + 3 * size // 4), (x + 3 * size // 4, y + 3 * size // 4)],
    }

    for pos in positions[number]:
        pygame.draw.circle(screen, black, pos, dot_radius)


# Główna pętla gry
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Kostka do Gry")
    clock = pygame.time.Clock()

    # Parametry kostki
    die_x, die_y = 300, 200
    die_size = 100
    die_number = 1  # Początkowa liczba oczek

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Losowanie liczby oczek
                    die_number = random.randint(1, 6)

        # Rysowanie tła i kostki
        screen.fill((200, 100, 30))  # Tło

        draw_die(screen, die_x, die_y, die_size, die_number)

        # Aktualizacja ekranu
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
