# --------------------------------------------------
# 2. Palindrome String
# --------------------------------------------------
# Check whether the string is a palindrome.
# Ignore spaces and case sensitivity.

text = "Never Odd Or Even"
# Expected Output:
# True

str = text.replace(" ", "").lower()
palindrome = str == str[::-1]

print(palindrome)
