
import math
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


gcd = math.gcd(a, b)

# LCM formula: (a * b) / gcd
lcm = abs(a * b) // gcd

print(f"GCD of {a} and {b} is: {gcd}")
print(f"LCM of {a} and {b} is: {lcm}")
