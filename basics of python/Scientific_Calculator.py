import math

while True:
    print("\n===== SCIENTIFIC CALCULATOR =====")
    print("1. sin(x)")
    print("2. cos(x)")
    print("3. tan(x)")
    print("4. log(x)")      # Natural logarithm (base e)
    print("5. log10(x)")    # Logarithm base 10
    print("6. exp(x)")      # e^x
    print("7. sqrt(x)")     # Square root
    print("8. Power (x^y)")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == '9':
        print("Exiting Scientific Calculator. Goodbye!")
        break

    # For single-argument operations
    if choice in ['1','2','3','4','5','6','7']:
        x = float(input("Enter value of x: "))

        if choice == '1':
            print("sin(", x, ") =", math.sin(math.radians(x)))
        elif choice == '2':
            print("cos(", x, ") =", math.cos(math.radians(x)))
        elif choice == '3':
            print("tan(", x, ") =", math.tan(math.radians(x)))
        elif choice == '4':
            if x <= 0:
                print("Error! log(x) undefined for x <= 0")
            else:
                print("log(", x, ") =", math.log(x))
        elif choice == '5':
            if x <= 0:
                print("Error! log10(x) undefined for x <= 0")
            else:
                print("log10(", x, ") =", math.log10(x))
        elif choice == '6':
            print("exp(", x, ") =", math.exp(x))
        elif choice == '7':
            if x < 0:
                print("Error! sqrt(x) undefined for x < 0")
            else:
                print("sqrt(", x, ") =", math.sqrt(x))

    # For power operation
    elif choice == '8':
        x = float(input("Enter base (x): "))
        y = float(input("Enter exponent (y): "))
        print(x, "^", y, "=", math.pow(x, y))

    else:
        print("Invalid choice! Please enter a number between 1 and 9.")
