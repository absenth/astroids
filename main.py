import pygame
from constants import *




def main():
    dt = 0

    pygame.init()
    Clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


            screen.fill("black")
            pygame.display.flip()
            tick_value = Clock.tick(60)
            dt = tick_value / 1000



if __name__ == "__main__":
    main()
