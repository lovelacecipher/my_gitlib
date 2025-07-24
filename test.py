# Import our function from the library
from mygitlib import say_hello, add_numbers, make_uppercase, save_to_file

# test greeting
print(say_hello("Ian"))

# test math
print("2 + 3 =", add_numbers(2,3))

# test string
print(make_uppercase("this should be uppercase"))

# test file saving
print(save_to_file("example.txt", "this is a test file"))
