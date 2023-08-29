import tkinter as tk
 

MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board

BTN_WIDTH, BTN_HEIGHT = 8, 2
BTN_PADX = 20
BTN_FONT = ("Comic Sans MS", 20, "bold")
CELL_FONT = ("Comic Sans MS", 16, "bold")


class SudokuUI(tk.Frame):
    def __init__(self, window, game):
        tk.Frame.__init__(self, window)
        self.window = window
        self.game = game
        self.row, self.col = -1, -1 #select cell, (-1, -1): not selects
        self.initUI()

    def initUI(self):
        self.window.title("Sudoku")
        # self.pack(fill=tk.BOTH, expand=1)
        
        self.canvas = tk.Canvas(self.window, width=WIDTH, height=HEIGHT, highlightthickness=0)
        # self.canvas.pack(fill=tk.BOTH, side=tk.TOP) #Add to window
        self.canvas.grid(row = 0, column=0, rowspan=3)
        self.new_game_btn = tk.Button(self.window, text="New Game", font = BTN_FONT, fg="blue2", 
                                      width=BTN_WIDTH, height=BTN_HEIGHT, 
                                      command=self.new_game)
        self.new_game_btn.grid(row=0, column=1, padx=BTN_PADX)

        self.reset_game_btn = tk.Button(self.window, text="Reset", font = BTN_FONT, fg="SpringGreen3", 
                                        width=BTN_WIDTH, height=BTN_HEIGHT,
                                        command=self.reset_game)
        self.reset_game_btn.grid(row=1, column=1, padx=BTN_PADX)
        self.solve_game_btn = tk.Button(self.window, text="Solve", font = BTN_FONT, fg="firebrick1", 
                                        width=BTN_WIDTH, height=BTN_HEIGHT,
                                        command=self.solve)
        self.solve_game_btn.grid(row=2, column=1, padx=BTN_PADX)


        self.draw_grid()

        self.canvas.bind("<Button-1>", self.cell_clicked)
        self.canvas.bind("<Key>", self.key_pressed)
        


    def draw_grid(self):
        # create_line(x0, y0, x1, y1)
        for i in range(10):
            if(i % 3 == 0):
                self.canvas.create_line(MARGIN + i * SIDE, MARGIN, 
                                        MARGIN + i * SIDE, HEIGHT - MARGIN, 
                                        fill="black", width=3)
                self.canvas.create_line(MARGIN, MARGIN + i * SIDE,
                                        WIDTH - MARGIN, MARGIN + i * SIDE,
                                        fill="black", width=3)
                
            else:
                self.canvas.create_line(MARGIN + i * SIDE, MARGIN, 
                                        MARGIN + i * SIDE, HEIGHT - MARGIN, 
                                        fill="black")
            
                self.canvas.create_line(MARGIN, MARGIN + i * SIDE,
                                        WIDTH - MARGIN, MARGIN + i * SIDE,
                                        fill="black")
    
    def draw_puzzle(self):
        self.select_menu.destroy()
        self.reset_game()
        for i in range(9):
            for j in range(9):
                answer = self.game.solved_board[i][j]
                original = self.game.answer_board[i][j]
                if(original != 0):
                    self.canvas.create_text(MARGIN + j  * SIDE + SIDE / 2,
                                            MARGIN + i * SIDE + SIDE / 2,
                                            text=original, font=CELL_FONT,
                                            tags="numbers", 
                                            fill="black" if(answer == original) else "red")
    

    def draw_cursor(self):
        self.canvas.delete("cursor")
        if(self.row >= 0 and self.col >= 0):
            self.canvas.create_rectangle(MARGIN + self.col * SIDE + 1,
                                         MARGIN + self.row * SIDE + 1,
                                         MARGIN + (self.col + 1) * SIDE - 1,
                                         MARGIN + (self.row + 1) * SIDE - 1,
                                         outline="red", tags="cursor")


    def new_game(self):
        self.select_menu = tk.Toplevel(self.window)
        self.select_menu.title("Select Difficulty")

        w, h = 200,  300
        x = self.window.winfo_x() + self.window.winfo_width() / 2 - w / 2
        y = self.window.winfo_y() + self.window.winfo_height() / 2 - h / 2

        self.select_menu.geometry("%dx%d+%d+%d" % (w, h, x , y)) # set menu size and position
        easy_btn = tk.Button(self.select_menu, text="Easy", font = BTN_FONT, fg="lime green",
                            width=BTN_WIDTH, height=BTN_HEIGHT,
                            command=lambda: [self.game.generate_board(2), self.draw_puzzle()])
        easy_btn.pack()
        medium_btn = tk.Button(self.select_menu, text="Medium", font = BTN_FONT, fg="dodger blue",
                               width=BTN_WIDTH, height=BTN_HEIGHT, 
                               command=lambda: [self.game.generate_board(3), self.draw_puzzle()])
        medium_btn.pack()
        hard_btn = tk.Button(self.select_menu, text="Hard", font = BTN_FONT, fg="dark orange",
                             width=BTN_WIDTH, height=BTN_HEIGHT,
                             command=lambda: [self.game.generate_board(4), self.draw_puzzle()])
        hard_btn.pack()
        expert_btn = tk.Button(self.select_menu, text="Expert", font = BTN_FONT, fg="red3",
                               width=BTN_WIDTH, height=BTN_HEIGHT,
                               command=lambda: [self.game.generate_board(5), self.draw_puzzle()])
        expert_btn.pack()
    
    # Clear board
    def reset_game(self):
        self.canvas.delete("numbers")

    def solve(self):
        pass


    def cell_clicked(self, event):
        x, y = event.x, event.y
        if(x > MARGIN and x < WIDTH - MARGIN and y  > MARGIN and y < HEIGHT - MARGIN):
            self.canvas.focus_set()
            row,  col = (y - MARGIN) // SIDE, (x - MARGIN) // SIDE
            if(row, col) == (self.row, self.col):
                self.row , self.coll = -1, -1
            elif(self.game.board[row][col] == 0):
                self.row, self.col = row, col
        else:
            self.row , self.coll = -1, -1
        
        self.draw_cursor()

    def key_pressed(self, event):
        
        if(self.row >= 0 and self.col >= 0 and event.char in "1234567890"):
            self.game.answer_board[self.row][self.col] = int(event.char)
            self.col, self.row = -1, -1
            self.draw_puzzle()
            self.draw_cursor()