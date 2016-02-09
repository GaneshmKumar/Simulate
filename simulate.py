import pygame,sys
from pygame.locals import *
import time
import random
pygame.init()
letter='\0'
element=[];p=[]
score=0;p=0;temp=0;i=0;n=0;x=0;l=140;r=100;t=140;b=100
#input
def pattern():
    i=0;ploop=0
    ip='\0'
    ploop=random.randint(5,8)
    #print ploop
    while i!=ploop:
        i=i+1
        n=random.randint(1,4)
        if n==1:
            letter='r'
            ip=ip+letter
            pygame.draw.rect(disp,WHITE,(l,t,r,b))
            pygame.display.update()
            time.sleep(0.3)
            pygame.draw.rect(disp,RED,(l,t,r,b))
            pygame.display.update()
            time.sleep(0.3)
        elif n==2:
            letter='g'
            ip=ip+letter
            pygame.draw.rect(disp,WHITE,(l+110,t,r,b))
            pygame.display.update()
            time.sleep(0.3)
            pygame.draw.rect(disp,GREEN,(l+110,t,r,b))
            pygame.display.update()
            time.sleep(0.3)
        elif n==3:
            letter='b'
            ip=ip+letter
            pygame.draw.rect(disp,WHITE,(l,t+110,r,b))
            pygame.display.update()
            time.sleep(0.3)
            pygame.draw.rect(disp,BLUE,(l,t+110,r,b))
            pygame.display.update()
            time.sleep(0.3)
        elif n==4:
            letter='y'
            ip=ip+letter
            pygame.draw.rect(disp,WHITE,(l+110,t+110,r,b))
            pygame.display.update()
            time.sleep(0.3)
            pygame.draw.rect(disp,YELLOW,(l+110,t+110,r,b))
            pygame.display.update()
            time.sleep(0.3)
        #print ip
        element=[ploop,ip]
    return element
#output
def click():
    op='\0'
    var=0
    while var!=p[0]:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN:
                var=var+1
                if event.key == K_r:
                    letter='r'
                    op=op+letter
                    pygame.draw.rect(disp,WHITE,(l,t,r,b))
                    pygame.display.update()
                    time.sleep(0.1)
                    pygame.draw.rect(disp,RED,(l,t,r,b))
                elif event.key == K_g:
                    letter='g'
                    op=op+letter
                    pygame.draw.rect(disp,WHITE,(l+110,t,r,b))
                    pygame.display.update()
                    time.sleep(0.1)
                    pygame.draw.rect(disp,GREEN,(l+110,t,r,b))
                elif event.key == K_b:
                    letter='b'
                    op=op+letter
                    pygame.draw.rect(disp,WHITE,(l,t+110,r,b))
                    pygame.display.update()
                    time.sleep(0.1)
                    pygame.draw.rect(disp,BLUE,(l,t+110,r,b))
                elif event.key == K_y:
                    letter='y'
                    op=op+letter
                    pygame.draw.rect(disp,WHITE,(l+110,t+110,r,b))
                    pygame.display.update()
                    time.sleep(0.1)
                    pygame.draw.rect(disp,YELLOW,(l+110,t+110,r,b))
                else:
                    var=var-1
                pygame.display.update()
                #print op
    return op
soundObj=pygame.mixer.music.load('l.mp3')
pygame.mixer.music.play(-1, 0.0)
disp=pygame.display.set_mode((500,500),0,32)
pygame.display.set_caption('SIMULATE')
RED=(155,0,0)
GREEN=(0,155,0)
BLUE=(0,0,155)
YELLOW=(155,155,0)
BLACK=(0,0,0)
WHITE=(255,255,255,1)
bg=BLACK
disp.fill(bg)
pygame.draw.rect(disp,RED,(l,t,r,b))
pygame.draw.rect(disp,GREEN,(l+110,t,r,b))
pygame.draw.rect(disp,BLUE,(l,t+110,r,b))
pygame.draw.rect(disp,YELLOW,(l+110,t+110,r,b))
fontObj=pygame.font.Font('freesansbold.ttf',25)
textSurfaceObj=fontObj.render('SIMULATE',True,WHITE,BLACK)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (240, 50)
disp.blit(textSurfaceObj,textRectObj)
while i<5:
    i=i+1
    p=pattern()
    c=click()
    print c
    print p[1]
    if c == p[1]:
        print 'win'
        score=score+10
        fontObj=pygame.font.Font('freesansbold.ttf',25)
        textSurfaceObj=fontObj.render('YOU WIN',True,WHITE,BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (250, 450)
        disp.blit(textSurfaceObj,textRectObj)
        pygame.display.update()
        time.sleep(2)
        textSurfaceObj=fontObj.render('YOU WIN',True,BLACK,BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (250, 450)
        disp.blit(textSurfaceObj,textRectObj)
    else:
        print 'lost'
        fontObj=pygame.font.Font('freesansbold.ttf',25)
        textSurfaceObj=fontObj.render('YOU LOSE',True,WHITE,BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (250, 450)
        disp.blit(textSurfaceObj,textRectObj)
        pygame.display.update()
        time.sleep(2)
        textSurfaceObj=fontObj.render('YOU LOSE',True,BLACK,BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (250, 450)
        disp.blit(textSurfaceObj,textRectObj)
    pygame.display.update()
    time.sleep(2)
pygame.mixer.music.stop()
