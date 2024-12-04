import pygame
pygame.init()
window = pygame.display.set_mode((1200,675))
pygame.display.set_caption("immi's game")
#walkright = [pygame.image.load('zom1.png'),pygame.image.load('zom2.png'),pygame.image.load('zom3.png'),pygame.image.load('zom4.png'),pygame.image.load('zom5.png'),pygame.image.load('zom6.png'),pygame.image.load('zom7.png'),pygame.image.load('zom8.png'),pygame.image.load('zom9.png')]
#walkleft = [pygame.image.load('zom1.png'),pygame.image.load('zom1.png'),pygame.image.load('zom1.png'),pygame.image.load('zom1.png'),pygame.image.load('zom1.png'),pygame.image.load('zom1.png'),pygame.image.load('zom1.png'),pygame.image.load('zom1.png'),pygame.image.load('zom1.png')]
walkright = [pygame.image.load(f'zom{i}.png') for i in range(1, 10)]


walkleft = [pygame.transform.flip(img, True, False) for img in walkright]
bg = pygame.image.load('bg2.png')

char = [pygame.image.load('idle.png')]
x = 15
y = 375
width = 300
height = 300
vel =15
clock = pygame.time.Clock()
jump = False
jumpcount = 10

left = False
right = False
run = True
walkcount = 0

def redrawwindow():
    global walkcount

    window.blit(bg,(0,0))
    if walkcount +1>= 27:
        walkcount = 0
    if left:
        window.blit(walkleft[walkcount//3],(x,y))
        walkcount+= 1
    elif right:
        window.blit(walkright[walkcount//3],(x,y))
        walkcount+= 1
    else:
        window.blit(char[0], (x,y))
        walkcount = 0

    pygame.display.update()


while run:
    clock.tick(27)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key= pygame.key.get_pressed()

    if key[pygame.K_LEFT] and x>-70:
        x = x- vel
        left = True
        right = False

    elif key[pygame.K_RIGHT] and x< 1200 -width+80:
        x = x+ vel
        left = False
        right = True
    else:
        left = False
        right = False
        walkcount = 0

   
    if not(jump):
        if key[pygame.K_SPACE]:
            jump = True
            left = False
            right = False
            walkcount =0
    else :
        if jumpcount >= -10:
            neg = 1
            if jumpcount < 0 :
                neg = -1
            y -= (jumpcount ** 2)*0.3*neg
            jumpcount -= 1
        else:
            jump = False
            jumpcount = 10
    redrawwindow()
  
pygame.quit()