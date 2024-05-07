import gameBoard
from Players import StockfishPlayer, UserPlayer, ChessEnginePlayer
from Visualizers import PygameVisualizer

visualizer = PygameVisualizer.PygameVisualizer(gameBoard.DEFAULT_START_POSITION)
gameBoard = gameBoard.GameBoard(visualizer)
white = ChessEnginePlayer.ChessEnginePlayer()
black = UserPlayer.UserPlayer()

gameBoard.play_game(white, black)