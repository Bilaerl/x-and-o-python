class GameBoard:
    board = [
        ['-','-','-'],
        ['-','-','-'],
        ['-','-','-']
    ]

    x_to_move = True

    def __init__(self):
        pass

    def set_square(self, row, col):
        if self.x_to_move:
            self.board[row][col] = 'X'
        else:
            self.board[row][col] = 'O'
        
        self.x_to_move = not self.x_to_move
    
    def get_square(self, row, col):
        return self.board[row][col]
    
    def print_board(self):
        for row in self.board:
            for col in row:
                print(col, end="\t")
            print()
            
