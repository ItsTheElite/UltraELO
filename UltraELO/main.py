# UltraELO 1.0.0
import chess
import evaluator
import engine

import os


board = chess.Board()

os.system('TITLE UltraELO 1.0.0')
os.system('CLS')
os.system('COLOR F')


while not board.is_game_over():

    if board.turn == chess.WHITE:
        move = input('Move [SAN] (White): ')
    
    else:
        move = input('Move [SAN] (Black): ')
    
    try:
        move = board.push_san(move)
        print(f'Move Played - [{move.uci()}]')

        print(f'| Evaluation: {round(evaluator.evaluate_pos(board), 3)}')
        print(f'| Next Move: {engine.search(board)}\n')

    except:
        print('Invalid Move! (You can use UCI if SAN doesn\'t work)\n')
        continue


if board.is_checkmate():
    if board.turn == chess.WHITE:
        print('!--- BLACK WON ---!')
        input()
    
    else:
        print('!--- WHITE WON ---!')
        input()

elif board.is_stalemate():
    print('The Game Ended In A Stalemate, Noone Won!\n')
    input()

else:
    print('The Game Is A Draw, Noone Won!\n')
    input()
