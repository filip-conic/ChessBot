from abc import ABC, abstractmethod

class VisualizerInterface(ABC):

    @abstractmethod
    def update_board(self, fen):
        pass