from shape3d import Shape3D

def main():
    shape = Shape3D("Generic Shape", "Red", 1, 1, 1)

    print("Type:", shape.get_type())
    print("Colour:", shape.get_colour())

    shape.set_type("Updated Shape")
    shape.set_colour("Blue")

    print("Updated Type:", shape.get_type())
    print("Updated Colour:", shape.get_colour())

    print("Volume:", shape.volume())
    print("Surface Area:", shape.surface_area())

if __name__ == "__main__":
    main()