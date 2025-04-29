import pygame
from constants import *
from player import Player

def main():
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  
  pygame.init()
  clock = pygame.time.Clock()
  dt = 0
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
      
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  Player.containers = (updatable, drawable)
  
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2
  player = Player(x, y)
 
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    pygame.Surface.fill(screen, color=(0, 0, 0))
    
    for draw in drawable: 
      draw.draw(screen)
    updatable.update(dt)
    
    pygame.display.flip() 
    dt = clock.tick(60) / 1000.0
  
if __name__ == "__main__":
    main()
    
    