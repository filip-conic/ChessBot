from chessboard import display

DEFAULT_START_POSITION = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

class PygameDisplayBoard:

    # Start position is given in FEN notation
    def __init__(self, startPosition = DEFAULT_START_POSITION):
        self.displayBoard = display.start()
        try:
            print("Test 1")
            display.update(startPosition, self.displayBoard)
            print("test 2")
        except Exception as e:
            print("Invalid Fen, Exception: " + str(e))

    def updateBoard(self, fen):
        print("Here")
        print(fen)
        try:
            print(display)
            display.update(fen, self.displayBoard)
        except Exception as e:
            print("Invalid Fen, Exception: " + str(e))