#Assignment Operators

print("Assignment Operators:")
c = 10
d = c
print(d)
c += d #sum
print("SUM:", d) 
c -= d #sub
print("SUB:", d) 
c *= d #multiply
print("MULTIPICATION:", d)
d <<= c #bitwise left shift assignment operator
print("left shift:", d)


#identity Operators

print("\nidentity Operators:")
a = 10
b = 20
c = a
print(a is not b)
print(a is c)