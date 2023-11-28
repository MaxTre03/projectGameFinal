import pygame

class pet:
    def __init__(self,x,y,berry1,drop =5):
        self.berry = pygame.transform.scale(berry1,(200,200))
        self.x=x
        self.y=y
        self.drop = drop
        self.frog = pygame.Rect(self.x,self.y,200,200)

    def draw(self,disp):
        disp.blit(self.berry,self.frog)
        #pygame.draw.rect(disp,(255,255,255),self.frog)

    def update(self):
        self.frog.y += self.drop

    def out(self,height,width):
        if self.fbox.y > height or self.fbox.y < 0:
            self.reload()
        if self.fbox.x > width or self.fbox.x < 0:
            self.reload()

