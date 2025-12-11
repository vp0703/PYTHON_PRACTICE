setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

print(setA | setB)   # Union -> {1, 2, 3, 4, 5, 6}
print(setA & setB)   # Intersection -> {3, 4}
print(setA - setB)   # Difference -> {1, 2}
print(setA ^ setB)   # Symmetric difference -> {1, 2, 5, 6}
