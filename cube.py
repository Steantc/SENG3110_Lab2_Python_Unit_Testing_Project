import math

def surfaceArea(ln):
    area = round((6 * ln**2), 2)
    return area   

def volume(ln):
    volume = round((ln**3), 2)
    return volume

def lateral(ln):
    lateral = round((4* ln**2), 2)
    return lateral

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME AND SURFACE AREA OF A CUBE")
    print("------------------------------------------------------------")
    length = int(input("Please Enter the Length of any Side of a Cube :"))

    print("The Surface Area of a Cube is = ", surfaceArea(length))
    print("The Volume Area of a Cube is = ", volume(length))
    print("Lateral Surface Area of a Cube = ", lateral(length))
    print("------------------------------------------------------------")
    print()
    return length


if __name__ == '__main__':
    prompt()