# overwritten code we might reuse?

def get_all_moves(gamestate: Tuple[List[List[Piece | str]], List[str], List[str], bool, bool, str]):
    ''' Returns dictionary of key=move_notation, val=gamestate '''
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