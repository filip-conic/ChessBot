from chessboard import display

class PygameDisplayBoard:
    # Start position is given in FEN notation
    def __init__(self, startPosition):
        self.displayBoard = display.start()
        try:
            display.update(startPosition, self.displayBoard)
        except Exception as e:
            print("Invalid Fen, Exception: " + str(e))

    def update_board(self, fen):
        try:
            display.update(fen, self.displayBoard)
        except Exception as e:
            print("Invalid Fen, Exception: " + str(e))