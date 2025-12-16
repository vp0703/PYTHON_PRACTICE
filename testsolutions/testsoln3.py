# --------------------------------------------------
# 3. Divisibility Logic
# --------------------------------------------------
# Print all numbers between 1 and 50
# that are divisible by 4 but not divisible by 8.

# Expected Output:
# [4, 12, 20, 28, 36, 44]

res = (x for x in range(1, 51) if x % 4 == 0 and x % 8 != 0)
print(list(res))