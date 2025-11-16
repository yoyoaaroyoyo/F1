import pygame

w = 600
h = 337
x = 100
y = 100

pygame.init()
pygame.display.set_caption("Waves Of War")
disp = pygame.display.set_mode((w,h))
image = pygame.image.load(r"C:\Users\Aaroh\Downloads\city.webp")
image = pygame.transform.scale(image,(w,h))
player = pygame.Surface((x,y))
player.fill("red")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    x += 0.25
    y += 0.25
    disp.fill("white")
    disp.blit(image,(0,0))
    disp.blit(player,(x,y))
    pygame.display.update()

pygame.quit()