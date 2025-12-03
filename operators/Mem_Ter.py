#Membership Operators

print("Membership Operators:")
person = {"name": "Alice", "age": 30, "city": "New York"}
# Using 'in' (checks for keys)
print("Is 'name' a key in the dictionary?:", "name" in person)
print("Is 'country' a key in the dictionary?:", "country" in person)
# Using 'not in' (checks for keys)
print("Is 'address' not a key in the dictionary?:", "address" not in person)


#Ternary Operators

print("\nTernary Operators:")
a, b = 10, 20
min = a if a < b else b
print("min:", min)