import math

def slant(rad, hi):
    slant = round((math.sqrt(rad**2 +hi**2)), 2)
    return slant

def surfaceArea(rad, hi):
    area = round((math.pi * rad *(rad + math.sqrt(hi**2 + rad**2))), 2)
    return area

def volume(rad, hi):
    volume = round((math.pi * rad**2 * (hi/3)), 2) 
    return volume

def lateral(rad, hi):
    lateral = round((math.pi * rad * math.sqrt(hi**2 + rad**2)), 2)
    return lateral

def prompt():
    print()
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME & SURFACE AREA OF A CONE")
    print("----------------------------------------------------------")
    radius = int(input("Please Enter the Radius :"))
    height = int(input("Please Enter the Height :"))
    print()
    print("Length of a Side (slant) of a Cone = ", slant(radius, height))
    print("The Surface Area of a Cone = ", surfaceArea(radius, height))
    print("The Volume of a Cone = ", volume(radius, height))
    print("Lateral Surface Area of a Cone = ", lateral(radius, height))
    print()

if __name__ == '__main__':
     prompt()