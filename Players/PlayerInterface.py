from abc import ABC, abstractmethod

class PlayerInterface(ABC):

    @abstractmethod
    def make_move_uci(self, board, color):
        pass