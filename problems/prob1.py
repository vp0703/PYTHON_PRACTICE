#12/12/25

"""Q1 - Given two integer numbers, write a Python program to return their product only if 
the product is equal to or lower than 1000. Otherwise, return their sum"""

def pronum(num1, num2):
    product = num1*num2
    if(product <=1000):
        print(num1*num2)
    else:
        print(num1+num2)
        
d = pronum(20, 30)
d = pronum(40, 30) 

#o/p: 600 
#     70



"""Q2 - Write Python code to iterate through the first 10 numbers and, in each iteration, 
print the sum of the current and previous number."""

print ("Printing current and previous number sum in a range (10)")
pre = 0
for i in range (1, 11):
    sum = pre + i
    print(f"Current Number {i} previous Number {pre} sum: {sum}")
    pre = i

# #o/p: Printing current and previous number sum in a range (10)
# Current Number 1 previous Number 0 sum: 1
# Current Number 2 previous Number 1 sum: 3
# Current Number 3 previous Number 2 sum: 5
# Current Number 4 previous Number 3 sum: 7
# Current Number 5 previous Number 4 sum: 9
# Current Number 6 previous Number 5 sum: 11
# Current Number 7 previous Number 6 sum: 13
# Current Number 8 previous Number 7 sum: 15
# Current Number 9 previous Number 8 sum: 17
# Current Number 10 previous Number 9 sum: 19



"""Q3 - Write a Python code to accept a string from the user and display characters present 
at an even index number.
For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’."""

w = list(input("Enter a word :"))
print ("original String:", w)
for i in w[0::2]:
    print(i)

# i/p: PYnative

# o/p: original String: ['P', 'Y', 'n', 'a', 't', 'i', 'v', 'e']
# P
# n
# t
# v



"""Q4 - Write a Python code to remove characters from a string from 0 to n and return a 
new string."""

def remove_char(w, n):
    print("original string:", w)
    return(w[n:])
    
print("Removing characters from a string")
print(remove_char("pynative", 4))
print(remove_char("pynative", 2))

#o/p: tive
#     native



"""Q5 - Write a code to return True if the list’s first and last numbers are the same. 
If the numbers are different, return False"""

num = list(input().split())
if(num[0] == num[-1]):
    print("True")
else:
    print("False")

# #i/p 1 : 10 20 30 40 10 
#      2 : 75 65 35 75 30
# #o/p 1 : True
#      2 : False



"""Q6 - Write a Python code to display numbers from a list divisible by 5"""

ip = input("Enter number :")
lst = [int(i) for i in ip.replace(",", " ").split()]

for i in lst:
    if (i % 5==0):
        print(i)

# ip : 10, 20, 33 45 55 60, 77
# op : 10 20 45 55 60



"""Q7 - Write a Python code to find how often the substring appears in the given string."""

str = input()
substr = input()
print(f"{substr} appeared {str.count(substr)} times")

# i/p : Emma is a good coder. Emma is too smart
# Emma
#o/p : Emma appeared 1 times



"""Q8 - Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5"""

for i in range (1, 6):
    print((str(i)+" ")*i)



"""Q9 - Print the following pattern
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1"""

for i in range (5, 0, -1):
    print((str(i)+" ")*i)



"""Q10 -Given two lists of numbers, write Python code to create a new list containing odd
 numbers from the first list and even numbers from the second list. """

lst1 = input()
lst2 = input()
lst1 = [int(x.strip()) for x in lst1.replace(",", " ").split()]
lst2 = [int(x.strip()) for x in lst2.replace(",", " ").split()]
res = []
for i in lst1:
    if i % 2 != 0:
        res.append(i)

for i in lst2:
    if i % 2 == 0:
        res.append(i)

print(res)

# i/p : 10, 20, 25, 30, 35
#       40, 45, 60, 75, 90
# o/p : [25, 35, 40, 60, 90]



"""Q11 - The multiplication table from 1 to 10 is a table that shows the products of numbers from 1 to 10.

Write a code to generates a complete multiplication table for numbers 1 through 10"""

for n in range(1, 11):
    for i in range(1, 11):
        print(n*i, end=" ")
    print("\n\n")

# o/p : 1 2 3 4 5 6 7 8 9 10 


# 2 4 6 8 10 12 14 16 18 20 


# 3 6 9 12 15 18 21 24 27 30 


# 4 8 12 16 20 24 28 32 36 40 


# 5 10 15 20 25 30 35 40 45 50 


# 6 12 18 24 30 36 42 48 54 60 


# 7 14 21 28 35 42 49 56 63 70 


# 8 16 24 32 40 48 56 64 72 80 


# 9 18 27 36 45 54 63 72 81 90 


# 10 20 30 40 50 60 70 80 90 100 



"""Q12 - Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp."""

def EXP():
    base = int(input("Enter a integer :"))
    exp = int(input("Enter a non -ve integer :"))
    res = base**exp
    print(f"{base} raises to the power of {exp} is :", res)
EXP()

# i/p : 5
#       4
# o/p : 5 raises to the power of 4 is : 625



"""Q13 - Capitalize the first letter of each word in a string"""

def caps(txt):
    cap = txt.split()
    cap1 = [word.capitalize() for word in cap]
    return " ".join(cap1)
txt = input("enter a string :")
print(caps(txt))

# i/p : pynative.com is for python lovers
# o/p : Pynative.com Is For Python Lovers 



"""Q14 - Write a code to create a simple countdown timer of seconds using a while loop, take input for number of seconds from user.

Once the timer finishes (when the remaining time reaches zero), print a “Time’s up!” message."""

import time
def timer(sec):
    while sec > 0:
        print(f"Time remaining : {sec} seconds")
        time.sleep(1)
        sec -=1
    
    print("Time's up!!")
drn = int(input("Enter a number to start a countdown :\n"))
timer(drn)

# i/p : Enter a number to start a countdown :
#       9
# o/p : Time remaining : 9 seconds
#       Time remaining : 8 seconds
#       Time remaining : 7 seconds
#       Time remaining : 6 seconds
#       Time remaining : 5 seconds
#       Time remaining : 4 seconds
#       Time remaining : 3 seconds
#       Time remaining : 2 seconds
#       Time remaining : 1 seconds
#       Time's up!!



"""Q15 - """