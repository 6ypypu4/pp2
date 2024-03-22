import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("Кнопка мыши нажата в точке ", event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                print("Кнопка мыши отпущена в точке ", event.pos)
            elif event.type == pygame.MOUSEMOTION:
                print("Движение мыши в точку:", event.pos)
                print("Изменение:", event.rel)
            elif event.type == pygame.MOUSEWHEEL:
                print("Вращение колесика:", event.y)
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
