#Checking for Vowels

s = input("Enter string: ")
i = 0
count = 0
vowels = "aeiouAEIOU"

while i < len(s):
    if s[i] in vowels:
        count += 1
    i += 1

print("Vowel count =", count)