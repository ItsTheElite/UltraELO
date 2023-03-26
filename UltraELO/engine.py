import chess
import evaluator


def search(board: chess.Board) -> str:

    board_copy = board.copy()

    first_evals = []
    first_moves = []

    for move in board_copy.legal_moves:

        board_copy.push(move)

        if board_copy.legal_moves.count() == 0:
            first_evals.append(evaluator.evaluate_pos(board_copy))
            first_moves.append(move)

            board_copy.pop()
            break

        second_evals = []
        second_moves = []

        for move2 in board_copy.legal_moves:

            board_copy.push(move2)

            if board_copy.legal_moves.count() == 0:
                second_evals.append(evaluator.evaluate_pos(board_copy))
                second_moves.append(move2)

                board_copy.pop()
                break

            third_evals = []
            third_moves = []

            for move3 in board_copy.legal_moves:

                board_copy.push(move3)

                if board_copy.legal_moves.count() == 0:
                    third_evals.append(evaluator.evaluate_pos(board_copy))
                    third_moves.append(move3)

                    board_copy.pop()
                    break

                third_evals.append(evaluator.evaluate_pos(board_copy))
                third_moves.append(move3)
                board_copy.pop()

            if board_copy.turn == chess.WHITE:
                second_evals.append(max(third_evals))
                second_moves.append(move2)
            
            elif board_copy.turn == chess.BLACK:
                second_evals.append(min(third_evals))
                second_moves.append(move2)

            board_copy.pop()

        if board_copy.turn == chess.WHITE:
            first_evals.append(max(second_evals))
            first_moves.append(move)

        elif board_copy.turn == chess.BLACK:
            first_evals.append(min(second_evals))
            first_moves.append(move)
        
        board_copy.pop()
    
    if board_copy.turn == chess.WHITE:
        move: chess.Move =  first_moves[first_evals.index(max(first_evals))]
        return move.uci()
    
    else:
        move: chess.Move =  first_moves[first_evals.index(min(first_evals))]
        return move.uci()
