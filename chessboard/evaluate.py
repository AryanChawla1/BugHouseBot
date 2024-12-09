##############################
# FORMATTING NEEDS TO CHANGE #
##############################

'''
It'll be easier to have the gamestate passed along to each of the functions because that way we can edit the variables like w_taken right from the pawn_moves function.
When calculating which piece to take, 
'''

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
    ''' Returns dictionary of key=move_notation, val=gamestate '''
    board, w_taken, b_taken, w_castle, b_castle, latest_move = gamestate
    moves = {}
    player = 1 if latest_move == '' or latest_move[0] == 'b' else 0
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if isinstance(piece, Piece) and piece.ownership == player:
                if piece.piece == 'p':
                    moves.update((pawn_moves(piece, gamestate)))
                # elif piece.piece == 'r':
                    # moves.update((pawn_moves(piece, gamestate)))

    return moves # dictionary with key=move_notation, val=gamestate

def move(start: Tuple[int], end: Tuple[int], board: Tuple[List[List[Piece | str]]]):
    ''' move the piece, return board and captured piece, and evaluates if it is a check'''

    piece = board[start[0]][start[1]]
    player = piece.ownership
    captured = board[end[0]][end[1]]
    board[end[0]][end[1]] = piece
    piece.location = to_chess(end[0], end[1])
    board[start[0]][start[1]] = ''
    return board, captured, in_check(board, player)



def pawn_moves(piece: Piece, gamestate: Tuple[List[List[Piece | str]], List[str], List[str], bool, bool, str]):
    board, w_taken, b_taken, w_castle, b_castle, latest_move = gamestate
    moves = {}
    row, col = to_index(piece.location)
    direction = -1 if piece.ownership else 1 
    start = 6 if piece.ownership else 1
    if 0 <= row + direction < 8 and not board[row + direction][col]: # up one
        new_board, _, checked = move((row, col), (row + direction, col), [row[:] for row in board]) # move the piece
        if not checked:
            moves[f"{piece.id}{to_chess(row + direction, col)}"] = (new_board, w_taken, b_taken, w_castle, b_castle, latest_move)
        if row == start and 0 <= row + (direction * 2) < 8 and not board[row +  (direction * 2)][col]: # up two
            new_board, _, checked = move((row, col), (row + (direction * 2), col), [row[:] for row in board])
            if not checked:
                moves[f"{piece.id}{to_chess(row + (direction * 2), col)}"] = (new_board, w_taken, b_taken, w_castle, b_castle, latest_move)

    # capture pieces
    for d in [-1, 1]: # left and right side
        new_row, new_col = row + direction, col + d
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            if board[new_row][new_col] and board[new_row][new_col].ownership != piece.ownership:
                new_board, taken, checked = move((row, col), (new_row, new_col), [row[:] for row in board])
                if not checked:
                    if piece.ownership:
                        b_taken.append(taken)
                    else:
                        w_taken.append(taken)
                    moves[f"{piece.id}{to_chess(new_row, new_col)}"] = (new_board, w_taken, b_taken, w_castle, b_castle, latest_move)

    # en passant, promotion, capturing pieces to implement later
    
    return moves

def in_check(board: List[List[Piece | str]], player: int):
    ''' return if the player's king is in check based on the board '''
    return False