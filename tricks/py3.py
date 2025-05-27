# join method is much faster
from timeit import default_timer as timer
my_list = ["a"] * 1000000

# bad
start = timer()
a = ""
for i in my_list:
    a += i
end = timer()
print(end - start)
#print(a)

# good
start = timer()
a = " ".join(my_list)
end = timer()
print(end - start)
#print(a)