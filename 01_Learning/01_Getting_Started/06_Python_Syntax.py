# ============================================
# Python Syntax Basics
# File: 06_Python_Syntax.py
# ============================================


# --------------------------------------------
# 1. Print Statement: This is the most basic statement in Python used to display output on the screen.
# --------------------------------------------

print("Hello, Arnav!!")


# --------------------------------------------
# 2. Strings: Strings are sequences of characters encloded in single or double quotes.
# --------------------------------------------

print("This is a string.")
print('This is also a string.')


# --------------------------------------------
# 3. Numbers: Numbers are numeric data type in python. They can be integers or floating point numbers.
# --------------------------------------------

print(10)
print(25.5)


# --------------------------------------------
# 4. Basic Arithmetic: Python Supports basic arithmetic operations like addition, subtraction, multiplication and division.
# --------------------------------------------

print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)


# --------------------------------------------
# 5. Variables: Variables are used to store data values. In Python, we do not need to declare the type of variable explicitly. Python automatically assigns the data type based on the value assigned to the variable.
# --------------------------------------------

name = "Arnav"
age = 20

print(name)
print(age)


# --------------------------------------------
# 6. Multiple Values: Python allows us to assign multiple values to multiple variables in a single line.
# --------------------------------------------

first_name = "Arnav"
last_name = "Raj"

print(first_name, last_name) # here we are printing two variables in a single print statement.


# --------------------------------------------
# 7. Comments: Comments are used to explain the code and make it more readable. They are ignored by Python during execution. in Python, comments are created using the '#' symbol. Everything after the '#' symbol on that line is considered a comment and is ignored by Python.

#There are two types of comments in Python: single-line comments and multi-line comments. Single-line comments start with a '#' symbol and continue until the end of the line. Multi-line comments are enclosed within triple quotes (''' or """) and can span multiple lines.
# --------------------------------------------

# This is a single-line comment.

print("Comments are ignored by Python.")


# --------------------------------------------
# 8. Indentation: Indentation is used to define blocks of code in Python. It is important to use consistent indentation (spaces or tabs) to avoid syntax errors. In Python, indentation is used to indicate a block of code that belongs to a specific control structure, such as an if statement or a loop.
# --------------------------------------------

if age >= 18:
    print("You are an adult.")


# --------------------------------------------
# 9. Case Sensitivity: Python is a case-sensitive programming language. This means that variable names, function names, and other identifiers are treated as distinct based on their capitalization. For example, 'myVariable' and 'myvariable' would be considered two different variables in Python.
# --------------------------------------------

language = "Python"

print(language)

# Python is case-sensitive.
# 'language' and 'Language' are different names.


# --------------------------------------------
# 10. Long Variable Names: Python allows for long variable names to improve code readability.
# --------------------------------------------

student_name = "Arnav Raj"

print(student_name)


# --------------------------------------------
# 11. Multiple Statements: Python allows multiple statements to be written on a single line using semicolons (;) to separate them. However, it is generally recommended to write one statement per line for better readability.
# --------------------------------------------

x = 10
y = 20

print(x)
print(y)

# --------------------------------------------
# 12. User Input: Python provides a built in function called input() that allows us to take input from the user. The input() function reads a line from the input (usually from the user) and converts it into a string.
# --------------------------------------------

user_name = input("Enter your name: ")

print("Hello,", user_name)


# --------------------------------------------
# 13. Checking Data Types: Python provides a built-in function called type() that allows us to check the data type of a variable or value. The type() function returns the data type of the specified object.
# --------------------------------------------

name = "Arnav"
age = 20

print(type(name))
print(type(age))




# --------------------------------------------
# End
# --------------------------------------------

print("Python syntax basics completed!")