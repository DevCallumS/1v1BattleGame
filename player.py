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
        self.hitbox = (self.x, self.y, 64, 64)


    def draw(self, win):
        # if self.left:
            
        # else: 
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

        self.hitbox = (self.x, self.y, 64, 64)
        pygame.draw.rect(win, (0, 0, 0), self.hitbox, 2)

    
    def hit(self):
        self.health -= 1
        if self.health <= 0:
            print("Killed")
