# 7. Exception Handling
# --------------------------------------------------
# Safely divide two numbers and handle division by zero.

a = 10
b = 0
# Expected Output:
# "Cannot divide by zero"

try:
    res = a/b
    print(res)
except ZeroDivisionError:
    print("denominator is Zero, Cannot perform Division")

print("nxt code")