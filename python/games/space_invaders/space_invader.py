import pygame, random


pygame.init()

# Set Display
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("SPACE INVADERS")

# Set the Clock
FPS = 60
clock = pygame.time.Clock()

# Define the classes
class Game():
    """A class to help control and update the gameplay"""

    def __init__(self):
        """Initialize the game"""
        pass

    def update(self):
        """Update the game"""
        pass

    def draw(self):
        """Draw the HUD and other information to display"""
        pass

    def shift_aliens(self):
        """Shift a weave of aliens down the screen and reverse direction"""
        pass

    def check_collisions(self):
        """Check for collisions"""
        pass

    def check_round_complete(self):
        """Check to see if the round is complete"""
        pass

    def check_game_status(self):
        """Check to see the status of the game and how the player died"""
        pass

    def pause_game(self):
        """Pause the game"""
        pass

    def reset_game(self):
        """Reset the game to beginning"""
        pass

    def start_new_round(self):
        """Start a new round"""
        pass


class Player(pygame.sprite.Sprite):
    """A class to model a spaceship the user can control"""

    def __init__(self, bullet_group):
        """Initialize the player"""
        super().__init__()
        self.image = pygame.image.load("spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT

        self.lives = 3
        self.velocity = 8
        self.bullet_group = bullet_group

        self.shoot_sound = pygame.mixer.Sound("laser_sound.wav")

    def update(self):
        """Update the player"""
        pass

    def fire(self):
        """Update the player"""
        pass

    def reset(self):
        """"Fire a laser"""
        pass

class alien(pygame.sprite.Sprite):
    """A class to model an enemy alien"""

    def __init__(self):
        """Initialize the alien"""
        pass

    def update(self):
        """Update the alien"""
        pass

    def fire(self):
        """Fire a laser"""
        pass

    def reset(self):
        """Reset the position"""
        pass

class PlayerBullet(pygame.sprite.Sprite):
    """A class to model the bullet fired by the player"""

    def __init__(self):
        """Initialize the bullet"""
        pass

    def update(self):
        """Update the bullet"""

class AlienBullet(pygame.sprite.Sprite):
    """A class to model the bullet fired by the alien"""

    def __init__(self):
        """Initialize the bullet"""
        pass

    def update(self):
        """Update the bullet"""

# Create the bullet groups
my_player_bullet_group = pygame.sprite.Group()
my_alien_bullet_group = pygame.sprite.Group()

# Create a player group
my_player_group = pygame.sprite.Group()
my_player = Player(my_player_bullet_group)
my_player_group.add(my_player)

# Create an alien group. Add alien objects via the game's start new round method
my_alien_group = pygame.sprite.Group()

# Create a game object
my_game = Game()

# Run the game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill((0,0,0))

    my_player_group.update()
    my_player_group.draw(display_surface)

    my_alien_bullet_group.update()
    my_alien_group.draw(display_surface)

    my_player_bullet_group.update()
    my_player_bullet_group.draw()
    my_alien_bullet_group.update()
    my_alien_bullet_group.draw()
 
    my_game.update()
    my_game.draw()

    #check if user wants to move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 64:
        pass
    if keys[pygame.K_RIGHT] and player_rect.right < WINDOW_HEIGHT:
        pass

    pygame.display.update()
    clock.tick(FPS)

# End the game
pygame.quit()