import pygame
import os
import re
pygame.init()
done = False

window_width = 500 
window_height = 500
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
print(os.getcwd())
mus = os.chdir('music')
music = []
i = 0
for file in os.listdir(mus):
    music.append(file)
font = pygame.font.Font(None, 36)
volume = 0.5
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: #Пауза
                if pygame.mixer.music.get_busy():  
                    pygame.mixer.music.pause()  
                else:
                    pygame.mixer.music.unpause() 
            elif event.key == pygame.K_RIGHT: #Вперел
                i = (i+1)%len(music)
                pygame.mixer.music.load(music[i])
                pygame.mixer.music.play(0)
            elif event.key == pygame.K_LEFT : #Назад
                i = (i-1)%len(music)
                pygame.mixer.music.load(music[i])
                pygame.mixer.music.play(0)
            elif event.key == pygame.K_UP: #Громче
                volume = min(1.0, volume + 0.03)  
                pygame.mixer.music.set_volume(volume)
            elif event.key == pygame.K_DOWN : #Тише
                volume = max(0.0, volume - 0.03)  
                pygame.mixer.music.set_volume(volume)
           
    text_surface = font.render(re.sub(f".mp3", "", music[i]), True, (255,255,255))
    text_rect = text_surface.get_rect(center=(window_width // 2, window_height // 4))
    screen.fill((0,0,0))
    screen.blit(text_surface, text_rect)
    clock.tick(15)
    pygame.display.flip()
pygame.quit()
