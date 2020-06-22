"""
    INITIALISED BY: Callum S
    DATE INITIALISED: {{DD/MM/YYYY}} 20/06/2020
    DATE FINISHED: {{DD/MM/YYYY}} N/A
    EDITED BY: Callum S
    LAST EDITED BY & DATE {{DD/MM/YYYY}}: Callum S, 2/06/2020|14:54

"""

import pygame
import os
from player import player
from projectile import projectile


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

plrOne = player(36, 219, 64, 64, (0, 255, 0))
plrTwo = player(370, 219, 64, 64, (255, 0, 0))


plrOne.health = 8
plrTwo.health = 4


plr1Bullets = []
plr2Bullets = []

shootCoolDown1 = 0
shootCoolDown2 = 0

def redrawGameWindow():
    win.blit(backGround, (0, 0))
    plrOne.draw(win)
    plrTwo.draw(win)
    drawText()

    for bullet in plr1Bullets:
        bullet.draw(win)

    for bullet in plr2Bullets:
        bullet.draw(win)

    pygame.display.update()


def drawText():
    win.blit(healthFont.render("Player One", True, (0, 0, 0)), (10, 5)) # font.render("...") = text | False = Sharpness (True = sharp, False = not sharp) | (0, 0, 0) = Color | (0, 0 )= position
    test = win.blit(healthFont.render(f"Health: {str(plrOne.health)}", True, (0, 0, 0)), (10, 41))
    test = win.blit(healthFont.render("Player Two", True, (0, 0, 0)), (365, 5))
    test = win.blit(healthFont.render(f"Health: {str(plrTwo.health)}", True, (0, 0, 0)), (365, 41))

def isInHitBoxY1(bullet):
     return bullet.y - bullet.radius < plrTwo.hitbox[1] + plrTwo.hitbox[3] and bullet.y + bullet.radius > plrTwo.hitbox[1]


def isInHitBoxX1(bullet):
    return bullet.x + bullet.radius > plrTwo.hitbox[0] and bullet.x - bullet.radius < plrTwo.hitbox[0] + plrTwo.hitbox[2]


def isInHitBoxY2(bullet):
     return bullet.y - bullet.radius < plrOne.hitbox[1] + plrOne.hitbox[3] and bullet.y + bullet.radius > plrOne.hitbox[1]


def isInHitBoxX2(bullet):
    return bullet.x + bullet.radius > plrOne.hitbox[0] and bullet.x - bullet.radius < plrOne.hitbox[0] + plrOne.hitbox[2]


while run:
    clock.tick(27)

    if shootCoolDown1 > 0:
        shootCoolDown1 += 1
    if shootCoolDown1 > 30:
        shootCoolDown1 = 0

    if shootCoolDown2 > 0:
        shootCoolDown2 += 1
    if shootCoolDown2 > 30:
        shootCoolDown2 = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break


    for bullet in plr1Bullets:
        if isInHitBoxX1(bullet) and isInHitBoxY1(bullet):
            plrTwo.hit()
            plr1Bullets.pop(plr1Bullets.index(bullet))
        
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            plr1Bullets.pop(plr1Bullets.index(bullet))


    for bullet in plr2Bullets:
        if isInHitBoxX2(bullet) and isInHitBoxY2(bullet):
            plrOne.hit()
            plr2Bullets.pop(plr2Bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            plr2Bullets.pop(plr2Bullets.index(bullet))
    

    keys = pygame.key.get_pressed()


    # Player 1 Movement


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


    # Player 2 Movement


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


    # Player 1 Shooting


    if keys[pygame.K_s] and shootCoolDown1 == 0:
        if plrOne.left:
            facing = -1
        else:
            facing = 1

        if len(plr1Bullets) < 5:
            plr1Bullets.append(projectile(round(plrOne.x + plrOne.width //2), round(plrOne.y + plrOne.height //2), 6, plrOne.color, facing))

        shootCoolDown1 = 1



    # Player 2 Shooting


    if keys[pygame.K_DOWN] and shootCoolDown2 == 0:
        if plrTwo.left:
            facing = -1
        else:
            facing = 1

        if len(plr2Bullets) < 5:
            plr2Bullets.append(projectile(round(plrTwo.x + plrTwo.width //2), round(plrTwo.y + plrTwo.height //2), 6, plrTwo.color, facing))

        shootCoolDown2 = 1


    redrawGameWindow()

pygame.quit()