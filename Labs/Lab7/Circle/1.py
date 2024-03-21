import pygame

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
done = False
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
mycolors = [black, red, green, blue, white]  # List of colors
current_color_index = 0
current_bgcolor_index = 0
x = y = 30
speed = 6  # Speed variable
radius = 25
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                current_color_index = (current_color_index + 1) % len(mycolors)  # Update color index
            elif event.key == pygame.K_RETURN:
                current_bgcolor_index = (current_bgcolor_index + 1) % len(mycolors)  # Update bgcolor index
            elif event.key == pygame.K_ESCAPE:
                done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and pressed[pygame.K_LEFT] and y > 0 and x > 0: 
        y -= speed**0.5
        x -= speed**0.5
    elif pressed[pygame.K_UP] and pressed[pygame.K_RIGHT] and y > 0 and x < screen_width - 50:
        y -= speed**0.5
        x += speed**0.5
    elif pressed[pygame.K_DOWN] and pressed[pygame.K_RIGHT] and x < screen_width - 50 and y < screen_height - 50:
        y += speed**0.5
        x += speed**0.5
    elif pressed[pygame.K_DOWN] and pressed[pygame.K_LEFT] and y < screen_height - 50 and x > 0:
        y += speed**0.5
        x -= speed**0.5
    else:
      if pressed[pygame.K_UP] and y > 0: y -= speed
      if pressed[pygame.K_DOWN] and y < screen_height - 50: y += speed
      if pressed[pygame.K_LEFT] and x > 0: x -= speed
      if pressed[pygame.K_RIGHT] and x < screen_width - 50: x += speed
    

    screen.fill(mycolors[current_bgcolor_index])  # Fill the screen with the background color
    pygame.draw.circle(screen, mycolors[current_color_index], (x + radius, y + radius), radius)

    pygame.display.flip()
    clock.tick(60)  # Limit to 30 frames per second

pygame.quit()
