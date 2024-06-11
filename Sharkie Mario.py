# Sharkie Mario 
# Jean Chen, Albert Li
# 06/02/2024

import pygame as pg

# Global constants

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class Sharkie(pg.sprite.Sprite):
    # -- Methods
    def __init__(self):
        """ Constructor function """
        # Call the parent's constructor
        super().__init__()
        # Load Sharkie, Have it rotate between 4 sequences to create a walking effect 
        width = 40
        height = 60

        self.run_images = []
        self.jump_image = pg.image.load("./Images/Sharkie5.png")
        self.jump_image = pg.transform.scale(self.jump_image, (self.jump_image.get_width() * 5, self.jump_image.get_height() * 5))
        for i in range(4):
            # load the image
            img = pg.image.load(f"./Images/Sharkie{i+1}.png")

            # scale
            img = pg.transform.scale(img, (img.get_width() * 5, img.get_height() * 5))

            # add to images list
            self.run_images.append(img)

        self.image = pg.Surface([width, height])

        self.image_counter = 0
        self.image = self.run_images[self.image_counter]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.rect.inflate_ip(-120, 0)

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        self.walking = False
        self.jumping = False
        self.jump_count = 0

        # List of sprites we can bump against
        self.level = None

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        # Move up/down
        self.rect.y += self.change_y

        if self.walking:
            self.image_counter = (self.image_counter + 1) % 24
            self.image = self.run_images[self.image_counter // 6]

        if self.jumping:
            self.image = self.jump_image
        elif not self.jumping and not self.walking:
            self.image_counter = 0
            self.image = self.run_images[self.image_counter]

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y > 0:
            self.jumping = False

        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
            self.jump_count = 0  # Reset jump count when on the ground

    def jump(self):
        """ Called when user hits 'jump' button. """
        if self.jump_count < 30:
            self.change_y = -10
            self.jumping = True
            self.jump_count += 1

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.walking = True

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        self.walking = True

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        self.walking = False


class Box(pg.sprite.Sprite):
    # -- Methods
    def __init__(self, x, y):
        """ Constructor function """
        # Call the parent's constructor
        super().__init__()

        # Load the box image
        self.image = pg.image.load("./Images/box.png")
        # Scale down
        self.image = pg.transform.scale(
            self.image, (self.image.get_width() // 20, self.image.get_height() // 20)
        )

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class PopEffect(pg.sprite.Sprite):
    # -- Methods
    def __init__(self, x, y, image_path):
        """ Constructor function """
        super().__init__()
        self.image = pg.image.load(image_path)
        # self.image = pg.transform.scale(self.image, (self.image.get_width() // 10, self.image.get_height() // 10))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        """ Update the effect """
        pass  # Do nothing, so the image stays on screen


def start():
    """ Main Program """
    pg.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pg.display.set_mode((1280, 720), pg.FULLSCREEN)

    bg = pg.image.load("./Images/Background.png")

    pg.display.set_caption("SLSS LIPDUB 2024")

    # -- Sprite Groups
    all_sprites = pg.sprite.Group()
    boxes = pg.sprite.Group()
    effects = pg.sprite.Group()

    # Create the player
    player = Sharkie()

    # Create boxes at different locations
    box1 = Box(350, SCREEN_HEIGHT - 600)
    box2 = Box(540, SCREEN_HEIGHT - 460)
    box3 = Box(850, SCREEN_HEIGHT - 600)

    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height

    # Add player and boxes to sprite groups
    all_sprites.add(player)
    all_sprites.add(box1, box2, box3)
    boxes.add(box1, box2, box3)

    # Load different pop effect images
    pop_images = ["./Images/pop1.png", "./Images/pop2.png", "./Images/pop3.png"]
    box_effects = {box1: pop_images[0], box2: pop_images[1], box3: pop_images[2]}

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pg.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    player.go_left()
                if event.key == pg.K_RIGHT:
                    player.go_right()
                if event.key == pg.K_UP:
                    player.jump()

            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pg.K_RIGHT and player.change_x > 0:
                    player.stop()

        # Update all sprites
        all_sprites.update()

        # Check for collisions between player and boxes
        hits = pg.sprite.spritecollide(player, boxes, True)
        for hit in hits:
            effect = PopEffect(hit.rect.centerx, hit.rect.centery, box_effects[hit])
            all_sprites.add(effect)
            effects.add(effect)

        # # If the player gets near the right side, shift the world left (-x)
        # if player.rect.right > SCREEN_WIDTH:
        #     player.rect.right = SCREEN_WIDTH

        # # If the player gets near the left side, shift the world right (+x)
        # if player.rect.left < 0:
        #     player.rect.left = 0

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        screen.blit(bg, (0, 0))

        all_sprites.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pg.display.flip()

    # on exit.
    pg.quit()

if __name__ == "__main__":
    start()
