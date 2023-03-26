import chess


PAWN = 1
KNIGHT = 3
BISHOP = 3.25
ROOK = 5
QUEEN = 9

MOVE = 0.01

CENTRAL_SQ = (chess.E4, chess.E5, chess.D4, chess.D5)
CENTRAL_BONUS = 0.25
FLANK_SQ = (chess.C4, chess.C5, chess.F4, chess.F5)
FLANK_BONUS = 0.15

CASTLE_BOOST = 0.5


def evaluate_white(board: chess.Board):

    pawns = len(tuple(board.pieces(chess.PieceType(chess.PAWN), chess.WHITE))) * PAWN
    knights = len(tuple(board.pieces(chess.PieceType(chess.KNIGHT), chess.WHITE))) * KNIGHT
    bishops = len(tuple(board.pieces(chess.PieceType(chess.BISHOP), chess.WHITE))) * BISHOP
    rooks = len(tuple(board.pieces(chess.PieceType(chess.ROOK), chess.WHITE))) * ROOK
    queens = len(tuple(board.pieces(chess.PieceType(chess.QUEEN), chess.WHITE))) * QUEEN

    evaluation = pawns + knights + bishops + rooks + queens

    board_copy = board.copy()
    board_copy.turn = chess.WHITE
    moves = board_copy.legal_moves.count() * MOVE

    evaluation += moves

    for sq in CENTRAL_SQ:
        if board.piece_at(sq) != None:
            if board.piece_at(sq).color == chess.WHITE:
                evaluation += CENTRAL_BONUS
    
    for sq in FLANK_SQ:
        if board.piece_at(sq) != None:
            if board.piece_at(sq).color == chess.WHITE:
                evaluation += FLANK_BONUS
    
    for move in board.move_stack:
        if board.is_castling(move) and board.color_at(move.to_square) == chess.WHITE:
            evaluation += CASTLE_BOOST

    return evaluation


def evaluate_black(board: chess.Board):

    pawns = len(tuple(board.pieces(chess.PieceType(chess.PAWN), chess.BLACK))) * PAWN
    knights = len(tuple(board.pieces(chess.PieceType(chess.KNIGHT), chess.BLACK))) * KNIGHT
    bishops = len(tuple(board.pieces(chess.PieceType(chess.BISHOP), chess.BLACK))) * BISHOP
    rooks = len(tuple(board.pieces(chess.PieceType(chess.ROOK), chess.BLACK))) * ROOK
    queens = len(tuple(board.pieces(chess.PieceType(chess.QUEEN), chess.BLACK))) * QUEEN

    evaluation = pawns + knights + bishops + rooks + queens

    board_copy = board.copy()
    board_copy.turn = chess.BLACK
    moves = board_copy.legal_moves.count() * MOVE

    evaluation += moves

    for sq in CENTRAL_SQ:
        if board.piece_at(sq) != None:
            if board.piece_at(sq).color == chess.BLACK:
                evaluation += CENTRAL_BONUS
    
    for sq in FLANK_SQ:
        if board.piece_at(sq) != None:
            if board.piece_at(sq).color == chess.BLACK:
                evaluation += FLANK_BONUS
    
    for move in board.move_stack:
        if board.is_castling(move) and board.color_at(move.to_square) == chess.BLACK:
            evaluation += CASTLE_BOOST

    return evaluation


def evaluate_pos(board: chess.Board):

    if board.is_checkmate():
        if board.turn == chess.WHITE:
            return -9999
        
        else:
            return 9999
    
    elif board.is_stalemate():
        return 0
    
    else:
        evaluation = evaluate_white(board) - evaluate_black(board)
        return evaluation
