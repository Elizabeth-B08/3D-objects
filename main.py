from shape3d import Shape3D

def main():
    shape = Shape3D("Generic Shape", "Red")

    # Test getters
    print("Type:", shape.get_type())
    print("Colour:", shape.get_colour())

    # Test setters
    shape.set_type("Updated Shape")
    shape.set_colour("Blue")

    print("Updated Type:", shape.get_type())
    print("Updated Colour:", shape.get_colour())

    # Test methods
    print("Volume:", shape.volume())
    print("Surface Area:", shape.surface_area())

if __name__ == "__main__":
    main()