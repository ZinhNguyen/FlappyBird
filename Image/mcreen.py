from Utils import constant as const
from Utils import variables as var
from Utils import function as fn

SCREEN = var.SCREEN
WINDOWWIDTH = const.WINDOWWIDTH
M_SCREEN_WIDTH = const.M_SCREEN_WIDTH
M_SCREEN_HEIGHT= const.M_SCREEN_HEIGHT
M_SCREEN_X_POS = const.M_SCREEN_X_POS
M_SCREEN_Y_POS = const.M_SCREEN_Y_POS
MOVE_BG_URL = const.MOVING_BG_URL

# Add moving screen for Background
M_SCREEN = fn.load_scale_image(MOVE_BG_URL, M_SCREEN_WIDTH, M_SCREEN_HEIGHT)

class Mscreen():
    def __init__(self):
        self.x = M_SCREEN_X_POS
        self.y = M_SCREEN_Y_POS
        self.width = M_SCREEN_WIDTH
        self.height = M_SCREEN_HEIGHT

    def draw(self,M_SCREEN_X_POS):
        SCREEN.blit(M_SCREEN, (M_SCREEN_X_POS, M_SCREEN_Y_POS))
        SCREEN.blit(M_SCREEN, (M_SCREEN_X_POS + WINDOWWIDTH, M_SCREEN_Y_POS))