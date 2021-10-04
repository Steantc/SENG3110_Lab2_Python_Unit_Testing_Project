import math

def surfaceArea(rad):
    area = round((4 * math.pi * rad**2), 2)
    return area   

def volume(rad):
    volume = round(((4/3) * math.pi * rad**3), 2)
    return volume

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME AND SURFACE AREA OF A SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the Radius :"))

    print("The Surface Area of a Shpere is = ", surfaceArea(radius))
    print("The Volume Area of a Shpere is = ", volume(radius))
    print("------------------------------------------------------------")
    print()
    return radius


if __name__ == '__main__':
    prompt()