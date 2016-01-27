class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return(self.__x)

    def set_x(self, x):
        self.__x = x


class Pixel(Point):
    def __init__(self, x, y, rgb):
        super().__init__(x, y)
        self._r = rgb[0]
        self._g = rgb[1]
        
