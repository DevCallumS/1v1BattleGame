from main import plrOne
from main import plrTwo

def isInHitBoxY1(bullet):
     return bullet.y - bullet.radius < plrTwo.hitbox[1] + plrTwo.hitbox[3] and bullet.y + bullet.radius > plrTwo.hitbox[1]


def isInHitBoxX1(bullet):
    return bullet.x + bullet.radius > plrTwo.hitbox[0] and bullet.x - bullet.radius < plrTwo.hitbox[0] + plrTwo.hitbox[2]


def isInHitBoxY2(bullet):
     return bullet.y - bullet.radius < plrOne.hitbox[1] + plrOne.hitbox[3] and bullet.y + bullet.radius > plrOne.hitbox[1]


def isInHitBoxX2(bullet):
    return bullet.x + bullet.radius > plrOne.hitbox[0] and bullet.x - bullet.radius < plrOne.hitbox[0] + plrOne.hitbox[2]
