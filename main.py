import gameBoard
from Players import StockfishPlayer, UserPlayer
from Visualizers import PygameVisualizer

visualizer = PygameVisualizer.PygameVisualizer(gameBoard.DEFAULT_START_POSITION)
gameBoard = gameBoard.GameBoard(visualizer)
white = StockfishPlayer.StockfishPlayer()
black = UserPlayer.UserPlayer()

gameBoard.play_game(white, black)