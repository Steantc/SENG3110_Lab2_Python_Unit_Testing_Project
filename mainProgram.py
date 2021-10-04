import sphere
def main():

    while True:
        print("Welcome to the geometry program: ")
        print("1. Sphere")
        print("2. cylinder")
        print("0. Quit")
        selection = int(input("Please enter your selection: "))
        if selection == 1:
            sphere.main()        
        if selection == 0:
            break

if __name__ == '__main__':
    main()
