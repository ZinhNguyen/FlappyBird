from Utils import constant as const
from Utils import variables as var
from Utils import function as fn

SCREEN = var.SCREEN
WINDOWWIDTH = const.WINDOWWIDTH
WINDOWHEIGHT = const.WINDOWHEIGHT
BG_X_POS = const.BG_X_POS
BG_Y_POS = const.BG_Y_POS
BG_URL = const.BACKGROUND_URL

# Load Background
BACKGROUND = fn.load_scale_image(BG_URL, WINDOWWIDTH, WINDOWHEIGHT)

class Background():
    def __init__(self):
        self._x = BG_X_POS
        self._y = BG_Y_POS
        self._width = WINDOWWIDTH
        self._height = WINDOWHEIGHT
        self._surface = BACKGROUND
    def draw(self):
        SCREEN.blit(self._surface, (self._x, self._y))

