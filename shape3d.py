import math

class Shape:
    def __init__(self, colour, x, y, z):
        self.colour = colour
        self.location = (x, y, z)

    def get_type(self):
        return self.__class__.__name__

    def get_colour(self):
        return self.colour

    def get_location(self):
        return self.location

    def draw(self):
        print(f"Drawing a {self.get_type()}...")

class Shape3D():
    def __init__(self, type, colour, x, y, z):
        self.__type = type
        self.__colour = colour
        self.__x = x
        self.__y = y
        self.__z = z

    # Getters
    def get_type(self):
        return self.__type

    def get_colour(self):
        return self.__colour

    def get_location(self):
        return (self.__x, self.__y, self.__z)

    def set_type(self, new_type):
        self.__type = new_type

    # Setters
    def set_colour(self, colour):
        self.__colour = colour

    def set_location(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    # Methods to override
    def volume(self):
        return None

    def surface_area(self):
        return None

    def draw(self):
        print("Drawing a generic 3D shape")

class Sphere(Shape):
    def __init__(self, colour, x, y, z, radius):
        super().__init__(colour, x, y, z)
        self.radius = radius

    def volume(self):
        return (4/3) * math.pi * self.radius**3

    def surface_area(self):
        return 4 * math.pi * self.radius**2

    def draw(self):
        print("Drawing a sphere:")
        print("  ***  ")
        print(" *   * ")
        print("  ***  ")


class Torus(Shape):
    def __init__(self, colour, x, y, z, R, r):
        super().__init__(colour, x, y, z)
        self.R = R  # major radius
        self.r = r  # minor radius

    def volume(self):
        return (2 * math.pi**2) * self.R * self.r**2

    def surface_area(self):
        return (4 * math.pi**2) * self.R * self.r

    def draw(self):
        print("Drawing a torus (donut shape):")
        print("  ****  ")
        print(" *    * ")
        print("  ****  ")


def main():
    # Create objects
    sphere = Sphere("Red", 0, 0, 0, 5)
    torus = Torus("Blue", 1, 2, 3, 6, 2)

    shapes = [sphere, torus]  # polymorphism

    for shape in shapes:
        print("Type:", shape.get_type())
        print("Colour:", shape.get_colour())
        print("Location:", shape.get_location())
        print("Volume:", shape.volume())
        print("Surface Area:", shape.surface_area())
        shape.draw()
        print("----------------------")


if __name__ == "__main__":
    main()


