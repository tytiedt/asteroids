import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
  astroidable = pygame.sprite.Group()
  shootable = pygame.sprite.Group()
  Player.containers = (updatable, drawable)
  Asteroid.containers = (updatable, drawable, astroidable)
  AsteroidField.containers = updatable
  Shot.containers = (updatable, drawable, shootable)
  
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2
  player = Player(x, y)
  
  asteroid_field = AsteroidField()
 
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    pygame.Surface.fill(screen, color=(0, 0, 0))
    
    for draw in drawable: 
      draw.draw(screen)
    updatable.update(dt)
    
    for asteroid in astroidable:
      if player.collision(asteroid):
        print("Game over!")
        return
      for shot in shootable:
        if asteroid.collision(shot):
          asteroid.split()
          shot.kill()
          break
    
    pygame.display.flip() 
    dt = clock.tick(60) / 1000.0
  
if __name__ == "__main__":
    main()
    
    