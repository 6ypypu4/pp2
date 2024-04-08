import pygame
import os
import random

# Определение констант
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
ROAD_LANE_WIDTH = 120
i = 0

# Установка рабочей директории
os.chdir("resources")
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
done = False

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
grey = (70, 70, 70)
yellow = (255, 255, 0)

font = pygame.font.Font(None, 36)

# Определение объектов
class Player:
    speed = 6
    car = pygame.image.load("player_sprite.png")
    width = car.get_width()
    height = car.get_height()

class Enemy:
    speed = 3
    car = pygame.image.load("enemy_sprite.png")
    width = car.get_width()
    height = car.get_height()

class Coin:
    width = 20
    height = 20
    coin_image = pygame.image.load("coin_sprite.png")

# Установка начальных позиций
player_pos_x = (SCREEN_WIDTH - Player.width) // 2
player_pos_y = SCREEN_HEIGHT - Player.height - 5
rect_pos_y = 0
game_condition = True  # В меню / в игре
enemy_pos_y = 0 
enemy_pos_x = random.randint(10, SCREEN_WIDTH - Enemy.width - 10)
cars_passed = 0
coins_collected = 0
coins_collected = 0
coins = []

# Функции отрисовки
def draw_background():
    global rect_pos_y
    rect_pos_y = (rect_pos_y + Player.speed) % SCREEN_HEIGHT
    screen.fill(grey)
    pygame.draw.rect(screen, yellow, pygame.Rect(10, 0, 5, SCREEN_HEIGHT))
    pygame.draw.rect(screen, white, pygame.Rect(SCREEN_WIDTH//2-5, 0, 5, SCREEN_HEIGHT))
    pygame.draw.rect(screen, white, pygame.Rect(SCREEN_WIDTH//2+5, 0, 5, SCREEN_HEIGHT))
    pygame.draw.rect(screen, yellow, pygame.Rect(SCREEN_WIDTH - 10, 0, 5, SCREEN_HEIGHT))

    for n in range(0, SCREEN_HEIGHT, ROAD_LANE_WIDTH):
        pygame.draw.rect(screen, white, pygame.Rect(SCREEN_WIDTH//4 + 5, (rect_pos_y + n) % SCREEN_HEIGHT, 15, 80))
        pygame.draw.rect(screen, white, pygame.Rect(SCREEN_WIDTH - SCREEN_WIDTH//4 - 5, (rect_pos_y + n) % SCREEN_HEIGHT, 15, 80))
        pygame.draw.rect(screen, white, pygame.Rect(SCREEN_WIDTH//4 + 5, (rect_pos_y + n) % SCREEN_HEIGHT - ROAD_LANE_WIDTH, 15, 80))
        pygame.draw.rect(screen, white, pygame.Rect(SCREEN_WIDTH - SCREEN_WIDTH//4 - 5, (rect_pos_y + n) % SCREEN_HEIGHT - ROAD_LANE_WIDTH, 15, 80))

def draw_player():
    screen.blit(Player.car, (player_pos_x, player_pos_y))

def draw_enemy():
    screen.blit(Enemy.car, (enemy_pos_x, enemy_pos_y - Enemy.height))

def draw_hud():
    global cars_passed, coins_collected
    carsnum = font.render(str(cars_passed), True, white)
    coinsnum = font.render(str(coins_collected), True, white)
    screen.blit(carsnum, carsnum.get_rect(topleft=(15, 10)) )
    screen.blit(coinsnum, coinsnum.get_rect(topright=(SCREEN_WIDTH - 15 , 10)) ) 

def draw_coins():
    for coin in coins:
        screen.blit(Coin.coin_image, coin)

# Функции движения
def move_player():
    pressed = pygame.key.get_pressed()
    global player_pos_x, Player
    if pressed[pygame.K_LEFT] and player_pos_x > 0:
        player_pos_x -= (Player.speed + 1)
    if pressed[pygame.K_RIGHT] and player_pos_x < SCREEN_WIDTH - Player.width:
        player_pos_x += Player.speed + 1

def move_enemy():
    global enemy_pos_y, enemy_pos_x, cars_passed, Enemy
    if enemy_pos_y < Player.speed + Enemy.speed:
        enemy_pos_x = random.randint(10, SCREEN_WIDTH - Enemy.width - 10)
        cars_passed = cars_passed + 1
        Enemy.speed = Enemy.speed + 0.1
        if cars_passed % 5 == 0:
            Enemy.speed = Enemy.speed + 1
    enemy_pos_y = (enemy_pos_y + Enemy.speed + Player.speed) % (SCREEN_HEIGHT + Enemy.height) 

def move_coins():
    global coins_collected, Player
    for coin in coins:
        coin[1] += Player.speed
        if coin[1] > SCREEN_HEIGHT:
            coins.remove(coin)
        coin_rect = pygame.Rect(coin[0], coin[1], Coin.width, Coin.height)
        player_rect = pygame.Rect(player_pos_x, player_pos_y, Player.width, Player.height)
        if player_rect.colliderect(coin_rect):
            coins.remove(coin)
            coins_collected += 1
            Player.speed = max(1,Player.speed + random.randrange(-1,2))





def check_collision():
    global enemy_pos_x, enemy_pos_y, player_pos_x, player_pos_y, game_condition, cars_passed, coins_collected
    player_rect = pygame.Rect(player_pos_x, player_pos_y, Player.width, Player.height)
    enemy_rect = pygame.Rect(enemy_pos_x, enemy_pos_y - Enemy.height, Enemy.width, Enemy.height)
    if player_rect.colliderect(enemy_rect):
        game_condition = not game_condition
        cars_passed = 0
        coins_collected = 0
        pygame.time.delay(10)
# Функции меню и игрового экрана
def handle_menu_screen():
    global enemy_pos_y, enemy_pos_x, player_pos_x
    enemy_pos_y = 0
    enemy_pos_x = random.randint(10, SCREEN_WIDTH - Enemy.width - 10)
    text_surface = font.render("You're dead", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
    screen.fill((0, 0, 0))
    screen.blit(text_surface, text_rect)







def handle_game_screen():
    move_player()
    move_enemy()
    move_coins()
    draw_background()
    check_collision()
    draw_player()
    draw_enemy()
    draw_coins()
    draw_hud()

def generate_coins():
    if random.randint(0, 100) < 2:  
        coins.append([random.randint(10, SCREEN_WIDTH - Coin.width - 10), 0])

# Основной игровой цикл
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               game_condition = not game_condition
    if game_condition:
      handle_menu_screen()
    else:
      handle_game_screen()
      generate_coins()

    pygame.display.flip()
    clock.tick(60)  

        