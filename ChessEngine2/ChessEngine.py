import chess


def evaluate_position(board):
    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    bp = len(board.pieces(chess.PAWN, chess.BLACK))
    wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(board.pieces(chess.BISHOP, chess.WHITE))
    bb = len(board.pieces(chess.BISHOP, chess.BLACK))
    wr = len(board.pieces(chess.ROOK, chess.WHITE))
    br = len(board.pieces(chess.ROOK, chess.BLACK))
    wq = len(board.pieces(chess.QUEEN, chess.WHITE))
    bq = len(board.pieces(chess.QUEEN, chess.BLACK))

    material = 100 * (wp - bp) + 300 * (wn - bn) + 300 * (wb - bb) + 500 * (wr - br) + 900 * (wq - bq)
    return material

def get_best_move(board, is_white, depth = 3):
    best_move_value = -100000 if is_white else 100000
    alpha_beta = best_move_value
    best_move = None

    if is_white:
        for move in board.legal_moves:
            board.push(move)
            val = minimax(board, not is_white, alpha_beta, 100000, depth - 1)
            board.pop()
            if (is_white and val > best_move_value) or (not is_white and val < best_move_value):
                best_move_value = val
                alpha_beta = max(alpha_beta, best_move_value)
                best_move = move
    else:
        for move in board.legal_moves:
            board.push(move)
            val = minimax(board, not is_white, -100000, alpha_beta, depth-1)
            board.pop()
            if (is_white and val > best_move_value) or (not is_white and val < best_move_value):
                best_move_value = val
                best_move = move
                alpha_beta = min(alpha_beta, best_move_value)
    return best_move

# White = Maximizing
# Black = Minimizing
def minimax(board, depth, alpha, beta, is_maximizing):
    if depth <= 0 or board.game_is_over():
        return evaluate_position(board)

    # White to play
    if is_maximizing:
        best_move = -100000
        for move in board.legal_moves:
            board.push(move)
            value = minimax(board, depth-1, alpha, beta, not is_maximizing)
            board.pop()
            best_move = max(best_move, value)
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_move

    # Black to play
    else:
        best_move = 100000
        for move in board.legal_moves:
            board.push(move)
            value = minimax(board, depth-1, alpha, beta, not is_maximizing)
            board.pop()
            best_move = min(best_move, value)
            beta = min(beta, value)
            if beta <= alpha:
                break
        return best_move


