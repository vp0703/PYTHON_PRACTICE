# 8. File Handling
# --------------------------------------------------
# Read a text file and count number of
# lines, words, and characters.

# File Content:
# Hello World
# Python is great

# Expected Output:
# Lines: 2
# Words: 5
# Characters: 25



# with open("file.txt","w") as f:
# f.write("Hello World\nPython is great")

with open("file.txt","r") as f:
    data = f.read()
    lines = data.splitlines()
    print(f"Lines : {len(lines)}")
    words = data.split()
    print(f"Words : {len(words)}")
    chara = len(data)
    print(f"Characters : {chara}")
