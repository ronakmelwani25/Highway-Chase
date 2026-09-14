import pygame
import random
pygame.init()

WIDTH = 1600
HEIGHT = 900
screen= pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("white")

bg=pygame.image.load("Python/Pygame/Lesson 4 - Space Shooter/Images/ChatGPT Image Sep 13, 2026, 05_30_29 PM.png")

Mclaren=pygame.image.load("Python/Pygame/Lesson 4 - Space Shooter/Images/Overhead_McLarenv1-removebg-preview.png")
mscale=pygame.transform.scale(Mclaren,(270,160))
mrotate=pygame.transform.rotate(mscale,270)

Tesla=pygame.image.load("Python/Pygame/Lesson 4 - Space Shooter/Images/overheadviewteslav1-removebg-preview.png")
tscale=pygame.transform.scale(Tesla,(330,250))
trotate=pygame.transform.rotate(tscale,270)

Koenigsegg=pygame.image.load("Python/Pygame/Lesson 4 - Space Shooter/Images/overheadkoenigsegg-removebg-preview.png")
kscale=pygame.transform.scale(Koenigsegg,(300,200))
krotate=pygame.transform.rotate(kscale,90)

Corvette=pygame.image.load("Python/Pygame/Lesson 4 - Space Shooter/Images/overheadcorvettev1-removebg-preview.png")
cscale=pygame.transform.scale(Corvette,(160,260))
crotate=pygame.transform.rotate(cscale,360)

mrect=pygame.Rect(270,160,270,160)
trect=pygame.Rect(100,100,330,250)
crect=pygame.Rect(1300,-100,260,160)
krect=pygame.Rect(1000,1100,300,200)

def mover():
    if keys_pressed[pygame.K_UP]:
        mrect.y=mrect.y-2
    if keys_pressed[pygame.K_DOWN]:
        mrect.y=mrect.y+2
    if keys_pressed[pygame.K_LEFT]:
        mrect.x=mrect.x-2
    if keys_pressed[pygame.K_RIGHT]:
        mrect.x=mrect.x+2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    screen.blit(bg, (0, 0))
    screen.blit(mrotate, (mrect))
    screen.blit(trotate, (trect))
    screen.blit(crotate, (crect))
    screen.blit(krotate, (krect))
    keys_pressed = pygame.key.get_pressed()
    p=random.randint(1,7)
    pp=random.randint(1,5)
    mover()

    krect.y=krect.y-p
    if krect.y<=-300:
        krect.y=1000
        krect.x=random.randint(800,1300)

    crect.y=crect.y+pp
    print(crect.y)
    if crect.y>=1000:
        crect.y=-100
        crect.x=random.randint(800,1300)

    pygame.display.update()