import sys
import pygame

pygame.init()

size = width, height = 1920, 1080
background = 255, 255, 255
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing ball")

font = pygame.font.Font('FreeSansBold.ttf', 32)



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        
