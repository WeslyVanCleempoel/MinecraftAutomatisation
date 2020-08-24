from pywinauto.application import Application
import time

import constants


def open_minecraft(path, world, launcher_delay, game_delay):
    app = Application().start(path)
    print(f"Started launcher at {path}, waiting {launcher_delay} seconds for it to load...")
    time.sleep(launcher_delay)
    dlg = app.top_window()
    dlg.set_keyboard_focus()
    dlg.type_keys("{TAB 11}{ENTER}")
    print(f"Starting game, waiting {game_delay} seconds before attempting to connect...")
    time.sleep(game_delay)
    connect_game_window(world)


def connect_game_window(world):
    app = Application().connect(title_re="Minecraft 1.*", class_name="GLFW30")
    dlg = app.top_window()
    dlg.set_keyboard_focus()
    dlg.type_keys("{TAB}{ENTER}")
    time.sleep(0.2)
    print(f"connected to game window, loading world \"{world}\"...")
    load_world(dlg, world)


def load_world(dlg, world):
    dlg.set_keyboard_focus()
    dlg.type_keys(world)
    time.sleep(0.1)
    dlg.type_keys("{TAB 2}{ENTER}")
    time.sleep(15)
    print(f"Minecraft world {world} loaded.")


if __name__ == '__main__':
    open_minecraft(constants.LAUNCHER_PATH, constants.MC_WORLD_NAME, 2.5, 25)
