import pygame
from sys import exit

pygame.init()
screen= pygame.display.set_mode((800,400))
pygame.display.set_caption('ARK ISLAND')
clock=pygame.time.Clock()
sky_surface= pygame.image.load('graphics/daysky.png')
ground_surface= pygame.image.load('graphics/ground.png')
while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            exit()
    #draw all our elements
    #update everthing
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,350))
    pygame.display.update()
    clock.tick(60)
