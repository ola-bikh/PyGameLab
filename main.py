import pygame
import random #bibloteka losowosci
from kostka_do_gry import draw_die  # Funkcja do rysowania kostki
from simple_popup import show_simple_popup  # Funkcja do wyświetlania okienka zwycięzcy

# Inicjalizacja Pygame
pygame.init()

# Ustawienia ekranu
SZEROKOSC, WYSOKOSC = 800, 600  # Większy rozmiar ekranu
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption("Gra planszowa Aleksandry Bikhit")  # Zaktualizowany tytuł

# Kolory
BIALY = (255, 255, 255)
CZARNY = (0, 0, 0)
CZERWONY = (255, 0, 0)
NIEBIESKI = (0, 0, 255)

# Ustawienia gry
ROZMIAR_PLANSZY = 20  # liczba pól na planszy
SZEROKOSC_POLA = SZEROKOSC // ROZMIAR_PLANSZY  # Szerokość każdego pola
pozycje_graczy = [0, 0]  # Pozycje startowe graczy
aktualny_gracz = 0  # Gracz 1 zaczyna
czcionka = pygame.font.Font(None, 36)

# Ustawienia kostki
kostka_x, kostka_y = 650, 50  # Pozycja kostki na ekranie
rozmiar_kostki = 50  # Rozmiar kostki
wylosowana_liczba = 1  # Domyślna liczba oczek na kostce

# Pętla gry
dziala = True
while dziala:
    ekran.fill(BIALY)

    # Rysowanie planszy (dwie ścieżki)
    for i in range(ROZMIAR_PLANSZY):
        # Górna ścieżka dla Gracza 1
        pygame.draw.rect(ekran, CZARNY, (i * SZEROKOSC_POLA, WYSOKOSC // 3, SZEROKOSC_POLA, 50), 1)
        # Dolna ścieżka dla Gracza 2
        pygame.draw.rect(ekran, CZARNY, (i * SZEROKOSC_POLA, (WYSOKOSC // 3) * 2, SZEROKOSC_POLA, 50), 1)

    # Rysowanie graczy
    pygame.draw.circle(ekran, CZERWONY, (pozycje_graczy[0] * SZEROKOSC_POLA + SZEROKOSC_POLA // 2, WYSOKOSC // 3 + 25), 15)  # Gracz 1
    pygame.draw.circle(ekran, NIEBIESKI, (pozycje_graczy[1] * SZEROKOSC_POLA + SZEROKOSC_POLA // 2, (WYSOKOSC // 3) * 2 + 25), 15)  # Gracz 2

    # Rysowanie kostki
    draw_die(ekran, kostka_x, kostka_y, rozmiar_kostki, wylosowana_liczba)

    # Wyświetlanie aktualnego gracza
    tekst_gracza = f"Tura Gracza {aktualny_gracz + 1} (Naciśnij SPACJĘ, aby rzucić)"
    powierzchnia_tekstu = czcionka.render(tekst_gracza, True, CZARNY)
    ekran.blit(powierzchnia_tekstu, (50, 20))  # Pozycja tekstu u góry ekranu

    # Obsługa zdarzeń
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            dziala = False
        elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_SPACE:
            # Rzut kostką
            wylosowana_liczba = random.randint(1, 6)
            print(f"Gracz {aktualny_gracz + 1} wylosował {wylosowana_liczba}")
            pozycje_graczy[aktualny_gracz] += wylosowana_liczba

            # Sprawdzanie warunku zwycięstwa
            if pozycje_graczy[aktualny_gracz] >= ROZMIAR_PLANSZY:
                tekst_zwyciezcy = f"Gracz {aktualny_gracz + 1} wygrał!"
                wynik = show_simple_popup(ekran, tekst_zwyciezcy)
                if wynik == "exit":
                    dziala = False
                else:
                    # Resetowanie gry
                    pozycje_graczy = [0, 0]
                    aktualny_gracz = 0
                    continue

            # Zmiana gracza
            aktualny_gracz = 1 - aktualny_gracz

    # Aktualizacja ekranu
    pygame.display.flip()

pygame.quit()
