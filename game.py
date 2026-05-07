import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('ARK ISLAND')
clock = pygame.time.Clock()
font = pygame.font.Font('fonts/MTF Toast.ttf',50)

sky_surface = pygame.image.load('graphics/daysky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = font.render('my game',False,'yellow')

vorg_surface = pygame.image.load('graphics/orc.png').convert_alpha()
vorg_x_pos = 50

# smaller size
vorg = pygame.transform.scale(vorg_surface, (96, 96))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,350))
    screen.blit(text_surface,(350,0))
    vorg_x_pos += 2
    if vorg_x_pos == 800: 
        vorg_x_pos= 0

    screen.blit(vorg,(vorg_x_pos,280))

    pygame.display.update()
    clock.tick(60)