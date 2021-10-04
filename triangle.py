import math

def perimeter(f, s, t):
    perimeter = round((f + s + t), 2)
    return perimeter

def semiPerimeter(f, s, t):
    semi = round(((f + s + t)/2), 2)
    return semi

def area(f, s, t, semi):
    area = round((math.sqrt(semi * (semi-f) * (semi-s) * (semi-t))), 2)
    return area

def prompt():
    print()
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME & SURFACE AREA OF A TRIANGLE")
    print("----------------------------------------------------------")
    first = int(input("Please Enter the First side of a Triangle :"))
    second = int(input("Please Enter the Second side of a Triangle :"))
    third = int(input("Please Enter the Third side of a Triangle :"))
    print()
    print("The Perimeter of a Triangle = ", perimeter(first, second, third))
    print("The Semi Perimeter of a Triangle = ", semiPerimeter(first, second, third))
    semi = semiPerimeter(first, second, third)
    print("The Area of a Triangle is = ", area(first, second, third, semi))
    print("----------------------------------------------------------")
    print()

if __name__ == '__main__':
    prompt()