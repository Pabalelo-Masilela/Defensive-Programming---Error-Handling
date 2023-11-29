# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal ="Lion"
animal_type = "cub"
# Syntax erroe- A string of charecters/letters is already recogbised a string and does not need to be in quotation marks
number_of_teeth = 16
# Full spec varaible was removed because its function is able to be well correclt executed in line 13 using an f string correctly. 
# Syntax error - A way of concetenation without "+" is an f-string and that needs an f, triple quoataion and a closed bracket set to be interpreted correctly.
# Logical error - 'animal_type' and 'number_of teeth' variable were not placed in correct sense in reference to the sentence to be printed and understood.
print(f'''This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth''')
