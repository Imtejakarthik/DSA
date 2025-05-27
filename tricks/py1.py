#Value swapping
a, b = 5, 10
print(a, b)
a, b = b, a
print(a, b)
# also possible in a list
myList = [1, 2, 3, 4, 5]
print("Initial list :", myList)
myList[0], myList[1] = myList[1], myList[0]
print("Modified list:", myList)