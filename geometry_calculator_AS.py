   
import sphere
import cylinder
import cone
import cube
import triangle
import trapezoid
import cuboid
import equilateral

def main():

    while True:
        print("\nWelcome to the Geometry Program\n")
        print("1. Sphere")
        print("2. Cylinder")
        print("3. Cone")
        print("4. Cube")
        print("5. Triangle")
        print("6. Trapezoid")
        print("7. Cuboid")
        print("8. Equilateral Triangle")
        print("0. Quit")
        selection = int(input("\nPlease enter your selection: "))
        if selection == 1:
            sphere.prompt()
        elif selection == 2:
            cylinder.prompt()
        elif selection == 3:
            cone.prompt()
        elif selection == 4:
            cube.prompt()
        elif selection == 5:
            triangle.prompt()
        elif selection == 6:
            trapezoid.prompt()
        elif selection == 7:
            cuboid.prompt()
        elif selection == 8:
            equilateral.prompt()
        if selection == 0:
            print("\nProgram Terminating...\n")
            break

if __name__ == '__main__':
    main()