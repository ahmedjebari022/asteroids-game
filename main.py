import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT,ASTEROID_MIN_RADIUS,ASTEROID_KINDS,ASTEROID_SPAWN_RATE,ASTEROID_MAX_RADIUS,PLAYER_RADIUS,PLAYER_TURN_SPEED
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    color = ""
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)
    asterfoidField = AsteroidField()
    print("Starting Asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    while 1 == 1 :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # player.update(dt)
        updatable.update(dt)
        for asteroid in asteroids:
            if player.check_colision(asteroid):
                print("Game over!")
                return
        screen.fill("black")
        # player.draw(screen)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
