import math

def area(ln, wd , hi):
    area = round(((2 * ln * wd) + (2 * ln * hi) + (2* hi * wd)), 2)
    return area

def volume(ln, wd , hi):
    volume = round((ln * wd * hi), 2)
    return volume

def lateral(ln, wd , hi):
    lateral = round((2 * (ln + wd) * hi), 2)
    return lateral


def prompt():
    print()
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME & SURFACE AREA OF A CUBOID")
    print("----------------------------------------------------------")
    length = int(input("Please Enter the length :"))
    width = int(input("Please Enter the width :"))
    height = int(input("Please Enter the height :"))
    print()
    print("Area Surface Area of a Cuboid = ", area(length, width, height))
    print("The Volume of a Cuboid = ", volume(length, width, height))
    print("The Lateral Surface Area of a Cuboid = ", lateral(length, width, height))
    print("----------------------------------------------------------")
    print()

if __name__ == '__main__':
    prompt()