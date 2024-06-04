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

# Set the defaults
PLAYER_STARTING_LIVES = 3

score = 0
player_lives = PLAYER_STARTING_LIVES


# Run the game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #check if user wants to move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 64:
        pass
    if keys[pygame.K_RIGHT] and player_rect.right < WINDOW_HEIGHT:
        pass

    pygame.display.update()
    clock.tick(FPS)


pygame.quit()



GREEN = (0,255,0)
DARKGREEN = (10,50,10)
WHITE = (255,255,255)
BLACK = (0,0,0)

font = pygame.font.SysFont('Lucidasans', 32)
score_text = font.render("Score: " + str(score),True,GREEN,DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10,10)

title_text = font.render("Feed the Dragon", True, GREEN, WHITE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10

lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARKGREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

game_over_text = font.render("GAMEOVER", True, GREEN, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to play again", True, GREEN, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

coin_sound = pygame.mixer.Sound("explosion.wav")
miss_sound = pygame.mixer.Sound("firemissile.wav")
miss_sound.set_volume(.1)
pygame.mixer.music.load("background.wav")

#Set images
player_image = pygame.image.load("dragon_right.png")
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT//2

coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
coin_rect.y = random.randint(64, WINDOW_HEIGHT)


#main game loop
pygame.mixer.music.play(-1,0.0)

        
    #Move the coin
    if coin_rect.x < 0:
        #Player missed the coin
        player_lives -= 1
        miss_sound.play()
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)
    else:
        coin_rect.x -= coin_velocity

    #check for collisions
    if player_rect.colliderect(coin_rect):
        score+=1
        coin_sound.play()
        coin_velocity+=COIN_ACCELERATION
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)

        
    score_text = font.render("Score: " + str(score), True, GREEN, DARKGREEN)
    lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARKGREEN)

    #check for gameover
    if player_lives == 0:
        display_surface.blit(game_over_text,game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        #Pause the game until the player presses a key, then reset the game

        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                #if the player wants to play again
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    player_rect.y = WINDOW_HEIGHT//2
                    coin_velocity = COIN_STARTING_VELOCITY
                    pygame.mixer.music.play(-1,0.0)
                    is_paused = False
                #if the player wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False
                    
    display_surface.fill(BLACK)

    #blit the HUD to screen
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)
    pygame.draw.line(display_surface, WHITE, (0,64), (WINDOW_WIDTH,64), 2)

    #blit the assets to the screen
    display_surface.blit(player_image, player_rect)
    display_surface.blit(coin_image, coin_rect)