
# white = 1, black = 0

class Piece:

   static_id = 0

   def __init__(self, ownership, location, piece):
      self.ownership = ownership
      self.location = location
      self.piece = piece
      self.is_pawn = True if piece == 'p' else False
      self.id = Piece.static_id
      Piece.static_id += 1
   
   # ex: wpb5 (white, pawn, b5)
   def __str__(self):
      owner_string = 'w' if self.ownership else 'b'
      return owner_string + self.piece + self.location