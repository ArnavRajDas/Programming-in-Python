# =======================================
# Python Fundamentals - Data Types
# =======================================

"""
Data Types in Python
--------------------

A data type defines the kind of value that a variable
can refer to.

Python provides several built-in data types.

In this file, we will learn about commonly used
built-in data types:

    1. int        -> Integer numbers
    2. float      -> Decimal numbers
    3. complex    -> Real and imaginary numbers
    4. bool       -> True or False
    5. str        -> Text

    6. list       -> Ordered, mutable collection
    7. tuple      -> Ordered, immutable collection
    8. set        -> Unordered collection of unique values
    9. dict       -> Collection of key-value pairs
    10. NoneType  -> The type of the None value

    Detailed operations and methods for these data types

    Detailed operations and methods for these data types
    will be covered separately.

The type() function can be used to check the data type
of a value.


"""



# --------------------------
# 1. Integer (int)
# --------------------------

"""
Integer (int)
--------------

An integer is a whole number without a decimal point.

Examples:

    10
    0
    -5
    97

Integers can be positive, negative, or zero.
"""

age = 19
score = 97
temperature = -5
number = 0

print("Age:", age)
print("Score:", score)
print("Temperature:", temperature)
print("Number:", number)

print("Type of age:", type(age))


# More examples

positive_number = 50
negative_number = -25
zero = 0

print(positive_number)
print(negative_number)
print(zero)


# --------------------------
# 2. Float (float)
# --------------------------

"""
Float (float)
-------------

A float represents a number with a decimal point.

Examples:

    3.14
    8.9
    -2.5
    0.0
"""

cgpa = 8.9
price = 99.99
temperature = -2.5
value = 0.0

print("CGPA:", cgpa)
print("Price:", price)
print("Temperature:", temperature)
print("Value:", value)

print("Type of cgpa:", type(cgpa))


# More examples

pi = 3.14159
height = 5.8
balance = -100.50

print(pi)
print(height)
print(balance)


# --------------------------
# 3. Complex (complex)
# --------------------------

"""
Complex (complex)
------------------

Complex numbers contain a real part and an imaginary part.

    Real part + Imaginary part

Python uses 'j' to represent the imaginary part.

Example:

    3 + 4j

Here:

    3 -> Real part
    4j -> Imaginary part
"""

number = 3 + 4j

print("Complex number:", number)
print("Type:", type(number))


# Accessing the real and imaginary parts

print("Real part:", number.real)
print("Imaginary part:", number.imag)


# More examples

number1 = 2 + 3j
number2 = -5 + 7j

print(number1)
print(number2)


# --------------------------
# 4. Boolean (bool)
# --------------------------

"""
Boolean (bool)
--------------

A Boolean represents one of two possible values:

    True
    False

Boolean values are commonly used when representing
whether something is true or false.
"""

is_student = True
is_adult = False

print("Is student:", is_student)
print("Is adult:", is_adult)

print("Type of is_student:", type(is_student))


# Boolean values can also be produced by comparisons

age = 19

print(age >= 18)
print(age < 18)

print(type(age >= 18))


# More examples

is_logged_in = True
has_permission = False

print("Logged in:", is_logged_in)
print("Has permission:", has_permission)


# --------------------------
# 5. String (str)
# --------------------------

"""
String (str)
-------------

A string is a sequence of characters used to represent text.

Strings can be written using:

    Single quotes: 'Python'
    Double quotes: "Python"
"""

name = "Arnav"
language = 'Python'

print("Name:", name)
print("Language:", language)

print("Type of name:", type(name))


# Strings can contain spaces

message = "Welcome to Python Programming"

print(message)


# An empty string is also a string

empty_text = ""

print("Empty string:", empty_text)
print("Type:", type(empty_text))


# -----------------------------
# 6. Basic String Operations
# -----------------------------

"""
A few basic operations can be performed on strings.

Detailed string manipulation will be covered in the
Strings section later in the learning journey.
"""

first_name = "Arnav"
last_name = "Raj"

full_name = first_name + " " + last_name

print("Full name:", full_name)


# len() returns the number of characters in a string

language = "Python"

print("Length:", len(language))


# Indexing allows us to access individual characters

print("First character:", language[0])
print("Last character:", language[-1])


# --------------------------
# 7. List (list)
# --------------------------

