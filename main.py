import gameBoard

gameBoard = gameBoard.GameBoard()

while True:
    userIn = input("Input a move: ")
    gameBoard.make_move_uci(userIn)
