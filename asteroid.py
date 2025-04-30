import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, NEW_ASTEROID_VELOCITY_RATE

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def draw(self, screen):
    pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
  def update(self, dt):
    self.position += self.velocity * dt
  
  def split(self):
    self.kill()
    if self.radius < ASTEROID_MIN_RADIUS:
      return
    spawn_angle = random.uniform(20, 50)
    original_velocity = self.velocity  
    new_velocity1 = original_velocity.rotate(spawn_angle)
    new_velocity2 = original_velocity.rotate(-spawn_angle)
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    
    asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid1.velocity = new_velocity1 * NEW_ASTEROID_VELOCITY_RATE
    asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid2.velocity = new_velocity2 * NEW_ASTEROID_VELOCITY_RATE
    
    return asteroid1, asteroid2