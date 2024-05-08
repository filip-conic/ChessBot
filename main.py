import gameBoard
from Players import StockfishPlayer, UserPlayer, ChessEngine
from Visualizers import PygameVisualizer

start_fen = gameBoard.TEST_FEN

visualizer = PygameVisualizer.PygameVisualizer(start_fen)
gameBoard = gameBoard.GameBoard(visualizer, start_fen)
white = ChessEngine.ChessEnginePlayer()
black = UserPlayer.UserPlayer()

gameBoard.play_game(white, black)