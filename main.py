"""
    INITIALISED BY: Callum S
    DATE INITIALISED: {{DD/MM/YYYY}} 20/06/2020
    DATE FINISHED: {{DD/MM/YYYY}} N/A
    EDITED BY: Callum S
    LAST EDITED BY & DATE {{DD/MM/YYYY}}: Callum S, 2/06/2020|14:54

"""

import pygame
import os

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

run = True

# WINDOW SETUP

WIDTH = 500
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("1v1 Local Player")
healthFont = pygame.font.SysFont("Comic Sans MS", 25)

# LOAD IMAGES

backGround = pygame.image.load(os.path.join("Assets", "bg.png"))

# END OF WINDOW SETUP

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


def redrawGameWindow():
    win.blit(backGround, (0, 0))
    plrOne.draw(win)
    plrTwo.draw(win)
    drawText()
    pygame.display.update()

def drawText():
    win.blit(healthFont.render("Player One", True, (0, 0, 0)), (10, 5)) # font.render("...") = text | False = Sharpness (True = sharp, False = not sharp) | (0, 0, 0) = Color | (0, 0 )= position
    test = win.blit(healthFont.render(f"Health: {str(plrOne.health)}", True, (0, 0, 0)), (10, 41))
    test = win.blit(healthFont.render("Player Two", True, (0, 0, 0)), (365, 5))
    test = win.blit(healthFont.render(f"Health: {str(plrTwo.health)}", True, (0, 0, 0)), (365, 41))




plrOne = player(36, 219, 64, 64, (0, 255, 0))
plrTwo = player(370, 219, 64, 64, (255, 0, 0))

plrOne.health = 8
plrTwo.health = 4

plr1Bullets = []
plr2Bullets = []


while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    for bullet in plr1Bullets:
        
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and plrOne.x > plrOne.velocity:
        plrOne.x -= plrOne.velocity
        plrOne.left = True
        plrOne.right = False
    elif keys[pygame.K_d] and plrOne.x < WIDTH - plrOne.width - plrOne.velocity:
        plrOne.x += plrOne.velocity
        plrOne.left = False
        plrOne.right = True

    if not(plrOne.isJump):
        if keys[pygame.K_w]:
            plrOne.isJump = True
            plrOne.right = False
            plrOne.left = False
            plrOne.walkCount = 0
    else:
        if plrOne.jumpCount >= -8:
            neg = 1
            if plrOne.jumpCount < 0:
                neg = -1
            plrOne.y -= int((plrOne.jumpCount ** 2) / 1 * neg)
            plrOne.jumpCount -= 1
        else:
            plrOne.isJump = False
            plrOne.jumpCount = 8

    if keys[pygame.K_LEFT] and plrTwo.x > plrTwo.velocity:
        plrTwo.x -= plrTwo.velocity
        plrTwo.left = True
        plrTwo.right = False
    elif keys[pygame.K_RIGHT] and plrTwo.x < WIDTH - plrTwo.width - plrTwo.velocity:
        plrTwo.x += plrTwo.velocity
        plrTwo.left = False
        plrTwo.right = True

    if not(plrTwo.isJump):
        if keys[pygame.K_UP]:
            plrTwo.isJump = True
            plrTwo.right = False
            plrTwo.left = False
            plrTwo.walkCount = 0
    else:
        if plrTwo.jumpCount >= -8:
            neg = 1
            if plrTwo.jumpCount < 0:
                neg = -1
            plrTwo.y -= int((plrTwo.jumpCount ** 2) / 1 * neg)
            plrTwo.jumpCount -= 1
        else:
            plrTwo.isJump = False
            plrTwo.jumpCount = 8

    if keys[pygame.K_s] and len(plr1Bullets) < 5:
        plr1Bullets.append()

    redrawGameWindow()



    

pygame.quit()