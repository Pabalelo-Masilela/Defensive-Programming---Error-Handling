# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")
#Syntax error - The print function needs the statement to be enclosed in brackets.
print ("\n")
# Syntax error - The new line is not supposed to be indented if not following a control function line.


# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24"
# Syntax error - The new line is not supposed to be indented if not following a control function line.The definition of a variable should only use one '='
# Running error - 24 should be entered as an intereger, with no quoataion marks and words to be recognised for calculations.
age = int(age_Str) 
# Syntax error - The new line is not supposed to be indented if not following a control function line.
# Running error - age_Str cannot be converted from a string sentence into an intereger.
print("I'm " + age_Str + " years old.")
# Syntax error - The new line is not supposed to be indented if not following a control function line.
# Running error - A print function cannot concetenate a string with interegers.

# Variables declaring additional years and printing the total years of age
years_from_now = 3
months_from_now = 6
# Syntax error - The new line is not supposed to be indented if not following a control function line.
# Running error - Placing the years_from_now value into quotation mark makes it a string instead of an intereger abale to be used in calculations.
total_years = age + years_from_now
# Syntax error - The new line is not supposed to be indented if not following a control function line.
# Running error - age and years_from_now would not be able to run in a calculation if not converetd or captured correctly into interegers

print("The total number of years:" + str(total_years))
# Syntax error - Statement to be printed must be enclosed inside a bracket set.
# Running error - total_years needs to be cast into a string in order for the print function to be able to concetanate the rest of the string.

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = ((total_years) * 12) + months_from_now
# Logical error - The calculation "toatl years * 12" did not factor in the additional 6 months described in line 39 and therfore gave an incorrect total
# Running error - 'total' is not a defined variable, a calculation cannot be referrence from an undefined variable.
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")
# Syntax error - Statement to be printed must be enclosed inside a bracket set.
# Running error - total_months needs to be cast into a string in order for the print function to be able to concetanate the rest of the string.

#HINT, 330 months is the correct answer