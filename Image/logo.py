from Utils import constant as const
from Utils import variables as var
from Utils import function as fn

class Logo():
    """This is Logo Class to display Logo"""
    def __init__(self):
        """initial contractor for Logo class"""
        self._x = const.LOGO_X_POS
        self._y = const.LOGO_Y_POS
        self._width = const.LOGO_WIDTH
        self._height = const.LOGO_HEIGHT
        self._surface = fn.load_scale_image(const.LOGO_URL, self._width, self._height)
    def draw(self):
        """This function will draw Logo into Background"""
        var.SCREEN.blit(self._surface, (self._x, self._y))

class GameOverLogo(Logo):
    """This is GameOverLogo Class inherited from Logo classs to display GameOver Logo"""
    def __init__(self):
        """initial contractor for GameOverLogo class"""
        Logo.__init__(self)
        self._surface = fn.load_scale_image(const.GAMEOVER_LOGO_URL, self._width, self._height)
