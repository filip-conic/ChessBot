from Players.PlayerInterface import PlayerInterface

class UserPlayer(PlayerInterface):
    def make_move_uci(self, board, color):
        user_in = input("Input a move: ")
        return user_in