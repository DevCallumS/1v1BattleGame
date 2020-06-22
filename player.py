import pygame

class player(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.isJump = False
        self.jumpCount = 8
        self.left = False
        self.right = False
        self.color = color
        self.health = 10


    def draw(self, win):
        if self.health <= 0:
            print("Lost")

        # if self.left:
            
        # else: 
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
