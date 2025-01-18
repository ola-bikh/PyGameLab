import pygame

def draw_text_box(screen, text, x, y, width, height, text_color, box_color):
    """
    Rysuje pole tekstowe z wyświetlonym tekstem, który automatycznie dopasowuje czcionkę do rozmiaru pola.
    
    screen - ekran Pygame.
    text - tekst do wyświetlenia.
    x, y - współrzędne lewego górnego rogu pola tekstowego.
    width, height - wymiary pola tekstowego.
    text_color - kolor tekstu (RGB).
    box_color - kolor tła pola tekstowego (RGB).
    """
    # Rysowanie prostokąta (tło pola tekstowego)
    pygame.draw.rect(screen, box_color, (x, y, width, height))
    pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height), 2)  # Obramowanie

    # Dopasowanie czcionki
    font_size = height // 2  # Skalowanie czcionki do połowy wysokości pola
    font = pygame.font.Font(None, font_size)

    # Dopasowanie tekstu do szerokości pola
    while font.size(text)[0] > width - 10:  # Zapas na margines
        font_size -= 1
        font = pygame.font.Font(None, font_size)

    # Renderowanie tekstu
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

#przykład użycia
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # Wypełnienie ekranu białym kolorem

        # Wyświetlenie pola tekstowego
        draw_text_box(screen, "Gracz 1 wygrał!", 200, 100, 400, 80, (255, 0, 0), (200, 200, 200))
        draw_text_box(screen, "Twój ruch!", 200, 200, 400, 80, (0, 255, 0), (150, 150, 150))

        pygame.display.flip()

    pygame.quit()
