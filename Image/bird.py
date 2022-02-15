from Utils import function as fn
from Utils import constant as const
from Utils import variables as var

class Bird():
    """This is default Bird Class"""
    def __init__(self):
        """initial contractor for class"""
        self._width = const.BIRDWIDTH
        self._height = const.BIRDHEIGHT
        self._x = (const.WINDOWWIDTH - self._width)/2 - 30
        self._y = (const.WINDOWHEIGHT - self._height)/2
        self._speed = 0
        self._Angle = 0

    def getWidth(self):
        """This function will return the width of bird"""
        return self._width
    def getHeight(self):
        """This function will return the height of bird"""
        return self._height
    def getX(self):
        """This function will get x_pos of bird"""
        return self._x
    def setY(self, y):
        """This function will set y_pos for bird"""
        self._y = y
    def getY(self):
        """This function will get y_pos of bird"""
        return self._y
    def setSpeed(self, speed):
        """This function will set speed for bird"""
        self._speed = speed
    def setAngle(self, Angle):
        """This function will set Angle for bird"""
        self._Angle = Angle
    def draw(self):
        """This function will draw bird with angle"""
        var.SCREEN.blit(fn.rotate_bird(var.BIRD, self._Angle), (int(self._x), int(self._y)))

    def update(self, mouseClick):
        """This function will update bird when have mouseClick event"""
        self._y += self._speed + 0.5*const.G
        self._speed += const.G
        self._Angle -= const.G*self._speed
        if mouseClick == True:
            self._Angle += 180
            self.setSpeed(const.SPEEDFLY)
        if self._Angle > 20:
            self._Angle = 20
        if self._Angle < -90:
            self._Angle = -90

class RedBird(Bird):
    """This is Brown Bird Class inherited from Bird"""
    def __init__(self):
        """initial contractor for BrownBird class"""
        Bird.__init__(self)
    def draw(self):
        """This function will draw Brownbird with angle"""
        var.SCREEN.blit(fn.rotate_bird(var.REDBIRD, self._Angle), (int(self._x), int(self._y)))


class BlueBird(Bird):
    """This is Blue Bird Class inherited from Bird"""
    def __init__(self):
        """initial contractor for BlueBird class"""
        Bird.__init__(self)
    def draw(self):
        """This function will draw Brownbird with angle"""
        var.SCREEN.blit(fn.rotate_bird(var.BLUEBIRD, self._Angle), (int(self._x), int(self._y)))
