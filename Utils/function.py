import pygame
from Utils import constant as const
from Sound import start as st

def load_scale_image(url_image, scale_width, scale_height):
    """
    This function will load image then scale with new width and height

    Parameters:
        url_image (url): path to image
        scale_width (int): the width of image after scale
        scale_height (int): the height of image after scale

    Returns:
        Return Surface
    """
    new_image = pygame.image.load(url_image)
    new_image = pygame.transform.scale(new_image, (scale_width, scale_height))
    return new_image

def rotate_bird(bird, angle):
    """
    This function will rotate object with new angle

    Parameters:
        bird (object): path to image
        angle (int): the Angle will be rotated

    Returns:
        Return object with new Angle
    """
    new_bird = pygame.transform.rotate(bird, angle)
    return new_bird

def flying(up, y, height):
    """
    This function will make object with moving in range

    Parameters:
        up (bool) : state for object
        y (float): y position of object
        height (int): moving range for object

    Returns:
        Return new y pos and new up state
    """
    if up == True:
        y -= 0.5
    if up == False:
        y += 0.5
    if y == const.DEFAULT_BIRD_POS - height:
        up = False
    if y == const.DEFAULT_BIRD_POS + height:
        up = True
    return y, up

# colission between bird and columns
def rectCollision(rect1, rect2):
    """
    This function will checking the collision between 2 rectangle

    Parameters:
        rect1 (list) : list with 4 parameter(x, y, width, height)
        rect2 (list) : list with 4 parameter(x, y, width, height)

    Returns:
        Return True if have collision else is False
    """
    if rect1[0] <= rect2[0]+rect2[2] and rect2[0] <= rect1[0]+rect1[2] and rect1[1] <= rect2[1]+rect2[3] and rect2[1] <= rect1[1]+rect1[3]:
        return True
    return False

def isGameOver(bird, columns):
    """
    This function will checking the collision between bird with columns or floor

    Parameters:
        bird (object) : list with 4 parameter(x, y, width, height)
        columns (object) : list with 4 parameter(x, y, width, height)

    Returns:
        Return True if have collision else is False
    """
    for i in range(3):
        rectBird = [bird.getX(), bird.getY(), bird.getWidth(), bird.getHeight()]
        rectColumn1 = [columns.ls[i][0], columns.ls[i][1] - columns.getHeight(), columns.getWidth(), columns.getHeight()]
        rectColumn2 = [columns.ls[i][0], columns.ls[i][1] + columns.getBlank(), columns.getWidth(), columns.getHeight()]
        if rectCollision(rectBird, rectColumn1) == True or rectCollision(rectBird, rectColumn2) == True:
            st.hit_sound.play()
            return True
    #if bird.y + bird.height < 0 or bird.y + bird.height > WINDOWHEIGHT - 160:
    if bird.getY() + bird.getHeight() > const.WINDOWHEIGHT - const.M_SCREEN_HEIGHT:
        return True
    return False

def draws(background, columns, bird, scoreBoard, GameOverLogo, goGuide, scoreTitle, scoreContent, BestTitle, BestContent, MedalTitle):
    """
    This function will set draw function for all Parameter

    Parameters:
        background,columns... (object) : all object will be set

    Returns:
        Return draw function for parameters
    """
    background.draw()
    columns.draw()
    bird.draw()
    scoreBoard.draw()
    GameOverLogo.draw()
    goGuide.draw()
    scoreTitle.draw()
    scoreContent.draw()
    BestTitle.draw()
    BestContent.draw()
    MedalTitle.draw()

def drawMedal(score):
    """
    This function will compare score then set draw function for medal

    Parameters:
        score (int) : this score use for comparison

    Returns:
        Return draw function for suitable medal
    """
    from Image import medal as md
    noMedal = md.NoMedal()
    bronzeMedal = md.BronzeMedal()
    silverMedal = md.SilverMedal()
    goldMedal = md.GoldMedal()
    diamondMedal = md.DiamondMedal()
    if score < 5:
        return noMedal.draw()
    elif score < 10:
        bronzeMedal.draw()
    elif score< 15:
        silverMedal.draw()
    elif score < 20:
        goldMedal.draw()
    else:
        diamondMedal.draw()

