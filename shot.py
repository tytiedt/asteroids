from circleshape import CircleShape
from constants import SHOT_RADIUS 
import pygame

class Shot(CircleShape):
  def __init__(self, x, y, radius=SHOT_RADIUS):
    super().__init__(x, y, radius)
  
  def draw(self, screen):
    pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
  def update(self, dt):
    self.position += self.velocity * dt
  # def update(self, dt):
  #   self.position += self.velocity * dt
  