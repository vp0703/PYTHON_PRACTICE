'''Lists are mutable 
   i.e. we can change/manipulate the data 
   lists have index values starting from 0,1,2,...
   and also has negative index values starting from -1,-2,-3,.... 
   we can access any elements by calling it's index value
   by using index values we can also perform slicing of the list
   while print with the help of index values the starting index value is included but the ending index value is excluded
    '''

lst = [10, "Math", "Science", 30, "40.33"] #simple list

print("element at index value 1 is :", lst[1])    #indexing

print("elements from index value 0 to 4 are :", lst[0: 4]) #slicing

lst.append("99.87")
print("lst after append function :", lst) #adds element at the end of the list

lst2 = [1, 22.34, "DSA"]
lst.extend(lst2)
print("lst after extend function :", lst)

lst.insert(3, 30.66)
print("lst after insert function :", lst)

lst.remove(30)
print("lst after remove function :", lst)

lst.pop(4)
print("lst after pop function :", lst)

lst3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("lst3 :", lst3)
lst3.reverse()
print("lst3 after reverse function :", lst3)

lst3.sort()
print("lst after sort function :", lst3)

lst3.sort(reverse=True)
print("lst after reverse sort function :", lst3)

even_squares = [x**2 for x in lst3 if x % 2 == 0]
print(even_squares)
even_squares1 = [x**2 for x in lst3]
print(even_squares1)