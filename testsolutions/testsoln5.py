# 5. Armstrong Number
# --------------------------------------------------
# Check whether the given number is an Armstrong number.

num = 153
# Expected Output:
# True

digi = [int(d) for d in str(num)]
power = len(digi)

is_armst = sum(d ** power for d in digi) == num
print(is_armst)
