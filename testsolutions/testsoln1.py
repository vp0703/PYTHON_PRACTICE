# --------------------------------------------------
# 1. Third Largest Element
# --------------------------------------------------
# Find the third largest number in the list.

nums = [10, 45, 23, 89, 67, 45]

# Expected Output:
# 45

third_largest = sorted(set(nums), reverse=True)[2]
print(third_largest)