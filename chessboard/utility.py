

def print_board(board):
   for line in board:
      print(line)

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