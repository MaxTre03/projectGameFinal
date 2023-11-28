import pygame

class item:
    #constuctor
    # load the image
    # create a reect object for the strawberry to detect collisions
    def __init__(self,x,y,item,size):
        self.berry = pygame.transform.scale(item,(size,size))
        self.x=x
        self.y=y
        self.fbox = pygame.Rect(self.x,self.y,size,size)

    def draw(self,disp):
        disp.blit(self.berry,self.fbox)
    
    def reload(self):
        self.fbox.x=self.x
        self.fbox.y=self.y

    def out(self,height,width):
        if self.fbox.y > height or self.fbox.y < 0:
            self.reload()
        if self.fbox.x > width or self.fbox.x < 0:
            self.reload()
