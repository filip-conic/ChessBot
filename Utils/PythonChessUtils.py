import chess


def is_game_over(board):
    if board.is_checkmate() or board.is_stalemate() \
            or board.is_insufficient_material() or board.is_seventyfive_moves() \
            or board.is_fivefold_repetition() or board.can_claim_draw():
        return True
    else:
        return False
