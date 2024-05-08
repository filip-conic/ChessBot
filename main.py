import gameBoard
from Players import StockfishPlayer, UserPlayer, ChessEnginePlayer, ChessEngine2
from Visualizers import PygameVisualizer

start_fen = gameBoard.TEST_FEN

visualizer = PygameVisualizer.PygameVisualizer(start_fen)
gameBoard = gameBoard.GameBoard(visualizer, start_fen)
white = ChessEngine2.ChessEngine2Player()
#white = ChessEnginePlayer.ChessEnginePlayer()
black = UserPlayer.UserPlayer()

gameBoard.play_game(white, black)