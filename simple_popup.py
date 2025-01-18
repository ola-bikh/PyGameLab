import time
import pygame

def show_simple_popup(screen, winner_text):
    """
    Wyświetla proste wyskakujące okienko z informacją o zwycięzcy i przyciskami.

    screen - ekran Pygame.
    winner_text - tekst z informacją o zwycięzcy.

    Zwraca:
    - "continue", jeśli kliknięto "Kontynuuj".
    - "exit", jeśli kliknięto "Zakończ".
    """
    # Wymiary i kolory
    popup_width, popup_height = 300, 150
    popup_color = (200, 200, 200)
    shadow_color = (150, 150, 150)
    text_color = (0, 0, 0)
    button_color = (100, 100, 255)
    button_hover_color = (150, 150, 255)
    button_text_color = (255, 255, 255)
    button_shadow_color = (50, 50, 100)

    # Pozycja okienka
    popup_x = (screen.get_width() - popup_width) // 2
    popup_y = (screen.get_height() - popup_height) // 2

    # Przycisk "Kontynuuj"
    continue_button_rect = pygame.Rect(popup_x + 30, popup_y + 80, 100, 40)
    # Przycisk "Zakończ"
    exit_button_rect = pygame.Rect(popup_x + 170, popup_y + 80, 100, 40)

    # Czcionka
    font = pygame.font.Font(None, 36)
    button_font = pygame.font.Font(None, 28)

    # Pętla do obsługi popupu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button_rect.collidepoint(event.pos):
                    return "continue"
                elif exit_button_rect.collidepoint(event.pos):
                    return "exit"

        # Rysowanie cienia dla popupu
        pygame.draw.rect(screen, shadow_color, (popup_x + 5, popup_y + 5, popup_width, popup_height))

        # Rysowanie popupu
        pygame.draw.rect(screen, popup_color, (popup_x, popup_y, popup_width, popup_height))
        pygame.draw.rect(screen, (0, 0, 0), (popup_x, popup_y, popup_width, popup_height), 2)

        # Tekst zwycięzcy
        text_surface = font.render(winner_text, True, text_color)
        text_rect = text_surface.get_rect(center=(popup_x + popup_width // 2, popup_y + 40))
        screen.blit(text_surface, text_rect)

        # Rysowanie cienia przycisku "Kontynuuj"
        pygame.draw.rect(screen, button_shadow_color, continue_button_rect.move(3, 3))
        # Przycisk "Kontynuuj"
        mouse_pos = pygame.mouse.get_pos()
        continue_color = button_hover_color if continue_button_rect.collidepoint(mouse_pos) else button_color
        pygame.draw.rect(screen, continue_color, continue_button_rect)
        continue_text = button_font.render("Kontynuuj", True, button_text_color)
        continue_text_rect = continue_text.get_rect(center=continue_button_rect.center)
        screen.blit(continue_text, continue_text_rect)

        # Rysowanie cienia przycisku "Zakończ"
        pygame.draw.rect(screen, button_shadow_color, exit_button_rect.move(3, 3))
        # Przycisk "Zakończ"
        exit_color = button_hover_color if exit_button_rect.collidepoint(mouse_pos) else button_color
        pygame.draw.rect(screen, exit_color, exit_button_rect)
        exit_text = button_font.render("Zakończ", True, button_text_color)
        exit_text_rect = exit_text.get_rect(center=exit_button_rect.center)
        screen.blit(exit_text, exit_text_rect)

        pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Okienko Popup")

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # Wypełnienie białym kolorem

        pygame.display.flip()

        # Przykładowe użycie w grze:
        time.sleep(2)
        result = show_simple_popup(screen, "Gracz 1 wygrał!")
        if result == "continue":
            print("Kontynuujemy grę!")
        elif result == "exit":
            print("Koniec gry.")
            pygame.quit()
            exit()



    pygame.quit()
