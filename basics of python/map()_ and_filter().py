
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Original list:", numbers)

# Using map() to square each number
squared = list(map(lambda x: x * x, numbers))
print("\nAfter using map() to square each number:")
print(squared)

# Using filter() to get even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("\nAfter using filter() to get even numbers:")
print(evens)
