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

    def __init__(self, player, alien_group, player_bullet_group, alien_bullet_group):
        """Initialize the game"""
        self.round_number = 1
        self.score = 0

        self.player = player
        self.alien_group = alien_group
        self.player_bullet_group = player_bullet_group
        self.alien_bullet_group = alien_bullet_group

        self.new_round_sound = pygame.mixer.Sound("new_round_sound.wav")
        self.breach_sound = pygame.mixer.Sound("breach.wav")
        self.alien_hit_sound = pygame.mixer.Sound("alien_hit.wav")
        self.player_hit_sound = pygame.mixer.Sound("player_hit_sound.wav")

        # Set Font
        self.font = pygame.font.Font("SPACEAGE.ttf",32)

    def update(self):
        """Update the game"""
        self.shift_aliens()
        self.check_collisions()
        self.check_round_complete()

    def draw(self):
        """Draw the HUD and other information to display"""
        WHITE = (255,255,255)
        #Set text color
        score_text = self.font.render("Score: " + str(self.score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.centerx = WINDOW_WIDTH//2
        score_rect.centery = 25

        round_text = self.font.render("Round: " + str(self.round_number), True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topleft = (20, 10)

        lives_text = self.font.render("Lives: " + str(self.player.lives), True, WHITE)
        lives_rect = lives_text.get_rect()
        lives_rect.topright = (WINDOW_WIDTH - 20, 10)

        display_surface.blit(score_text,score_rect)
        display_surface.blit(round_text,round_rect)
        display_surface.blit(lives_text, lives_rect)

        pygame.draw.line(display_surface,WHITE, (0,50), (WINDOW_WIDTH,50),4)
        pygame.draw.line(display_surface,WHITE, (0,WINDOW_HEIGHT-100), (WINDOW_WIDTH,WINDOW_HEIGHT-100))


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
        pygame.mixer.Sound("new_round_sound.wav")


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
        #check if user wants to move
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity

    def fire(self):
        """"Fire a laser"""
        # Restrict the number of bullets on screen at a given time
        if len(self.bullet_group) < 4:
            self.shoot_sound.play()
            player_bullet = PlayerBullet(self.rect.centerx, self.rect.top, self.bullet_group)

    def reset(self):
        self.lives = 3
        self.rect.centerx = WINDOW_WIDTH//2

class Alien(pygame.sprite.Sprite):
    """A class to model an enemy alien"""

    def __init__(self, x, y, velocity, bullet_group):
        """Initialize the alien"""
        super().__init__()
        self.image = pygame.image.load("alien.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.starting_x = x
        self.starting_y = y

        self.direction = 1
        self.velocity = velocity
        self.bullet_group = bullet_group
        self.shoot_sound = pygame.mixer.Sound("alien_laser_sound.wav")


    def update(self):
        """Update the alien"""
        self.rect.x += self.direction * self.velocity
        
        if random.randint(0,1000) > 998 and len(self.bullet_group) < 3:
            self.shoot_sound.play()
            self.fire()
            
        #self.direction *= -1
    
    def fire(self):
        """Fire a laser"""
        AlienBullet(self.rect.centerx, self.rect.centery, self.bullet_group)

    def reset(self):
        """Reset the position"""
        self.rect.topleft = (self.starting_x, self.starting_y)
        self.direction = 1

class PlayerBullet(pygame.sprite.Sprite):
    """A class to model the bullet fired by the player"""

    def __init__(self, x, y, bullet_group):
        """Initialize the bullet based on (x,y) of the ship location"""
        super().__init__()
        self.image = pygame.image.load("green_laser.jpg")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.velocity = 10
        bullet_group.add(self)

    def update(self):
        """Update the bullet"""
        self.rect.y -= self.velocity

        #if the bullet is off the screen, remove from the bullet_group
        if self.rect.bottom < 0:
            self.kill()

class AlienBullet(pygame.sprite.Sprite):
    """A class to model the bullet fired by the alien"""

    def __init__(self, x, y, bullet_group):
        """Initialize the bullet"""
        super().__init__()
        self.image = pygame.image.load("red_laser.jpg")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.velocity = 3
        bullet_group.add(self)

    def update(self):
        """Update the bullet"""
        self.rect.y += self.velocity
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()

# Create the bullet groups
my_player_bullet_group = pygame.sprite.Group()
my_alien_bullet_group = pygame.sprite.Group()

# Create a player group
my_player_group = pygame.sprite.Group()
my_player = Player(my_player_bullet_group)
my_player_group.add(my_player)

# Create an alien group. Add alien objects via the game's start new round method
my_alien_group = pygame.sprite.Group()
for i in range(10):
    alien = Alien(64+i*64, 100, 1, my_alien_bullet_group)
    my_alien_group.add(alien)

# Create a game object
my_game = Game(my_player, my_alien_group, my_player_bullet_group, my_alien_bullet_group)

# Run the game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.fire()

    display_surface.fill((0,0,0))

    my_player_group.update()
    my_player_group.draw(display_surface)

    my_alien_group.update()
    my_alien_group.draw(display_surface)

    my_player_bullet_group.update()
    my_player_bullet_group.draw(display_surface)

    my_alien_bullet_group.update()
    my_alien_bullet_group.draw(display_surface)
 
    my_game.update()
    my_game.draw()

    pygame.display.update()
    clock.tick(FPS)

# End the game
pygame.quit()