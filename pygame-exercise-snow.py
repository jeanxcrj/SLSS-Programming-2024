#Snowflakes
#Jean
#04292024

import pygame
import random

# Constants
WIDTH = 1280  # Pixels
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Snowflake(pygame.sprite.Sprite):

    #drawing snow method stolen from mr ubial. 
    def __init__(self, width: int):
        """
        Params:
            width: width of snow in px
        """
        super().__init__()

        self.image = pygame.Surface((width, width))

        # Found by Duncan, he says Yippee!
        pygame.draw.circle(self.image, WHITE, (width // 2, width // 2), width // 2)


        self.rect = self.image.get_rect()

       #random position 
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(-100, -50)
        self.vel_y = random.choice([3, 4, 6, 9])  # Random vertical speed

    def update(self):
        # Move the snowflake vertically
        self.rect.y += self.vel_y

        # If the snowflake goes off the screen, reset its position
        if self.rect.y > HEIGHT:
            self.rect.y = random.randint(-100, -50)
            self.rect.x = random.randint(0, WIDTH)

def start():
    """Environment Setup and Game Loop"""
    pygame.init()

    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("SNOWFLAKES")

    clock = pygame.time.Clock()
    done = False

    all_sprites = pygame.sprite.Group()

    # Add snowflakes to the sprite group
    for _ in range(50):
        all_sprites.add(Snowflake(10))

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(BLACK)

        all_sprites.update()
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    start()
