import math

def area(b1, b2, hi):
    area = round(((b1 + b2)/2 * hi), 2)
    return area

def median(b1, b2):
    median = round((0.5 * (b1 + b2)), 2)
    return median


def prompt():
    print()
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME & SURFACE AREA OF A TRAPEZOID")
    print("----------------------------------------------------------")
    base1 = int(input("Please Enter the base1 :"))
    base2 = int(input("Please Enter the base2 :"))
    height = int(input("Please Enter the height :"))
    print()
    print("Area of a Trapezoid = ", area(base1, base2, height))
    print("Median of a Trapezoid = ", median(base1, base2))
    print("----------------------------------------------------------")
    print()

if __name__ == '__main__':
    prompt()