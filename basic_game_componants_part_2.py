import pygame

# Funkcja do rysowania konturu linii
def draw_line_outline(screen, start_x, start_y, end_x, end_y, color, thickness=1):
    """
    Rysuje linię między dwoma punktami.

    screen - ekran Pygame.
    start_x, start_y - współrzędne początku linii.
    end_x, end_y - współrzędne końca linii.
    color - kolor linii (RGB).
    thickness - grubość linii (domyślnie 1).
    """
    pygame.draw.line(screen, color, (start_x, start_y), (end_x, end_y), thickness)


# Funkcja do rysowania konturu okręgu
def draw_circle_outline(screen, center_x, center_y, radius, color, thickness=1):
    """
    Rysuje okrąg na ekranie (tylko kontur).

    screen - ekran Pygame.
    center_x, center_y - współrzędne środka okręgu.
    radius - promień okręgu.
    color - kolor okręgu (RGB).
    thickness - grubość obramowania okręgu.
    """
    pygame.draw.circle(screen, color, (center_x, center_y), radius, thickness)


# Funkcja do rysowania konturu prostokąta
def draw_rectangle_outline(screen, x, y, width, height, color, thickness=1):
    """
    Rysuje prostokąt na ekranie (tylko kontur).

    screen - ekran Pygame.
    x, y - współrzędne lewego górnego rogu prostokąta.
    width, height - szerokość i wysokość prostokąta.
    color - kolor prostokąta (RGB).
    thickness - grubość obramowania prostokąta.
    """
    pygame.draw.rect(screen, color, (x, y, width, height), thickness)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Rysowanie konturów")

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # Wypełnienie białym kolorem

        # Przykładowe rysowanie konturów
        draw_line_outline(screen, 50, 50, 200, 50, (255, 0, 0), thickness=5)  # Czerwona linia
        draw_circle_outline(screen, 400, 300, 50, (0, 255, 0), thickness=5)  # Zielony okrąg kontur
        draw_rectangle_outline(screen, 500, 100, 150, 100, (0, 0, 255), thickness=3)  # Niebieski prostokąt kontur

        pygame.display.flip()

    pygame.quit()
