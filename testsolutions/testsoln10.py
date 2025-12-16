# 10. Rotate List
# --------------------------------------------------
# Rotate the list to the right by k positions.

lst = [1, 2, 3, 4, 5]
k = 2
# Expected Output:
# [4, 5, 1, 2, 3]

k = k % len(lst)
rotated = lst[-k:] + lst[:-k]

print(rotated)
