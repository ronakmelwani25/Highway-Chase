import pygame
import random
pygame.init()

WIDTH = 1600
HEIGHT = 900
screen= pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("white")
font=pygame.font.SysFont("impact",100)

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

Bugatti=pygame.image.load("Python/Pygame/Lesson 4 - Space Shooter/Images/Over-removebg-preview.png")
bscale=pygame.transform.scale(Bugatti,(280,190))
brotate=pygame.transform.rotate(bscale,90)

F1=pygame.image.load("Python\Pygame\Lesson 4 - Space Shooter\Images\Lotus_F1-removebg-preview (1).png")
fscale=pygame.transform.scale(F1,(300,120))
frotate=pygame.transform.rotate(fscale,90)

#mrect=pygame.Rect(900,700,270,160)
mrect=pygame.Rect(1000,700,10,10)
trect=pygame.Rect(100,100,330,250)
crect=pygame.Rect(1300,-100,260,160)
krect=pygame.Rect(1500,1100,300,200)
brect=pygame.Rect(300,300,190,280)
frect=pygame.Rect(750,500,300,120)

p=1
pp=2
ppp=3
pppp=4
ppppp=5
score=0
time=0

rects=[trect,crect,krect,brect,frect]

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
    screen.blit(brotate, (brect))
    screen.blit(frotate, (frect))
    keys_pressed = pygame.key.get_pressed()
    mover()
    pygame.draw.rect(screen,"red",brect,2)

    text=font.render("Score= " + str(score),True, "Gold")
    screen.blit(text, (10,10))

    time+=1
    if time>10:
        time=0
        score+=1

    krect.y=krect.y-ppp
    if krect.y<=-300:
        krect.y=1000
        krect.x=random.randint(800,1300)
        p=random.randint(1,7)

    crect.y=crect.y+pp
    if crect.y>=1000:
        crect.y=-100
        crect.x=random.randint(800,1300)
        pp=random.randint(1,5)
    
    brect.y=brect.y+pppp
    if brect.y>=1000:
        brect.y=-100
        brect.x=random.randint(150,700)
        ppp=random.randint(2,6)
    
    trect.y=trect.y+p
    if trect.y>=1000:
        trect.y=-100
        trect.x=random.randint(150,700)
        pppp=random.randint(2,4)
    
    frect.y=frect.y+ppppp
    if frect.y>=1000:
        frect.y=-1000

#    for i in rects:
    if mrect.colliderect(brect):
            screen.fill("green")
            pygame.display.update()
            pygame.time.delay(3000)
            break

    pygame.display.update()