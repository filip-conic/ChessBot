import gameBoard
from Players import StockfishPlayer, UserPlayer

gameBoard = gameBoard.GameBoard()
white = StockfishPlayer.StockfishPlayer()
black = UserPlayer.UserPlayer()

gameBoard.play_game(white, black)