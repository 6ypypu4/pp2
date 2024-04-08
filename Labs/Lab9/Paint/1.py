import pygame
import math

pygame.init()
clock = pygame.time.Clock()

# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Размеры кисти и ластика
BRUSH_SIZE = 10
ERASER_SIZE = 20

# Текущий цвет
current_color = BLACK

# Функции для рисования прямоугольника
def draw_rect(surface, color, start_pos, end_pos):
    pygame.draw.rect(surface, color, pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])))

# Функция для рисования круга
def draw_circle(surface, color, center, radius):
    pygame.draw.circle(surface, color, center, radius)

# Функция для рисования квадрата
def draw_square(surface, color, start_pos, end_pos):
    width = abs(end_pos[0] - start_pos[0])
    height = abs(end_pos[1] - start_pos[1])
    size = min(width, height)
    if end_pos[0] < start_pos[0]:
        start_pos = (start_pos[0] - size, start_pos[1])
    if end_pos[1] < start_pos[1]:
        start_pos = (start_pos[0], start_pos[1] - size)
    pygame.draw.rect(surface, color, pygame.Rect(start_pos, (size, size)))

# Функция для рисования прямоугольного треугольника
def draw_right_triangle(surface, color, start_pos, end_pos):
    width = abs(end_pos[0] - start_pos[0])
    height = abs(end_pos[1] - start_pos[1])
    if end_pos[0] < start_pos[0]:
        start_pos = (start_pos[0] - width, start_pos[1])
    if end_pos[1] < start_pos[1]:
        start_pos = (start_pos[0], start_pos[1] - height)
    pygame.draw.polygon(surface, color, [start_pos, (start_pos[0] + width, start_pos[1]), end_pos])

# Функция для рисования равностороннего треугольника
def draw_equilateral_triangle(surface, color, start_pos, end_pos):
    side_length = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
    height = math.sqrt(3) / 2 * side_length
    if end_pos[0] < start_pos[0]:
        start_pos = (start_pos[0] - side_length, start_pos[1])
    if end_pos[1] < start_pos[1]:
        start_pos = (start_pos[0], start_pos[1] - height)
    pygame.draw.polygon(surface, color, [start_pos, (start_pos[0] + side_length / 2, start_pos[1] + height),
                                         (start_pos[0] + side_length, start_pos[1])])

# Функция для рисования ромба
def draw_rhombus(surface, color, start_pos, end_pos):
    width = abs(end_pos[0] - start_pos[0])
    height = abs(end_pos[1] - start_pos[1])
    if end_pos[0] < start_pos[0]:
        start_pos = (start_pos[0] - width, start_pos[1])
    if end_pos[1] < start_pos[1]:
        start_pos = (start_pos[0], start_pos[1] - height)
    pygame.draw.polygon(surface, color, [(start_pos[0] + width / 2, start_pos[1]),
                                         (end_pos[0], start_pos[1] + height / 2),
                                         (start_pos[0] + width / 2, start_pos[1] + height),
                                         (start_pos[0], start_pos[1] + height / 2)])

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Простой Paint")

left_button_pressed = False
right_button_pressed = False
drawing_mode = "brush"  
start_pos = (0, 0)  
screen.fill(WHITE)

# Основной цикл приложения
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                left_button_pressed = True
                start_pos = event.pos
            elif event.button == 3:  # Правая кнопка мыши
                right_button_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                left_button_pressed = False
            elif event.button == 3:
                right_button_pressed = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # R - рисовать прямоугольник
                drawing_mode = "rect"
            elif event.key == pygame.K_c:  # C - рисовать круг
                drawing_mode = "circle"
            elif event.key == pygame.K_e:  # E - использовать ластик
                drawing_mode = "eraser"
            elif event.key == pygame.K_b:  # B - выбрать кисть
                drawing_mode = "brush"
            elif event.key == pygame.K_k:  # K - выбрать черный цвет
                current_color = BLACK
            elif event.key == pygame.K_w:  # W - выбрать белый цвет
                current_color = WHITE
            elif event.key == pygame.K_r:  # R - выбрать красный цвет
                current_color = RED
            elif event.key == pygame.K_g:  # G - выбрать зеленый цвет
                current_color = GREEN
            elif event.key == pygame.K_l:  # L - выбрать синий цвет
                current_color = BLUE
            elif event.key == pygame.K_s:  # S - рисовать квадрат
                drawing_mode = "square"
            elif event.key == pygame.K_t:  # T - рисовать прямоугольный треугольник
                drawing_mode = "right_triangle"
            elif event.key == pygame.K_u: # U - рисовать равносторонний треугольник
                drawing_mode = "equilateral_triangle"
            elif event.key == pygame.K_h: # H - рисовать ромб
                drawing_mode = "rhombus"
    # Отрисовка
    if left_button_pressed or right_button_pressed:
      if drawing_mode == "brush":#
        if left_button_pressed:
            pygame.draw.circle(screen, current_color, pygame.mouse.get_pos(), BRUSH_SIZE)
        elif right_button_pressed:
            pygame.draw.circle(screen, WHITE, pygame.mouse.get_pos(), BRUSH_SIZE*5)
      elif drawing_mode == "rect":#
        if left_button_pressed:
            draw_rect(screen, current_color, start_pos, pygame.mouse.get_pos())
      elif drawing_mode == "circle": #
        if left_button_pressed:
            radius = ((pygame.mouse.get_pos()[0] - start_pos[0])**2 + (pygame.mouse.get_pos()[1] - start_pos[1])**2)**0.5
            draw_circle(screen, current_color, start_pos, int(radius))
      elif drawing_mode == "eraser":#
        if left_button_pressed:
            pygame.draw.circle(screen, WHITE, pygame.mouse.get_pos(), ERASER_SIZE)
      elif drawing_mode == "square":#
        if left_button_pressed:
            draw_square(screen, current_color, start_pos, pygame.mouse.get_pos())
      elif drawing_mode == "right_triangle":
        if left_button_pressed:
            draw_right_triangle(screen, current_color, start_pos, pygame.mouse.get_pos())
      elif drawing_mode == "equilateral_triangle":#
        if left_button_pressed:
            draw_equilateral_triangle(screen, current_color, start_pos, pygame.mouse.get_pos(),)
      elif drawing_mode == "rhombus":
        if left_button_pressed:
            draw_rhombus(screen, current_color, start_pos, pygame.mouse.get_pos())
    pygame.display.flip()
    clock.tick(60)  
