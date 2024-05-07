from ChessEngine.Engine import determine_best_move
from Players.PlayerInterface import PlayerInterface
import chess

class ChessEnginePlayer(PlayerInterface):
    def make_move_uci(self, board, color):
        is_white = True if color == chess.WHITE else False
        move = determine_best_move(board, is_white)
        return move.uci()