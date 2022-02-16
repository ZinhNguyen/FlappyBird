from Utils import constant as const
from Utils import variables as var
from Utils import function as fn

class Arrow():
    """This is class for Arrow"""
    def __init__(self):
        """initial contractor for Arrow class"""
        self._x = const.ARROW_X_POS
        self._y = const.ARROW_Y_POS
        self._width = const.ARROW_WIDTH
        self._height = const.ARROW_HEIGHT
        self._surface = fn.load_scale_image(const.ARROW_URL, self._width, self._height)

    def draw(self):
        """This function will display arrow"""
        var.SCREEN.blit(self._surface, (self._x, self._y))
