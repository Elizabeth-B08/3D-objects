class Shape3D:

    def __init__(self, type, colour, x, y, z):
        self.__type = type
        self.__colour = colour
        self.__x = x
        self.__y = y
        self.__z = z

    # getters
    def get_type(self):
        return self.__type

    def get_colour(self):
        return self.__colour

    def get_location(self):
        return (self.__x, self.__y, self.__z)

    # setters
    def set_colour(self, colour):
        self.__colour = colour

    def set_location(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    # methods to override
    def volume(self):
        return None

    def surface_area(self):
        return None

    def draw(self):
        print("Drawing a generic 3D shape")
