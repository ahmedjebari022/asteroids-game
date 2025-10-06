from circleshape import CircleShape
import pygame 
from constants import SHOT_RADIUS,PLAYER_SHOOT_SPEED
class Shot(CircleShape):
    containers = ()
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius)
    def update(self,dt):
        self.position += self.velocity * dt

    def rotate(self,rotation):
         self.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED
        