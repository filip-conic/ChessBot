from Players.PlayerInterface import PlayerInterface
from stockfish import Stockfish

class StockfishPlayer(PlayerInterface):
    def __init__(self):
        self.stockfish = Stockfish(path="/Users/filipconic/Desktop/SeniorProject/ChessBot/Stockfish/stockfish-macos-x86-64")

    def make_move_uci(self, fen):
        self.stockfish.set_fen_position(fen)
        return self.stockfish.get_best_move()
