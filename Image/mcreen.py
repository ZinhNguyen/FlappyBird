from Utils import constant as const
from Utils import variables as var
from Utils import function as fn

class Mscreen():
    """This is Moving Screen Class"""
    def __init__(self):
        """initial contractor for Moving Screen class"""
        self._x = const.M_SCREEN_X_POS
        self._y = const.M_SCREEN_Y_POS
        self._width = const.M_SCREEN_WIDTH
        self._height = const.M_SCREEN_HEIGHT
        self._surface = fn.load_scale_image(const.MOVING_BG_URL, self._width, self._height)
    def draw(self, M_SCREEN_X_POS):
        """This function will draw 2 Moving Screens into Background With x_pos"""
        var.SCREEN.blit(self._surface, (M_SCREEN_X_POS, self._y))
        var.SCREEN.blit(self._surface, (M_SCREEN_X_POS + const.WINDOWWIDTH, self._y))