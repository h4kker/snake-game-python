from tkinter import Tk
from gui import GameGUI

if __name__ == "__main__":
    window = Tk()
    window.title("Snake Game")

    game = GameGUI(window)
    window.mainloop()
