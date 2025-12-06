packed_data = 10, "hello", 3.14
# Unpacking a previously packed tuple
a, b, c = packed_data

print(f"Unpacked 'a': {a}")
print(f"Unpacked 'b': {b}")
print(f"Unpacked 'c': {c}")

# Unpacking with the '*' operator for variable assignment
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers

print(f"First element: {first}")
print(f"Middle elements (as a list): {middle}")
print(f"Last element: {last}")