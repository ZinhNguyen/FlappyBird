from Utils import constant as const
from Utils import variables as var
from Utils import function as fn

class Background():
    """This is class for Background"""
    def __init__(self):
        """initial contractor for Background class"""
        self._x = const.BG_X_POS
        self._y = const.BG_Y_POS
        self._width = const.WINDOWWIDTH
        self._height = const.WINDOWHEIGHT
        self._surface = fn.load_scale_image(const.BACKGROUND_URL, self._width, self._height)
    def setSurface(self, new_url):
        """This function will update new background"""
        self._surface = fn.load_scale_image(new_url, self._width, self._height)
    def draw(self):
        """This function will display background"""
        var.SCREEN.blit(self._surface, (self._x, self._y))

