import sys
import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids by exeCute")
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    font = pygame.font.Font(None, 36)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for member in updatable:
            member.update(dt)
        
        for asteroid in asteroids:
                if asteroid.check_collision(player):
                    print("Game Over!")
                    sys.exit()
                for shot in shots:
                    if asteroid.check_collision(shot):
                        score += 1
                        asteroid.split()
                        shot.kill()

        screen.fill("black")
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        
        for member in drawable:
            member.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
    