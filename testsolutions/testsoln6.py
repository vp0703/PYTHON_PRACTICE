# 6. List Comprehension
# --------------------------------------------------
# Find numbers between 1 and 30 that are divisible
# by 3 or 5 but not both.

# Expected Output:
# [3, 5, 6, 9, 10, 12, 18, 20, 21, 24, 25, 27]

lst = [i for i in range(1, 31) if (i % 3 ==0) ^ (i % 5 == 0)]
print(lst)