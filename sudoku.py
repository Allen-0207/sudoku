import tkinter as tk


from Board import SudokuUI
from generate import Game



if __name__ == '__main__':
    window = tk.Tk()

    game = Game()    
        
    board = SudokuUI(window, game)
    
    window.geometry('700x700')
    window.resizable(False, False) #Fix window size

    window.mainloop()   
