import pygame

w = 600
h = 337
x = 25
y = 25

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
    
    keys=pygame.key.get_pressed()

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        x -=0.2
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += 0.2
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= 0.2
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += 0.2

    disp.fill("white")
    disp.blit(image,(0,0))
    disp.blit(player,(x,y))
    pygame.display.update()

pygame.quit()