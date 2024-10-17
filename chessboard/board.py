
import pygame



class Board:
   """
      Constructor for board
      param:
         flipped - determine whether board should be flipped
   """
   def __init__(self) -> None:
      self.width = 2000
      self.height = 800
      self.screen = None
      self.timer = None
      self.font = None
      self.fps = 60

      self.create_window()


   def draw_board(self):
      for j in range(8):
         for i in range(8):
            color1 = 'white' if (i+j) % 2 == 0 else 'brown'
            color2 = 'white' if (i+j+1) % 2 == 0 else 'brown'
            pygame.draw.rect(self.screen, color1, [100 * i, 100*j, 100, 100])
            pygame.draw.rect(self.screen, color2, [100 * i + 1200, 100*j, 100, 100])



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
         