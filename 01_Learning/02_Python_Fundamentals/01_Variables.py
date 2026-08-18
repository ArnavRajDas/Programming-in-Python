# ========================================
# Python Fundamentals - Variables
# ========================================

"""
Variables in Python:
--------------------

A variable is a name used to refer to a value in a program.

A variable is created when a value is assigned to a name
using the assignment operator (=).

Syntax:

    variable_name = value
"""


# ------------------------------------------
# 1. Creating Variables
# ------------------------------------------

# A variable can store different kinds of values.

age = 19
name = "Arnav"
cgpa = 8.55

print(age)
print(name)
print(cgpa)


# ------------------------------------------
# 2. Assignment Operator (=)
# ------------------------------------------

# The '=' operator is called the assignment operator.
# It assigns the value on the right to the variable on the left.

age = 19

print("Age:", age)


# ------------------------------------------
# 3. Reassigning Variables
# ------------------------------------------

# A variable can be assigned a new value later in the program.

age = 19
print("Before:", age)

age = 20
print("After:", age)


# ------------------------------------------
# 4. Variables Can Store Different Values
# ------------------------------------------

# Variables can refer to values of different types.
# Detailed information about data types will be covered
# in the Data Types topic.

student_name = "Arnav"   # String
student_age = 19         # Integer
student_cgpa = 8.9       # Float
is_student = True        # Boolean

print(student_name)
print(student_age)
print(student_cgpa)
print(is_student)


# ------------------------------------------
# 5. Assigning Multiple Variables
# ------------------------------------------

# Variables can be assigned values using separate
# assignment statements.

first_name = "Arnav"
last_name = "Raj"
age = 19

print("First Name:", first_name)
print("Last Name:", last_name)
print("Age:", age)


# ------------------------------------------
# 6. Multiple Assignment
# ------------------------------------------

# Python also allows multiple variables to be assigned
# in a single statement.

name, age, cgpa = "Arnav", 19, 8.9

print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa)


# ----------------------------------------------------
# 7. Assigning the Same Value to Multiple Variables
# ----------------------------------------------------

# The same value can be assigned to multiple variables.

x = y = z = 100

print("x:", x)
print("y:", y)
print("z:", z)



# ------------------------------------------
# 8. Swapping Variables
# ------------------------------------------

# Python allows two variables to be swapped
# without using a temporary variable.

a = 10
b = 20

print("Before:", a, b)

a, b = b, a

print("After:", a, b)


# ------------------------------------------
# 9. Variable Naming Rules
# ------------------------------------------

"""
Rules for naming variables in Python:

1. A variable name can contain:
   - Letters (A-Z, a-z)
   - Digits (0-9)
   - Underscores (_)

2. A variable name cannot start with a digit.

3. A variable name cannot contain spaces.

4. Special characters such as $, @, #, %, etc.
   are not allowed. 
   Or we can say that Special characters are generally not allowed, exccept underscore (_).

5. Python variable names are case-sensitive.

6. Python keywords cannot be used as variable names.

7. Variable names should be meaningful and descriptive.
"""


# ------------------------------------------
# 10. Valid Variable Names
# ------------------------------------------

age = 19
_age = 22
student_age = 20
age2 = 21
_nice_45 = 45
a_b_c_7 = "Sam"

print(age)
print(_age)
print(student_age)
print(age2)
print(_nice_45)
print(a_b_c_7)


# ------------------------------------------
# 11. Invalid Variable Names
# ------------------------------------------

# The following examples are invalid.
# They are kept as comments so the program can still run.

# 34age = 19
# Invalid because a variable name cannot start with a digit.

# student-age = 20
# Invalid because '-' is not allowed in variable names.

# student age = 20
# Invalid because spaces are not allowed.

# a$$ge = 20
# Invalid because '$' is not allowed in variable names.

# @age = 20
# Invalid because '@' is not allowed in variable names.


# ------------------------------------------
# 12. Variable Names are Case Sensitive
# ------------------------------------------

name = "Arnav"
Name = "Shreya"

print("name:", name)
print("Name:", Name)

# 'name' and 'Name' are different variable names.


# -------------------------------------------------------
# 13. Python Keywords Cannot Be Used as Variable Names
# -------------------------------------------------------

# Python has reserved keywords that have special meanings.
# These keywords cannot be used as variable names.

# Examples of Python keywords:
# if
# else
# for
# while
# class
# def
# return
#
# Special constants:
# True
# False
# None

# Example of an invalid variable:
# class = "Python"

# This will produce a SyntaxError.


# ------------------------------------------
# 14. Meaningful Variable Names
# ------------------------------------------

# Variable names should clearly describe the data they contain.

# Not recommended:
x = 85

# Better:
student_marks = 85

print("Marks:", student_marks)


# Another example:

# Not recommended:
n = "Arnav"

# Better:
student_name = "Arnav"

print("Student:", student_name)


# ------------------------------------------
# 15. Python Naming Convention
# ------------------------------------------

# Python commonly uses snake_case for variable names.

student_name = "Arnav"
student_age = 19
total_marks = 450
average_marks = 90.0

print(student_name)
print(student_age)
print(total_marks)
print(average_marks)


# Avoid names like:

# studentName
# StudentName
# STUDENTNAME

# Prefer:

student_name = "Arnav"


# ------------------------------------------
# 16. Variable Values Can Be Changed
# ------------------------------------------

# Variables are not permanently fixed to one value.
# They can be reassigned during program execution.

score = 50

print("Initial score:", score)

score = 75

print("Updated score:", score)

score = 95

print("Final score:", score)


# ------------------------------------------
# 17. Using Variables in Expressions
# ------------------------------------------

# Variables can be used in calculations and expressions.

number1 = 10
number2 = 20

sum_result = number1 + number2

print("Number 1:", number1)
print("Number 2:", number2)
print("Sum:", sum_result)


# ------------------------------------------
# 18. Checking a Variable's Type
# ------------------------------------------

# The type() function can be used to check the type
# of the value referred to by a variable.
#
# Detailed study of data types will be covered separately.

age = 19
name = "Arnav"
cgpa = 8.9

print(type(age))
print(type(name))
print(type(cgpa))


# ------------------------------------------
# 19. Important Variable Concepts
# ------------------------------------------

"""
Remember:

    variable_name = value

Example:

    age = 19

Here:

    age  -> variable name
    =    -> assignment operator
    19   -> value
"""


# -------------------------
# Key Points
# -------------------------

"""
1. A variable is a name used to refer to a value. 

2. The '=' operator is used for assignment.

3. Variables can be reassigned.

4. A variable name can contain:
   - Letters
   - Digits
   - Underscores

5. A variable name cannot start with a digit.

6. Spaces and special characters are not allowed
   in variable names.

7. Variable names are case-sensitive.

8. Python keywords cannot be used as variable names.

9. Use meaningful and descriptive variable names.

10. Python commonly follows snake_case for variable names.

11. Variables can be used in expressions and calculations.

12. The type() function can be used to check the
    type of a variable's value.
"""


# =============================
# End of Variables
# =============================

print("\nVariables topic completed!")