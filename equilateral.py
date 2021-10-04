import math

def area(ln):
    area = round((math.sqrt(3)/4 * ln**2), 2)
    return area

def perimeter(ln):
    perimeter = round((3 * ln), 2)
    return perimeter

def semiPerimeter(ln):
    semi = round((0.5 * (ln + ln + ln)), 2)
    return semi

def altitude(ln):
    alt = round((0.5 * math.sqrt(3) * ln), 2)
    return alt

def prompt():
    print()
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME & SURFACE AREA OF A TRIANGLE")
    print("----------------------------------------------------------")
    length = int(input("Please Enter Length of any side of an Eqilateral Triangle: "))
    print()
    print("Area of an Equilateral Triangle = ", area(length))
    print("Perimeter of an Equilateral Triangle = ", perimeter(length))
    print("Semi Perimeter of an Equilateral Triangle = ", semiPerimeter(length))
    print("Altitude of an Equilateral Triangle = ", altitude(length))
    print("----------------------------------------------------------")
    print()

if __name__ == '__main__':
    prompt()