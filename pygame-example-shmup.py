
# pygame-example-shmup.py
# Shoot 'em up
# Jean C

import pygame as pg
import random

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 720
HEIGHT = 1000
SCREEN_SIZE = (WIDTH, HEIGHT)

# Enemy movement directions
LEFT = -1
RIGHT = 1


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/galaga_ship.png")
        self.image = pg.transform.scale(
            self.image, (self.image.get_width() // 2, self.image.get_height() // 2)
        )

        self.rect = self.image.get_rect()

    def update(self):
        """Follow the mouse"""
        self.rect.center = pg.mouse.get_pos()

        # Keep it at the bottom of the screen
        if self.rect.top < HEIGHT - 200:
            self.rect.top = HEIGHT - 200


class Bullet(pg.sprite.Sprite):
    def __init__(self, player_loc: list):
        """
        Params:
            player_loc: x,y coords of centerx and top
        """
        super().__init__()

        # Green rectangle
        self.image = pg.Surface((10, 25))
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()

        # Spawn at the Player
        self.rect.centerx = player_loc[0]
        self.rect.bottom = player_loc[1]

    def update(self):
        """Move the bullet up and remove it if it goes off-screen"""
        self.rect.y -= 10
        if self.rect.bottom < 0:
            self.kill()


class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Red rectangle for the enemy
        self.image = pg.Surface((50, 30))
        self.image.fill(RED)

        self.rect = self.image.get_rect()
      

        self.speed = 5
        self.direction = RIGHT

    def update(self):
        """Move enemy side-to-side and change direction at edges"""
        self.rect.x += self.speed * self.direction
        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.direction *= -1


def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in these sprite Groups
    all_sprites = pg.sprite.Group()
    bullets = pg.sprite.Group()
    enemies = pg.sprite.Group()

    # Create the Player sprite object
    player = Player()
    all_sprites.add(player)

    # Create enemy sprites
    for _ in range(10):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    pg.display.set_caption("Shoot 'Em Up")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                bullet = Bullet((player.rect.centerx, player.rect.top))
                all_sprites.add(bullet)
                bullets.add(bullet)

        # --- Update the world state
        all_sprites.update()

        # Check for collisions between bullets and enemies
        hits = pg.sprite.groupcollide(bullets, enemies, True, True)

        # --- Draw items
        screen.fill(BLACK)

        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps

    pg.quit()


def main():
    start()


if __name__ == "__main__":
    main()