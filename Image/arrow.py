from Utils import constant as const
from Utils import variables as var
from Utils import function as fn

ARROW_X_POS = const.ARROW_X_POS
ARROW_Y_POS = const.ARROW_Y_POS

SCREEN = var.SCREEN
ARROW_URL = const.ARROW_URL
ARROW_WIDTH = const.ARROW_WIDTH
ARROW_HEIGHT = const.ARROW_HEIGHT

# Add Arrow for Background
ARROW = fn.load_scale_image(ARROW_URL, ARROW_WIDTH, ARROW_HEIGHT)

class Arrow():
    def __init__(self):
        self._x = ARROW_X_POS
        self._y = ARROW_Y_POS
        self._width = ARROW_WIDTH
        self._height = ARROW_HEIGHT
        self._surface = ARROW

    def draw(self):
        SCREEN.blit(self._surface, (self._x, self._y))