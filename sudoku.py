import tkinter as tk


from Board import SudokuUI
from generate import Game

w = 700
h = 500

if __name__ == '__main__':
    window = tk.Tk()
    ws = window.winfo_screenwidth() # width of the screen
    hs = window.winfo_screenheight() # height of the screen
    game = Game()    
        
    board = SudokuUI(window, game)

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    window.resizable(False, False) #Fix window size

    window.mainloop()   