"""
List (list)
-------------

A list is an ordered and mutable collection of values.

Lists can store multiple values, and the values do not
have to be of the same data type.

Lists are written using square brackets:

    [ ]

Example:

    [10, 20, 30]
"""

marks = [85, 90, 78]

print("Marks:", marks)
print("Type:", type(marks))

# Lists are ordered, so individual elements can be
# accessed using their index.

print("First mark:", marks[0])
print("Last mark:", marks[-1])

# Lists are mutable, so their values can be changed.

marks[0] = 95

print("Updated marks:", marks)




# --------------------------
# 8. Tuple (tuple)
# --------------------------

"""
Tuple (tuple)
-------------

A tuple is an ordered and immutable collection of values.

Tuples are commonly written using parentheses:

    ( )

Example:

    (10, 20, 30)

Unlike lists, tuple elements cannot be changed after
the tuple is created.
"""

point = (10, 20, 30)

print("Point:", point)
print("Type:", type(point))

print("First coordinate:", point[0])
print("Last coordinate:", point[-1])

# Tuples are immutable.

# point[0] = 100
# This would raise a TypeError.



# ----------------------
# 9. Set (set)
# ----------------------

"""
Set (set)
---------

A set is an unordered collection of unique values.

Sets are written using curly braces:

    { }

Duplicate values are automatically removed.
"""

numbers = {10, 20, 30, 30, 40, 30}

# Duplicate values are automatically removed.
# Only one 30 will be stored in the set.

print("Numbers:", numbers)
print("Type:", type(numbers))



# ------------------------------
# 10. Dictionary (dict)
# ------------------------------


"""
Dictionary (dict)
-----------------

A dictionary stores data in key-value pairs.

Dictionaries are written using curly braces:

    {key: value}

Example:

    {"name": "Arnav", "age": 19}
"""

student = {
    "name": "Arnav",
    "age": 19,
    "course": "BTech"
}

print("Student:", student)
print("Type:", type(student))

print("Name:", student["name"])
print("Age:", student["age"])



# -----------------------------------
# 11. None and NoneType
# -----------------------------------

"""
None
----

None represents the absence of a value.

The type of None is NoneType.

None is commonly used when a variable currently
has no value.
"""

result = None

print("Result:", result)
print("Type:", type(result))




# ---------------------------------------
# 12. Checking Data Types with type()
# ---------------------------------------

"""
The type() function returns the type of a value.

Syntax:

    type(value)
"""

integer_value = 10
float_value = 10.5
complex_value = 2 + 3j
boolean_value = True
string_value = "Python"

list_value = [1, 2, 3]
tuple_value = (1, 2, 3)
set_value = {1, 2, 3}
dictionary_value = {"name": "Arnav"}
none_value = None

print(type(integer_value))
print(type(float_value))
print(type(complex_value))
print(type(boolean_value))
print(type(string_value))

print(type(list_value))
print(type(tuple_value))
print(type(set_value))
print(type(dictionary_value))
print(type(none_value))



# ---------------------------------------
# 13. Data Types and Variables
# ---------------------------------------

"""
Python is dynamically typed.

A variable does not have to be permanently associated
with one specific data type.

The same variable can refer to values of different
types at different points in a program.
"""

value = 10
print(value)
print(type(value))

value = "Python"
print(value)
print(type(value))

value = 3.14
print(value)
print(type(value))

value = True
print(value)
print(type(value))



# ---------------------------------------
# 14. Data Type Summary
# ---------------------------------------

"""
Data Type Summary

int       -> Whole numbers
float     -> Decimal / floating-point numbers
complex   -> Real and imaginary numbers
bool      -> True or False
str       -> Text / sequence of characters
list      -> Ordered, mutable collection
tuple     -> Ordered, immutable collection
set       -> Unordered collection of unique values
dict      -> Key-value pairs
NoneType  -> The type of the None value
"""


# -------------------------
# 15. Important Notes
# -------------------------

"""
Important Notes
---------------

1. The type() function can be used to check the data type
   of a value.

2. Python is dynamically typed, so a variable can refer
   to values of different data types during execution.

3. Lists are mutable, while tuples are immutable.

4. Sets store unique values and do not guarantee
   a particular order.

5. Dictionaries store data using key-value pairs.

6. None represents the absence of a value.

7. Detailed operations and methods for these data types
   will be covered in their respective topics.

8. Type conversion will be covered separately in:

       03_Type_Conversion.py
"""



# ============================================================
# End of Data Types
# ============================================================

print("\nData Types topic completed!")