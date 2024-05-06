import chess
import pygameDisplay

DEFAULT_START_POSITION = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'


class GameBoard:

    def __init__(self, visualize=True):
        self.game_board = chess.Board()
        self.to_move = "white"
        self.visualize = visualize
        if self.visualize:
            self.display_board = pygameDisplay.PygameDisplayBoard(
                'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')

    def fen(self):
        return self.game_board.fen()

    def whos_move(self):
        return self.to_move

    def is_legal_move_uci(self, move_str):
        move = chess.Move.from_uci(move_str)
        if move in self.game_board.legal_moves:
            return True
        else:
            return False

    def make_move_uci(self, move_str):
        if not self.is_legal_move_uci(move_str):
            print("That is not a legal move")
            return

        move = chess.Move.from_uci(move_str)
        self.game_board.push(move)
        if self.visualize:
            self.display_board.update_board(self.fen())
