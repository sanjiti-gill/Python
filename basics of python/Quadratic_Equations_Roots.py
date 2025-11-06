import cmath   # 'cmath' handles complex (imaginary) numbers

print("Quadratic Equation: ax² + bx + c = 0")

# Accept coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Check if 'a' is zero
if a == 0:
    print("This is not a quadratic equation (a cannot be 0).")
else:
    # Calculate discriminant
    d = (b**2) - (4*a*c)

    # Calculate two roots using quadratic formula
    root1 = (-b + cmath.sqrt(d)) / (2*a)
    root2 = (-b - cmath.sqrt(d)) / (2*a)

    # Display results
    print("\nThe roots of the quadratic equation are:")
    print("Root 1 =", root1)
    print("Root 2 =", root2)
