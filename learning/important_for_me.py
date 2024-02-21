# The result of division is always a float

bool(1 < 8) # => True

len("tells the lenght of a strings")

# combining or pre formatting strings
name = "Gandalf"
formatted_string = f"Prepare " + name + " to go out in the rain."
print(formatted_string)

# Don't use the equality "==" symbol to compare objects to None
# Use "is" instead. This checks for equality of object identity.

# By default the print function also prints out a newline at the end.
# Use the optional argument end to change the end string.
print("Hello, World", end="ddddddddddd")  # => Hello, Worldddddddddddd

# Simple way to get input data from console
input_string_var = input("Enter some data: ") # Returns the data as a string

# Arrays
list1 = [3, 2]
list2 = [5, 4]
list1.append(1)
list1.pop() # remove at the end
list1.index(0)

list3 = list2 + list1
list3 = list2.extend(list1)

# Tuples are like lists but are immutable.
tup = (1, 2, 3)
tup[0]      # => 1
tup[0] = 3  # Raises a TypeError

# Note that a tuple of length one has to have a comma after the last element but
# tuples of other lengths, even zero, do not.
type((1))   # => <class 'int'>
type((1,))  # => <class 'tuple'>
type(())    # => <class 'tuple'>

# instead of using brackets python uses indentation fo grouping