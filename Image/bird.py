import pygame
from Utils import function as fn
from Utils import constant as const
from Utils import variables as var

SCREEN = var.SCREEN
WINDOWWIDTH = const.WINDOWWIDTH
WINDOWHEIGHT = const.WINDOWHEIGHT
# Set constants variable for Bird
BIRDWIDTH = const.BIRDWIDTH
BIRDHEIGHT = const.BIRDHEIGHT
G = const.G
SPEEDFLY = const.SPEEDFLY

YELLOWBIRD_MID_URL = const.YELLOWBIRD_MID_URL
YELLOWBIRD_UP_URL = const.YELLOWBIRD_UP_URL
YELLOWBIRD_DOWN_URL = const.YELLOWBIRD_DOWN_URL

BROWNBIRD_MID_URL = const.BROWNBIRD_MID_URL
BROWNBIRD_UP_URL = const.BROWNBIRD_UP_URL
BROWNBIRD_DOWN_URL = const.BROWNBIRD_DOWN_URL

BLUEBIRD_MID_URL = const.BLUEBIRD_MID_URL
BLUEBIRD_UP_URL = const.BLUEBIRD_UP_URL
BLUEBIRD_DOWN_URL = const.BLUEBIRD_DOWN_URL

BIRD_INDEX = const.BIRD_INDEX

# Load yellow bird
BIRD_MID = fn.load_scale_image(YELLOWBIRD_MID_URL, BIRDWIDTH, BIRDHEIGHT)
BIRD_DOWN = fn.load_scale_image(YELLOWBIRD_DOWN_URL, BIRDWIDTH, BIRDHEIGHT)
BIRD_UP = fn.load_scale_image(YELLOWBIRD_UP_URL, BIRDWIDTH, BIRDHEIGHT)
BIRD_LIST = [BIRD_DOWN, BIRD_MID, BIRD_UP]
BIRD = BIRD_LIST[BIRD_INDEX]

#Load brown bird
BROWNBIRD_MID = fn.load_scale_image(BROWNBIRD_MID_URL, BIRDWIDTH, BIRDHEIGHT)
BROWNBIRD_DOWN= fn.load_scale_image(BROWNBIRD_DOWN_URL, BIRDWIDTH, BIRDHEIGHT)
BROWNBIRD_UP = fn.load_scale_image(BROWNBIRD_UP_URL, BIRDWIDTH, BIRDHEIGHT)
BROWNBIRD_LIST = [BROWNBIRD_DOWN, BROWNBIRD_MID, BROWNBIRD_UP]
BROWNBIRD = BROWNBIRD_LIST[BIRD_INDEX]

#Load blue bird
BLUEBIRD_MID = fn.load_scale_image(BLUEBIRD_MID_URL, BIRDWIDTH, BIRDHEIGHT)
BLUEBIRD_DOWN = fn.load_scale_image(BLUEBIRD_DOWN_URL, BIRDWIDTH, BIRDHEIGHT)
BLUEBIRD_UP = fn.load_scale_image(BLUEBIRD_UP_URL, BIRDWIDTH, BIRDHEIGHT)
BLUEBIRD_LIST = [BLUEBIRD_DOWN, BLUEBIRD_MID, BLUEBIRD_UP]
BLUEBIRD = BLUEBIRD_LIST[BIRD_INDEX]

BIRD_FLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRD_FLAP, 50)

class Bird():
    def __init__(self):
        self._width = BIRDWIDTH
        self._height = BIRDHEIGHT
        self._x = (WINDOWWIDTH - self._width)/2 - 30
        self._y = (WINDOWHEIGHT - self._height)/2
        self._speed = 0
        #self.surface = BIRD
        self._Angle = 0
    def getWidth(self):
        return self._width
    def getHeight(self):
        return self._height
    def getX(self):
        return self._x
    def setY(self, y):
        self._y = y
    def getY(self):
        return self._y
    def setSpeed(self, speed):
        self._speed = speed
    def draw(self):
        SCREEN.blit(fn.rotate_bird(BIRD, self._Angle), (int(self._x), int(self._y)))

    def update(self, mouseClick):
        self._y += self._speed + 0.5*G
        self._speed += G
        self._Angle -= G*self._speed
        if mouseClick == True:
            self._Angle += 180
            self.setSpeed(SPEEDFLY)
        if self._Angle > 20:
            self._Angle = 20
        if self._Angle < -90:
            self._Angle = -90


class BrownBird(Bird):
    def __init__(self):
        Bird.__init__(self)
    def draw(self):
        SCREEN.blit(fn.rotate_bird(BROWNBIRD, self._Angle), (int(self._x), int(self._y)))


class BlueBird(Bird):
    def __init__(self):
        Bird.__init__(self)
    def draw(self):
        SCREEN.blit(fn.rotate_bird(BLUEBIRD, self._Angle), (int(self._x), int(self._y)))
