import pygame, sys
from pygame.locals import *

pygame.init()
#DISPLAYSURF = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello, Pygame!")

BLUE = (0, 0, 255)
windowSurface = pygame.display.set_mode((500, 400), 0, 32)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)
    pygame.display.update()
