from ChessEngine2.ChessEngine import get_best_move
from Players.PlayerInterface import PlayerInterface
import chess

class ChessEngine2Player(PlayerInterface):
    def make_move_uci(self, board, color):
        is_white = True if color == chess.WHITE else False
        move = get_best_move(board, is_white, 4)
        return move.uci()