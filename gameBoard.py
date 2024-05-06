import chess
import pygameDisplay

DEFAULT_START_POSITION = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

class GameBoard:

    def __init__(self, visualizer):
        self.game_board = chess.Board()
        self.to_move = "white"
        self.visualizer = visualizer

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

    def update_board_uci(self, move_str):
        if not self.is_legal_move_uci(move_str):
            print("That is not a legal move")
            return False

        move = chess.Move.from_uci(move_str)
        self.game_board.push(move)
        self.visualizer.update_board(self.fen())
        return True

    def make_player_move(self, player):
        successful = False
        while not successful:
            player_move = player.make_move_uci(self.fen())
            successful = self.update_board_uci(player_move)

    def play_game(self, white, black):
        while True:
            self.make_player_move(white)
            self.make_player_move(black)
