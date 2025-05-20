# Single or double quotes
my_string = 'Hello'
my_string = "Hello"
my_string = "I' m a 'Geek'"

# Escaping with backslash
my_string = 'I\' m a "Geek"'
my_string = 'I\' m a \'Geek\''
print(my_string)  # Output: I'm a 'Geek'

# Triple quotes for multiline strings
my_string = """Hello
World"""
print(my_string)  # Output: Hello\nWorld

# Backslash for line continuation
my_string = ("Hello \
World")
print(my_string)  # Output: Hello World

my_string = "how are you doing"
a = my_string.split() # default argument is " "
print(a)