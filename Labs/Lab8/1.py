import pygame
import os
import random
import re
os.chdir("resources")
pygame.init()

screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
done = False
# Colors
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
grey = (70, 70, 70)
yellow = (255, 255, 0)

# Objects
class Player:
    width = 44
    height = 96
    speed = 6
    car = pygame.image.load("player_sprite.png")

class Enemy:
    width = 48
    height = 93
    speed = 3
    car = pygame.image.load("enemy_sprite.png")
#Подгружаю музыку:
mus = os.chdir('music')
music = []
i = 0
for file in os.listdir(mus):
    music.append(file)
font = pygame.font.Font(None, 36)
volume = 0.5

player_pos_x = (screen_width - Player.width) // 2
player_pos_y = screen_height - Player.height - 5
rect_pos_y = 0
game_condition = True  # In menu / in game
enemy_pos_y = 0 
enemy_pos_x = random.randint(10,screen_width - Enemy.width - 10)

#Game sceen
def background():
    global rect_pos_y
    rect_pos_y = (rect_pos_y + Player.speed)%600
    screen.fill(grey)
    pygame.draw.rect(screen, yellow, pygame.Rect(10, 0, 5, 600))
    pygame.draw.rect(screen, white, pygame.Rect(screen_width//2-5, 0, 5, 600))
    pygame.draw.rect(screen, white, pygame.Rect(screen_width//2+5, 0, 5, 600))
    pygame.draw.rect(screen, yellow, pygame.Rect(screen_width - 10, 0, 5, 600))

    for n in range(0,600, 120):
        pygame.draw.rect(screen, white, pygame.Rect(screen_width//4 + 5, (rect_pos_y + n )%600, 15, 80))
        pygame.draw.rect(screen, white, pygame.Rect(screen_width - screen_width//4 - 5, (rect_pos_y + n )%600, 15, 80))
        #I'm tired of trying to make it simpler(
        pygame.draw.rect(screen, white, pygame.Rect(screen_width//4 + 5, (rect_pos_y + n )%600 - 120, 15, 80))
        pygame.draw.rect(screen, white, pygame.Rect(screen_width - screen_width//4 - 5, (rect_pos_y + n )%600 - 120, 15, 80))
def player_movement():
    pressed = pygame.key.get_pressed()
    global player_pos_x, Player
    if pressed[pygame.K_LEFT] and player_pos_x > 0:
        player_pos_x -= (Player.speed + 1)
    if pressed[pygame.K_RIGHT] and player_pos_x < screen_width - Player.width:
        player_pos_x += Player.speed + 1
    if pressed[pygame.K_DOWN] and Player.speed >= 1.2:
        Player.speed -= 0.2
    if pressed[pygame.K_UP] and Player.speed <= 9.0:
        Player.speed += 0.2
def enemy_movement():
    global enemy_pos_y, enemy_pos_x
    if enemy_pos_y == 0 : enemy_pos_x = random.randint(10,screen_width - Enemy.width - 10) 
    enemy_pos_y = (enemy_pos_y + Enemy.speed + Player.speed)%(screen_height+Enemy.height) 
def check_collision():
    global enemy_pos_x, enemy_pos_y, player_pos_x, player_pos_y, game_condition
    player_rect = pygame.Rect(player_pos_x, player_pos_y, Player.width, Player.height)
    enemy_rect = pygame.Rect(enemy_pos_x, enemy_pos_y - Enemy.height, Enemy.width, Enemy.height)
    if player_rect.colliderect(enemy_rect):
        game_condition = not game_condition
        pygame.time.delay(1000)
        
def screen_game():
    player_movement()
    enemy_movement()
    background()
    check_collision()
    screen.blit(Player.car, (player_pos_x, player_pos_y))
    screen.blit(Enemy.car, (enemy_pos_x, enemy_pos_y - Enemy.height))

#Menu sceen
def musis_player(event):
    global volume, i
    if event.type == pygame.KEYDOWN:  # Проверяем, что это событие нажатия клавиши
        if event.key == pygame.K_RETURN:  # Пауза
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
        elif event.key == pygame.K_RIGHT:  # Вперел
            i = (i + 1) % len(music)
            pygame.mixer.music.load(music[i])
            pygame.mixer.music.play(0)
        elif event.key == pygame.K_LEFT:  # Назад
            i = (i - 1) % len(music)
            pygame.mixer.music.load(music[i])
            pygame.mixer.music.play(0)
        elif event.key == pygame.K_UP:  # Громче
            volume = min(1.0, volume + 0.03)
            pygame.mixer.music.set_volume(volume)
        elif event.key == pygame.K_DOWN:  # Тише
            volume = max(0.0, volume - 0.03)
            pygame.mixer.music.set_volume(volume)
    text_surface = font.render(re.sub(f".mp3", "", music[i]), True, (255,255,255))
    text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 4))
    screen.fill((0,0,0))
    screen.blit(text_surface, text_rect)
def screen_menu():
    global enemy_pos_y, enemy_pos_x, player_pos_x, event 
    enemy_pos_y = 0 
    enemy_pos_x = random.randint(10,screen_width - Enemy.width - 10)
    musis_player(event)


# Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_condition = not game_condition
    if game_condition:
        screen_menu()
    else:
        screen_game()

    pygame.display.flip()
    clock.tick(60)  

pygame.quit()
