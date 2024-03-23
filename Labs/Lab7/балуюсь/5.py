import pygame
import pygame.freetype
import time

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Определение размеров окна
WIDTH, HEIGHT = 400, 200

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text Input Example")

# Создание объекта для вывода текста
font = pygame.freetype.Font(None, 24)

# Определение состояния поля ввода
input_active = False
input_text = ''
cursor_visible = True
cursor_blink_interval = 0.5
last_blink = time.time()

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # При клике на поле ввода активируется ввод текста
            if input_rect.collidepoint(event.pos):
                input_active = True
            else:
                input_active = False
        elif event.type == pygame.KEYDOWN:
            # Обработка ввода текста
            if input_active:
                if event.key == pygame.K_RETURN:
                    print(input_text)
                    input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    # Мигание курсора
    current_time = time.time()
    if current_time - last_blink > cursor_blink_interval:
        cursor_visible = not cursor_visible
        last_blink = current_time

    # Очистка экрана
    screen.fill(WHITE)

    # Создание прямоугольника для поля ввода
    input_rect = pygame.Rect(50, 50, 300, 30)

    # Отображение рамки поля ввода
    pygame.draw.rect(screen, BLACK, input_rect, 2)

    # Определение координат для выравнивания текста по нижней границе
    text_width, text_height = font.get_rect(input_text)[2:]
    text_x = input_rect.x + 5
    text_y = input_rect.y + input_rect.height - text_height - 5

    # Отображение текста в поле ввода
    font.render_to(screen, (text_x, text_y), input_text, BLACK)

    # Отображение мигающего курсора
    if input_active and cursor_visible:
        cursor_pos = text_x + text_width
        pygame.draw.line(screen, BLACK, (cursor_pos, input_rect.y + 5),
                         (cursor_pos, input_rect.y + input_rect.height - 5), 2)

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
