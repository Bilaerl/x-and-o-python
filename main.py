from game import GameBoard
import tkinter as tk

root = tk.Tk()
root.title("X and O")
root.resizable(False, False)

game_board = GameBoard()

btn = [
       [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]
       ]

def callback(row, col):
      game_board.set_square(row, col)
      
      btn[row][col].configure(
                              foreground = "blue",
                              text = game_board.board[row][col]
                              )

def board():
    
    global square
    for r in range (3):
        for c in range(3):
    
            btn[r][c] = tk.Button(
                        height = 10,
                        width = 10,
                        command = lambda row = r, col = c: callback(row, col)
                                )
            
            btn[r][c].grid(row = r, column = c)
            clear()
def clear():
    clear_btn = tk.Button(text = "clear", background = 'red',
                          command = cleared
                            )
    clear_btn.grid(row = 3, column = 1)
    
def cleared():
    for i in range(3):
        for j in range(3):
            btn[i][j].configure(text = "")
    
board()

tk.mainloop()