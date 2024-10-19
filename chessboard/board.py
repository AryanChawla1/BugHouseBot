
import pygame



class Board:


   def __init__(self) -> None:
      self.width = 2000
      self.height = 800
      self.screen = None
      self.timer = None
      self.font = None
      self.fps = 60

      self.board1 = [
         ['br', 'bk', 'bb', 'bq', 'bk', 'bb', 'bk', 'br'],
         ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
         ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
         ['wr', 'wk', 'wb', 'wq', 'wk', 'wb', 'wk', 'wr']
      ]
      self.board2 = [
         ['wr', 'wk', 'wb', 'wk', 'wq', 'wb', 'wk', 'wr'],
         ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
         ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
         ['br', 'bk', 'bb', 'bk', 'bq', 'bb', 'bk', 'br'],
      ]

      self.image_loader = {
         'wp': './chessboard/images/Chess_plt60.png',
         'bp': './chessboard/images/Chess_pdt60.png',
         'wr': './chessboard/images/Chess_rlt60.png',
         'br': './chessboard/images/Chess_rdt60.png',
         'wk': './chessboard/images/Chess_nlt60.png',
         'bk': './chessboard/images/Chess_ndt60.png',
         'wb': './chessboard/images/Chess_blt60.png',
         'bb': './chessboard/images/Chess_bdt60.png',
         'wk': './chessboard/images/Chess_klt60.png',
         'bk': './chessboard/images/Chess_kdt60.png',
         'wq': './chessboard/images/Chess_qlt60.png',
         'bq': './chessboard/images/Chess_qdt60.png'
      }


      self.create_window()


   def draw_board(self):
      # chessboard
      for j in range(8):
         for i in range(8):
            color1 = 'white' if (i+j) % 2 == 0 else 'brown'
            color2 = 'white' if (i+j+1) % 2 == 0 else 'brown'
            pygame.draw.rect(self.screen, color1, [100 * i, 100*j, 100, 100])
            pygame.draw.rect(self.screen, color2, [100 * i + 1200, 100*j, 100, 100])

      # pieces
      for j in range(8):
         for i in range(8):
            if self.board1[j][i]:
               piece = self.image_loader[self.board1[j][i]]
               load = pygame.image.load(piece).convert_alpha()
               self.screen.blit(load, (100*i + 20, 100 * j + 20))
            if self.board2[j][i]:
               piece = self.image_loader[self.board2[j][i]]
               load = pygame.image.load(piece).convert_alpha()
               self.screen.blit(load, (100*i + 1220, 100 * j + 20))


   def create_window(self):
      pygame.init()
      pygame.font.init()
      self.font = pygame.font.SysFont('Arial', 30)
      self.screen = pygame.display.set_mode([self.width, self.height])
      pygame.display.set_caption('Chess Board')
      self.timer = pygame.time.Clock()

      run = True
      while run:
         self.timer.tick(self.fps)

         self.draw_board()

         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
         
         pygame.display.flip()
