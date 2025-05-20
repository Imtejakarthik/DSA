a  = [1, 2, 3, 4, 5, 6]
b = list(map(lambda x: x * 2 , a))

# However, try to prefer list comprehension
# Use map if you have an already defined function
c = [x*2 for x in a]
print(b)
print(c)