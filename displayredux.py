import pygame
from sys import exit
from math import ceil
from time import time

# Initialize pygame modules
pygame.init()

# Display settings
windowSize = (1000, 500)
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption('Python Sorting Algorithm Visualizer')

# Font
baseFont = pygame.font.SysFont('Seoge UI', 25)

# Used Colors
navy = (46, 58, 89)
green = (125, 240, 125)
white = (250, 250, 250)
red = (255, 50, 50)
black = (0, 0, 0)
blue = (50, 50, 255)

# THE CODE BELOW IS A MODULE FOR TAKING USER INPUT WITH PYGAME #
class InputBox:
    def __init__(self, name, color, rect):
        self.isActive = False
        self.name = name
        self.color = color
        self.rect = pygame.Rect(rect)

    def draw(self):
        label = baseFont.render(self.name, True, self.color)
        screen.blit(label, (self.rect.x + (self.rect.w - label.get_width()) / 2, self.rect.y - 25))
        pygame.draw.rect(screen, self.color, self.rect, 3)

    def update(self):
        mousePos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() != (0, 0, 0):
            if self.rect.collidepoint(mousePos):
                self.isActive = True
            else:
                self.isActive = False
                
class TextBox(InputBox):
    def __init__(self, name, color, rect):
        super().__init__(name, color, rect)
        self.text = ''

    def draw(self):
        super().draw()
        surface = baseFont.render(self.text, True, self.color)
        screen.blit(surface, (self.rect.x + 15, self.rect.y + 10))
        self.rect.w = max(surface.get_width() + 25, 50)

    def update(self, wEvent):
        super().update()
        if self.isActive and wEvent.type == pygame.KEYDOWN:
            if wEvent.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if wEvent.unicode.isdigit(): 
                    self.text += wEvent.unicode
                    
class SliderBox(InputBox):
    def __init__(self, name, color, rect):
        super().__init__(name, color, rect)
        self.value = self.rect.x+7

    def draw(self):
        super().draw()
        pygame.draw.line(screen, self.color, (self.rect.x+6, self.rect.y+25), (self.rect.x+self.rect.w-6, self.rect.y+25), 2)
        pygame.draw.line(screen, self.color, (self.value, self.rect.y+5), (self.value, self.rect.y+45), 12)

    def update(self):
        super().update()
        if self.isActive and pygame.mouse.get_pressed() != (0, 0, 0):
            x = pygame.mouse.get_pos()[0]
            if x <= self.rect.x+6:
                self.value = self.rect.x+6
            elif x >= self.rect.w+self.rect.x-6:
                self.value = self.rect.w+self.rect.x-6
            else:
                self.value = x
