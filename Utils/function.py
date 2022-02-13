import pygame
from Utils import constant as const
from Sound import start as st

WINDOWHEIGHT = const.WINDOWHEIGHT
M_SCREEN_HEIGHT = const.M_SCREEN_HEIGHT
DEFAULT_BIRD_POS = const.DEFAULT_BIRD_POS

def load_scale_image(url_image, scale_width, scale_height):
    new_image = pygame.image.load(url_image)
    new_image = pygame.transform.scale(new_image, (scale_width, scale_height))
    return new_image

def rotate_bird(bird, angle):
    new_bird = pygame.transform.rotate(bird, angle)
    return new_bird

def flying(up, y, height):
    if up == True:
        y -= 0.5
    if up == False:
        y += 0.5
    if y == DEFAULT_BIRD_POS - height:
        up = False
    if y == DEFAULT_BIRD_POS + height:
        up = True
    return y, up

# colission between bird and columns
def rectCollision(rect1, rect2):
    if rect1[0] <= rect2[0]+rect2[2] and rect2[0] <= rect1[0]+rect1[2] and rect1[1] <= rect2[1]+rect2[3] and rect2[1] <= rect1[1]+rect1[3]:
        return True
    return False

def isGameOver(bird, columns):
    for i in range(3):
        rectBird = [bird.getX(), bird.getY(), bird.getWidth(), bird.getHeight()]
        rectColumn1 = [columns.ls[i][0], columns.ls[i][1] - columns.height, columns.width, columns.height]
        rectColumn2 = [columns.ls[i][0], columns.ls[i][1] + columns.blank, columns.width, columns.height]
        if rectCollision(rectBird, rectColumn1) == True or rectCollision(rectBird, rectColumn2) == True:
            st.hit_sound.play()
            return True
    #if bird.y + bird.height < 0 or bird.y + bird.height > WINDOWHEIGHT - 160:
    if bird.getY() + bird.getHeight() > WINDOWHEIGHT - M_SCREEN_HEIGHT:
        return True
    return False

# from Image import bird as b
#
# def bird_animation():
#     NEW_BIRD = b.BIRD_LIST[b.BIRD_INDEX]
#     return NEW_BIRD
