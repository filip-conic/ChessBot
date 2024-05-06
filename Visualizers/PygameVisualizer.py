from Visualizers.VisualizerInterface import VisualizerInterface
from chessboard import display

class PygameVisualizer(VisualizerInterface):

    def __init__(self, start_fen):
        self.displayBoard = display.start()
        try:
            display.update(start_fen, self.displayBoard)
        except Exception as e:
            print("Invalid Fen, Exception: " + str(e))

    def update_board(self, fen):
        try:
            display.update(fen, self.displayBoard)
        except Exception as e:
            print("Invalid Fen, Exception: " + str(e))
