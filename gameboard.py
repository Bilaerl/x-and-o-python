class GameBoard:
    board = [
        ['-','-','-'],
        ['-','-','-'],
        ['-','-','-']
    ]

    def __init__(self):
        pass

    def set_square(self, row, col, char):
        self.board[row][col] = char
    
    def get_square(self, row, col):
        return self.board[row][col]
    
    def print_board(self):
        for row in self.board:
            for col in row:
                print(col, end="\t")
            print()
            
