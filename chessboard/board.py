import pygame
from .piece import Piece
from .evaluate import *

class Board:

   def __init__(self) -> None:
      self.width = 1200 # board is 800x800, with 400 extra pixels for everything else
      self.height = 800
      self.screen = None
      self.timer = None
      self.font = None
      self.fps = 60
      self.selected = ()
      self.turn = 1

      self.board = [['' for _ in range(8)] for _ in range(8)]

      self.image_loader = {
         'wp': './chessboard/images/Chess_plt60.png',
         'bp': './chessboard/images/Chess_pdt60.png',
         'wr': './chessboard/images/Chess_rlt60.png',
         'br': './chessboard/images/Chess_rdt60.png',
         'wn': './chessboard/images/Chess_nlt60.png',
         'bn': './chessboard/images/Chess_ndt60.png',
         'wb': './chessboard/images/Chess_blt60.png',
         'bb': './chessboard/images/Chess_bdt60.png',
         'wk': './chessboard/images/Chess_klt60.png',
         'bk': './chessboard/images/Chess_kdt60.png',
         'wq': './chessboard/images/Chess_qlt60.png',
         'bq': './chessboard/images/Chess_qdt60.png'
      }


      self.fill_board()
      self.create_window()

      self.game_state = (self.board, [], [], 0, 0, '')
      print(get_all_moves(self.game_state).keys())

   def fill_board(self):
      major_pieces = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
      for i, j in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
         # black pieces
         self.board[0][i] = Piece(0, j + '8', major_pieces[i])
         self.board[1][i] = Piece(0, j + '7', 'p')

         # white pieces
         self.board[6][i] = Piece(1, j + '2', 'p')
         self.board[7][i] = Piece(1, j + '1', major_pieces[i])

   def draw_board(self):
      # chessboard
      for j in range(8):
         for i in range(8):
            color = 'white' if (i + j) % 2 == 0 else 'brown'
            pygame.draw.rect(self.screen, color, [100 * i, 100*j, 100, 100])
            if self.selected and i == self.selected[0] and j == self.selected[1]:
               pygame.draw.rect(self.screen, 'red', [100 * i, 100 * j, 100, 100])
            # pieces
            square = str(self.board[j][i])[:2]
            if square:
               image = self.image_loader[square]
               piece = pygame.image.load(image).convert_alpha()
               self.screen.blit(piece, (100*i + 20, 100 * j + 20))

   def get_ownership(self, item):
      if isinstance(item, str):
         return None
      return item.ownership

   def handle_click(self, event):
      x, y = event.pos[0] // 100, event.pos[1] // 100
      # for now don't count outside board hits
      if (x > 8 or y > 8):
         return

      selected_turn = self.get_ownership(self.board[self.selected[1]][self.selected[0]]) if self.selected else None
      new_turn = self.get_ownership(self.board[y][x])

      # selected piece is your piece
      if selected_turn == self.turn % 2:
         # unselect your piece
         if self.selected == (x, y):
            self.selected = ()
         # click a different piece
         elif self.selected == () or selected_turn == new_turn:
            self.selected = (x, y)
         # move piece
         else:
            self.board[y][x] = self.board[self.selected[1]][self.selected[0]]
            self.board[self.selected[1]][self.selected[0]] = ''
            self.selected = ()
            self.turn += 1
      # first click
      else:
         self.selected = (x,y) if new_turn == self.turn % 2 else ()

   def create_window(self):
      pygame.init()
      pygame.font.init()
      self.font = pygame.font.SysFont('Arial', 30)
      self.screen = pygame.display.set_mode([self.width, self.height])
      pygame.display.set_caption('Crazyhouse Chess Board')
      self.timer = pygame.time.Clock()

      run = True
      while run:
         self.timer.tick(self.fps)

         self.draw_board()

         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
               self.handle_click(event)
         
         pygame.display.flip()
