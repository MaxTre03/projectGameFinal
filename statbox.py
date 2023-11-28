import pygame
pygame.init()
from pygame import mixer

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

pygame.init()

font = pygame.font.Font(None, 36)  

pygame.mixer.music.load("sounds/background.wav.mp3")
pygame.mixer.music.play(-1,0.0,5000)

dying_fx = pygame.mixer.Sound('sounds/cryingindaclub.mp3.mp3')
dying_fx.set_volume(0.5)


font = pygame.font.Font(None, 36)  

class statbox:
    # sets default attributes of all stats
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.hp = 50
        self.edu = 50
        self.ene = 50
        self.hap = 50
        self.gns = 50

    # draws box
    def draw(self, disp):
        pygame.draw.rect(disp, (60, 100, 100), self.rect)
        pygame.draw.rect(disp, (150, 110, 130), self.rect, 3)  

        text_surface = font.render("Stats", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.rect.centerx, self.rect.y + 15))
        disp.blit(text_surface, text_rect)

    def drawL(self, disp):
        pygame.draw.rect(disp, (60, 100, 100), self.rect)
        pygame.draw.rect(disp, (150, 110, 130), self.rect, 3)

        text_surface = font.render("Legend", True, (255, 255, 255))  
        text_rect = text_surface.get_rect(center=(self.rect.centerx, self.rect.y + 15))
        disp.blit(text_surface, text_rect) 

        colors = [(255, 0, 0), (0, 0, 255), (255, 255, 0), (0, 255, 0), (255, 165, 0)]
        stats = ["Health", "Intelligence", "Energy", "Happiness", "Gains"]

        y = 40
        for color, label in zip(colors, stats):
            legend_rect = pygame.Rect(self.rect.x+30, self.rect.y + y, (self.rect.width-60), 20)
            pygame.draw.rect(disp, color, legend_rect)

            sfont = pygame.font.Font(None, 25)  
            text_surface = sfont.render(label, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(legend_rect.centerx, legend_rect.centery))
            disp.blit(text_surface, text_rect)

            y+=40

    # displays only progress bars
    def update(self, disp):
        # making two arrays, one for stats and another for colors
        statvalues = [self.hp, self.edu, self.ene, self.hap, self.gns]
        colors = [(255, 0, 0), (0, 0, 255), (255, 255, 0), (0, 255, 0), (255, 165, 0)]
        # determining bar width
        bar_width = (self.rect.width - 50) / len(statvalues)
        y = 30
        x = 15  
        for value, color in zip(statvalues, colors):
            if value < 0:
                pygame.mixer.music.stop()
                dying_fx.play()
                disp.fill((0, 0, 0))
                ripFont = pygame.font.Font(None, 288)  
                rip = ripFont.render("R.I.P", True, (255, 0, 0))
                text_rect = rip.get_rect(center=(disp.get_width()/2, disp.get_height()/2))
                disp.blit(rip, text_rect) 
                break
                break
            elif value > 100:
                self.drawBar(disp, 100, color, y, x, bar_width)
                x += 40
            else:
                self.drawBar(disp, value, color, y, x, bar_width)
                x += 40

    def drawBar(self, disp, value, color, y_offset, x_offset, bar_width):
        bar_height = value * (self.rect.height - 33) / 100
        bar_rect = pygame.Rect(self.rect.x + x_offset, self.rect.y + y_offset, bar_width, bar_height)
        pygame.draw.rect(disp, color, bar_rect)





            