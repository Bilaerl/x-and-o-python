from gameboard import GameBoard

game_board = GameBoard()

game_board.set_square(0,0, 'X')
game_board.set_square(0,1, 'O')
game_board.set_square(1,1, 'X')
 
game_board.print_board()