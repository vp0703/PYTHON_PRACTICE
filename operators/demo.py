# lst = [10, 20, 20, 30, 40, 10, 20, 30, 20]
# #lss = []
# #lss = sorted(set(lst))
# ls1 = lst.count(10)
# ls2 = lst.count(20)
# ls3 = lst.count(30)
# ls4 = lst.count(40)
# freq_dict={10: ls1, 20: ls2, 30: ls3, 40: ls4}
# print(freq_dict)

#print("[{ 10:", ls1, "},","{ 20:", ls2, "},","{ 30:", ls3, "},","{ 40:", ls4,"}]")

#nm="my name is {} and i am learning python for the {}st time".format("Sita", 1)
#print(nm)

#num = 28
#print(type(num))
#s=repr(num)
#print(s)
#print(type(s))

# t = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("Enter a Number to be searched in the tuple:"))
# i = 0
# for el in t:
#     if(el==x):
#         print("No. Found at index:", i)
#     i+=1
#     break
# else:
#     print("NO.not found")

# n = 1
# while n<=100:
# #     print(n)
# #     n+=1

# n = 100
# while n>=1:
#     print(n)
#     n-=1

# n = int(input("Enter a no. to be displayed multiplication table of:"))
# i = 1
# while i<=10:
#     print(n*i)
#     i+=1

# l = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i=0
# while i<len(l):
#     print(l[i])
#     i+=1

# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("Enter a Number to be searched in the tuple:"))
# i=0
# while i<len(tup):
#     if(tup[i]==x):
#         print("Found at index:", i)
#         break
#     i+=1
    
# else:
#     print("Not Found")

# l = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for x in l:
#     print(x)

# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("enetr a no. to be searched in the tuple:"))
# i=0
# for elm in tup:
#     if(elm==x):
#         print("element found at index:", i)
#         break
#     i+=1
# else:
#     print("no. not found")

# for i in range(100, 0, -1):
#     print(i)

# n=int(input("Enter a no. :"))
# fact=1
# for i in range(1, n+1):
#     fact*=i
# print("factorial of number", n, "is:", fact)

# n = int(input("Enter a no.:"))
# def check(n):
#     if(n % 2 == 0):
#         print("EVEN No.")
#     else:
#         print("ODD No.")
# check(n)

x = "Hello"

def myfunc():
    global y
    y = "World"
myfunc()
print(x+ " " +y)