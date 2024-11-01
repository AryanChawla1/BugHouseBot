# evaluate game state functions
from typing import List, Tuple
from .piece import Piece

def to_chess(row, col):
    """converts 2D array indices to chess notation (A8 or B1)."""
    column_letter = chr(ord('A') + col)  # convert column number to letter
    row_number = 8 - row                 # convert row number 
    return f"{column_letter}{row_number}"

def to_index(notation):
    """converts chess notation to 2D array indices ((0, 0), (1, 7))"""
    col = ord(notation[0].upper()) - ord('A')  # convert letter to column index 
    row = 8 - int(notation[1])                 # convert number to row index 
    return row, col

def get_all_moves(gamestate: Tuple[List[List[Piece | str]], List[str], List[str], bool, bool, str]):
    board, w_taken, b_taken, w_castle, b_castle, latest_move = gamestate
    all_moves = {}
    player = 1 if latest_move == '' or latest_move[0] == 'b' else 0
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if isinstance(piece, Piece) and piece.ownership == player:

                moves = get_moves(piece, board, w_castle, b_castle)

                for move in moves:
                    new_board = [row[:] for row in board] # deep copy
                    new_board[move[0]][move[1]] = piece 
                    new_board[row][col] = ''
                    new_gamestate = (new_board, w_taken, b_taken, w_castle, b_castle, to_chess(*move))
                    if in_check(new_board, player):
                        continue
                    move_notation = f"{piece.id}{to_chess(*move)}"
                    all_moves[move_notation] = new_gamestate

    return all_moves

def get_moves(piece: Piece, board: List[List[Piece | str]], w_castle: bool, b_castle: bool):
    moves = []
    
    if piece.piece == 'p':
        moves.extend(pawn_moves(piece, board))

    return moves

def pawn_moves(piece: Piece, board: List[List[Piece | str]]):
    moves = []
    row, col = to_index(piece.location)
    direction = -1 if piece.ownership else 1 
    start = 6 if piece.ownership else 1
    if 0 <= row + direction < 8 and not board[row + direction][col]: # up one
        moves.append((row + direction, col))
    if row == start and 0 <= row + (direction * 2) < 8 and not board[row +  (direction * 2)][col]: # up two
        moves.append((row + (direction * 2), col))

    # en passant, promotion, capturing pieces to implement later
    
    return moves

def in_check(board: List[List[Piece | str]], player: int):
    ''' return if the player's king is in check based on the board '''
    return False