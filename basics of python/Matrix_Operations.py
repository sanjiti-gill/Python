# Matrix Addition, Subtraction and Multiplication

# Input matrix A
r1 = int(input("Enter rows for Matrix A: "))
c1 = int(input("Enter columns for Matrix A: "))
A = []
print("Enter elements of Matrix A:")
for i in range(r1):
    row = []
    for j in range(c1):
        val = int(input("Enter element: "))
        row.append(val)
    A.append(row)

# Input matrix B
r2 = int(input("\nEnter rows for Matrix B: "))
c2 = int(input("Enter columns for Matrix B: "))
B = []
print("Enter elements of Matrix B:")
for i in range(r2):
    row = []
    for j in range(c2):
        val = int(input("Enter element: "))
        row.append(val)
    B.append(row)

# Menu
print("\nSelect operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
ch = int(input("Enter choice (1/2/3): "))

# Addition
if ch == 1:
    if r1 == r2 and c1 == c2:
        C = []
        for i in range(r1):
            row = []
            for j in range(c1):
                row.append(A[i][j] + B[i][j])
            C.append(row)
        print("\nResult (A + B):")
        for row in C:
            print(row)
    else:
        print("Error: Matrices must have same size for addition.")

# Subtraction
elif ch == 2:
    if r1 == r2 and c1 == c2:
        C = []
        for i in range(r1):
            row = []
            for j in range(c1):
                row.append(A[i][j] - B[i][j])
            C.append(row)
        print("\nResult (A - B):")
        for row in C:
            print(row)
    else:
        print("Error: Matrices must have same size for subtraction.")

# Multiplication
elif ch == 3:
    if c1 == r2:
        C = []
        for i in range(r1):
            row = []
            for j in range(c2):
                sum = 0
                for k in range(c1):
                    sum += A[i][k] * B[k][j]
                row.append(sum)
            C.append(row)
        print("\nResult (A × B):")
        for row in C:
            print(row)
    else:
        print("Error: Columns of A must equal rows of B for multiplication.")

else:
    print("Invalid choice!")
