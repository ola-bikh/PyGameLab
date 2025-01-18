import tkinter as tk
import pygame
import ctypes


def get_pygame_window_position():
    """
    Pobiera pozycję okna Pygame na ekranie.
    Działa na systemie Windows przy użyciu ctypes.
    """
    hwnd = pygame.display.get_wm_info()["window"]

    # Definicja struktury RECT ręcznie
    class RECT(ctypes.Structure):
        _fields_ = [
            ("left", ctypes.c_long),
            ("top", ctypes.c_long),
            ("right", ctypes.c_long),
            ("bottom", ctypes.c_long),
        ]

    rect = RECT()
    ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
    return rect.left, rect.top


def show_system_popup(screen, winner_text):
    """
    Wyświetla systemowe okienko z komunikatem o wyniku gry.
    """

    def on_continue():
        nonlocal result
        result = "continue"
        root.destroy()  # Zamknij okno tkinter

    def on_exit():
        nonlocal result
        result = "exit"
        root.destroy()  # Zamknij okno tkinter

    # Pobierz rozmiar i pozycję okna Pygame
    screen_width, screen_height = pygame.display.get_window_size()
    screen_x, screen_y = get_pygame_window_position()

    # Inicjalizacja tkinter
    root = tk.Tk()
    root.withdraw()  # Ukryj główne okno tkinter

    # Tworzenie okienka popup
    result = None
    popup = tk.Toplevel(root)
    popup.title("Informacja")
    popup.geometry("400x200")  # Zwiększono rozmiar okienka
    popup.resizable(False, False)

    # Pozycjonowanie okienka na środku okna Pygame
    popup_x = screen_x + (screen_width - 400) // 2
    popup_y = screen_y + (screen_height - 200) // 2
    popup.geometry(f"400x200+{popup_x}+{popup_y}")

    # Dodanie komunikatu i przycisków
    label = tk.Label(popup, text=winner_text, font=("Arial", 14))
    label.pack(pady=30)

    button_width = 12  # Zwiększono szerokość przycisków
    continue_button = tk.Button(popup, text="Kontynuuj", command=on_continue, width=button_width)
    continue_button.pack(side="left", padx=50, pady=20)

    exit_button = tk.Button(popup, text="Zakończ", command=on_exit, width=button_width)
    exit_button.pack(side="right", padx=50, pady=20)

    root.mainloop()  # Uruchom pętlę tkinter

    return result


# Przykład użycia
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Gra z okienkiem")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 255, 255))  # Wypełnij ekran kolorem
        pygame.display.flip()

        # Wyświetl okienko z komunikatem
        result = show_system_popup(screen, "Gracz 1 wygrał!")
        if result == "continue":
            print("Kontynuujemy grę!")
        elif result == "exit":
            print("Kończymy grę.")
            running = False

    pygame.quit()
