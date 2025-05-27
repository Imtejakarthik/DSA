#Create a single string from list
my_list = ["I", "am", "awesome"]

# bad
a = ""
for i in my_list:
    a += i + " "
print(a)

# good
a = " ".join(my_list)
print(a)