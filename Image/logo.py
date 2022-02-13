from Utils import constant as const
from Utils import variables as var
from Utils import function as fn

SCREEN = var.SCREEN
LOGO_URL = const.LOGO_URL
LOGO_WIDTH = const.LOGO_WIDTH
LOGO_HEIGHT = const.LOGO_HEIGHT
LOGO_X_POS = const.LOGO_X_POS
LOGO_Y_POS = const.LOGO_Y_POS

# Add Logo for Background
LOGO = fn.load_scale_image(LOGO_URL, LOGO_WIDTH, LOGO_HEIGHT)

class Logo():
    def __init__(self):
        self.x = LOGO_X_POS
        self.y = LOGO_Y_POS
        self.width = LOGO_WIDTH
        self.height = LOGO_HEIGHT

    def draw(self):
        SCREEN.blit(LOGO, (LOGO_X_POS, LOGO_Y_POS))