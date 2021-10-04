import math

def surfaceArea(rad, hi):
    area = round((2 * math.pi * rad * hi) + (2 * math.pi * rad**2), 2)
    return area

def volume(rad, hi):
    volume = round((math.pi * rad**2 * hi), 2) 
    return volume

def lateral(rad, hi):
    lateral = round((2 * math.pi * rad * hi), 2)
    return lateral

def base(rad, hi):
    base = round((math.pi * rad**2), 2)
    return base

def prompt():
    print()
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME & SURFACE AREA OF A CYLINDER")
    print("----------------------------------------------------------")
    radius = int(input("Please Enter the Radius :"))
    height = int(input("Please Enter the Height :"))
    print()
    print("The Surface Area of a Cylinder = ", surfaceArea(radius, height))
    print("The Volume of a Cylinder = ", volume(radius, height))
    print("Lateral Surface Area of a Cylinder = ", lateral(radius, height))
    print("Top OR Bottom Surface Area of a Cylinder = ", base(radius, height))
    print()

if __name__ == '__main__':
    prompt()