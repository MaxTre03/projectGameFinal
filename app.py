import pygame
from pet import *
from item import *
from statbox import *
from pygame.locals import *
from pygame import mixer

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

pygame.init()
#make display and some pictures 
height = 600
width = 800
disp = pygame.display.set_mode((width,height))
berry1 = pygame.image.load("images/download.png").convert_alpha()
fruit1 = pygame.image.load("images/food.png").convert_alpha()
bone = pygame.image.load("images/bone.png").convert_alpha()
image = pygame.image.load("images/background.gif")
background = pygame.transform.scale(image,(width,height))
bed = pygame.image.load("images/bed.png")
swole = pygame.image.load("images/weight.png")
bok = pygame.image.load("images/book.png")
#clock object 
gameClock = pygame.time.Clock()

#adding the music 
eating_fx = pygame.mixer.Sound('sounds/eating.wav.wav')
eating_fx.set_volume(0.5)
book_fx = pygame.mixer.Sound('sounds/book.mp3.mp3')
book_fx.set_volume(0.5)
weight_fx = pygame.mixer.Sound('sounds/weights.mp3.mp3')
weight_fx.set_volume(0.5)
bed_fx = pygame.mixer.Sound('sounds/blanket.mp3.wav')
bed_fx.set_volume(1.5)
throw_fx = pygame.mixer.Sound('sounds/whoosh.mp3')
throw_fx.set_volume(1.5)
# fill the background with (200,200,200)
disp.fill((78,165,242))

#event handler object 
#make objeccts of classes
pepe = pet(290,175,berry1)
apple = item(50, 480,fruit1,100 )
sleepy = item(365,480,bed,100)
book = item(200, 480,bok,100)
happy = item(500,460,bone,150)
work = item(660,480,swole,100)
stats = statbox(10, 10, 225, 400)
legend = statbox(565, 10, 225, 250)
#berry = pygame.transform.scale(berry1,(200,200))

# create a main for lopp 
active_box = None
objs = []
objs.append(apple.fbox)
objs.append(sleepy.fbox)
objs.append(book.fbox)
objs.append(happy.fbox)
objs.append(work.fbox)

while True:
    #put stuff on the screen and fix some things
    disp.blit(background,(0,0))
    pepe.draw(disp)
    apple.draw(disp)
    sleepy.draw(disp)
    book.draw(disp)
    happy.draw(disp)
    work.draw(disp)
    #check out of bounds 
    apple.out(height,width)
    sleepy.out(height,width)
    book.out(height,width)
    happy.out(height,width)
    work.out(height,width)
    #statbox stuff, also displaying legend
    stats.draw(disp)
    legend.drawL(disp)
    stats.update(disp)
    #now we try to see if we can get stuff to collide

    if apple.fbox.colliderect(pepe.frog):
        stats.hp+=15
        stats.ene-=6
        if(stats.hp > 100):
            stats.hp = 100
        eating_fx.play()
        apple.reload()
    if sleepy.fbox.colliderect(pepe.frog):
        stats.ene+=15
        stats.hp-=5
        stats.edu-=5
        stats.gns-=5
        stats.hap-=5
        if(stats.ene > 100):
            stats.ene = 100
        bed_fx.play()
        sleepy.reload()
    if book.fbox.colliderect(pepe.frog):
        stats.edu+=15
        stats.gns-=6
        if(stats.edu > 100):
            stats.edu = 100
        book_fx.play()
        book.reload()
    if happy.fbox.colliderect(pepe.frog):
        stats.hap+=20
        stats.ene-=6
        if(stats.hap > 100):
            stats.hap = 100
        throw_fx.play()
        happy.reload()
    if work.fbox.colliderect(pepe.frog):
        stats.gns+=20
        stats.ene-=6
        if(stats.gns > 100):
            stats.gns = 100
        weight_fx.play()
        work.reload()
    
    # events are handled here 
    for events in pygame.event.get():
            if events.type == pygame.QUIT: 
                pygame.quit()
                exit()
            elif events.type == pygame.MOUSEBUTTONDOWN:
                if events.button ==1:
                    for num ,frogs in enumerate(objs):
                        if frogs.collidepoint(events.pos):
                            active_box = num
                        
            if events.type == pygame.MOUSEMOTION:
                if active_box != None:
                    objs[active_box].move_ip(events.rel)
            if events.type == pygame.MOUSEBUTTONUP:
                if events.button ==1 :
                    active_box = None

    # decay rates here
    stats.hp-=.05
    stats.edu-=.02
    stats.ene-=.1
    stats.hap-=.08
    stats.gns-=.03
             
    pygame.display.update()

    gameClock.tick(30)