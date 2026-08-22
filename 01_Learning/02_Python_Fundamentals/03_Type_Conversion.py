# =========================================
# Python Fundamentals - Type Conversion
# =========================================

"""
Type Conversion in Python:
---------------------------

Type conversion means changing a value from one data type
to another data type.

Python provides built-in functions such as:

    int()
    float()
    str()
    bool()

These functions can be used to convert values between
different data types.

For Example:
    
    "10"  -->  10

Here, a string is converted into an integer.
"""


# ---------------------------------------
# 1. Why Do We Need Type Conversion?
# ---------------------------------------

"""
Different data types work in different ways.

For example, if we do this:

    "10" + "20"

Python joins the two strings, so we get:

    "1020"

But if they are integers:

    10 + 20

we get:

    30


Type conversion allows us to convert values into the
appropriate data type when required.
"""

num1 = "10"
num2 = "20"

print(num1 + num2)  # Output: 1020

num1 = int(num1)
num2 = int(num2)

print(num1 + num2)  # Output: 30


# ---------------------------------------
# 2. Convert String to Integer
# ---------------------------------------

"""
int()
------

We can use int() when we want to convert something into
an integer, when the conversion is valid.

Example:

    "10" --> 10
"""

num_str = "10"
num_int = int(num_str)

print(num_int)          # Output: 10
print(type(num_int))    # Output: <class 'int'>


# Example

age = "19"

age = int(age)

print(age)
print(type(age))


# -----------------------------------
# 3. Convert String to Float
# -----------------------------------

"""
float()
--------

The float() function converts a value into a floating point
number when the conversion is valid.
It is used when we want a decimal number.

Example-1:

    "3.14" --> 3.14
"""

num_str = "3.14"
num_float = float(num_str)

print(num_float)          # Output: 3.14
print(type(num_float))    # Output: <class 'float'>


# Example-2: 

percentile = "99.99"

percentile = float(percentile)

print(percentile)
print(type(percentile))


# -----------------------------------
# 4. Convert Integer to String
# -----------------------------------

"""
str()
-----

The str() function converts a value into a string.

Example-1:

    25 --> "25"
"""

num = 25
num_str = str(num) # here, the integer 25 is converted into a string "25"

print(num_str)          # Output: 25
print(type(num_str))    # Output: <class 'str'>


# Example-2: 

age = 19

message = "My age is " + str(age) 

print(message)


# -----------------------------------
# 5. Convert Float to String
# -----------------------------------

# it is also possible to convert a float into a string using str().

percentile = 99.99
percentile_str = str(percentile)

print(percentile_str)
print(type(percentile_str))



# -----------------------------------
# 6. Convert Integer to Float
# -----------------------------------

"""
An integer can easily be converted into a float.

Example:

    10 --> 10.0
"""

num = 10
num_float = float(num)

print(num_float)          # Output: 10.0
print(type(num_float))    # Output: <class 'float'>


# -----------------------------------
# 7. Convert Float to Integer
# -----------------------------------

"""
A float can be converted into an integer using int().

NOTE: 

    int() truncates the decimal part.
    It does NOT round the number.

Example:

    3.14 --> 3
    7.99 --> 7
    -3.14 --> -3
"""

pi = 3.14
pi_int = int(pi)

print(pi_int)          # Output: 3
print(type(pi_int))    # Output: <class 'int'>


number = -7.99

print(int(number))     # Output: -7


# -----------------------------------
# 8. Integer and Float Conversion
# -----------------------------------

integer_value = 10
float_value = 10.5

print(float(integer_value))  # Output: 10.0
print(int(float_value))      # Output: 10


# ----------------------------------------
# 9. Type Conversion Creates a New Value
# ----------------------------------------

"""
Type conversion returns a converted value.

It does not automatically change the original value.

Example:
"""

number = "25"

converted_number = int(number)

print("Original:", number)
print("Type:", type(number))

print("Converted:", converted_number)
print("Type:", type(converted_number))


# -----------------------------------
# 10. Convert Boolean to Integer
# -----------------------------------

"""
Boolean values can also be converted into integers.

NOTE:
    True becomes 1
    False becomes 0
"""

true_value = True
false_value = False

print(int(true_value))       # Output: 1, because the boolean True is converted into an integer 1
print(int(false_value))      # Output: 0, because the boolean False is converted into an integer 0

print(type(int(true_value)))


# -----------------------------------
# 11. Convert Integer to Boolean
# -----------------------------------

"""
When converting integers to Boolean:

NOTE:
    0      --> False
    Any non-zero number --> True
"""

print(bool(0))       # Output: False
print(bool(1))       # Output: True
print(bool(10))      # Output: True
print(bool(-5))      # Output: True


# -----------------------------------
# 12. Convert String to Boolean
# -----------------------------------

"""
When converting strings to Boolean:

    Empty string "" -> False
    Non-empty string -> True

NOTE: One thing that can be confusing:

    bool("False") is True
    because "False" is a non-empty string. 
"""

print(bool(""))          # Output: False
print(bool("Python"))    # Output: True
print(bool("False"))     # Output: True


# -----------------------------------
# 13. Convert Boolean to String
# -----------------------------------

true_value = True
false_value = False

true_string = str(true_value)
false_string = str(false_value)

print(true_string) # Output: True
print(type(true_string)) # Output: <class 'str'>

print(false_string) # Output: False
print(type(false_string)) # Output: <class 'str'>


# -----------------------------------
# 14. Converting Numeric Strings
# -----------------------------------

"""
Strings containing valid numeric values can be converted
into numbers.

Examples:

    "100"    -> int
    "3.14"   -> float
    "-50"    -> int
"""

number1 = "100"
number2 = "3.14"
number3 = "-50"
#number4 = "Arnav" #this is not a valid number string, so it cannot be converted into an integer or float.
# because it does not represent a numeric value.

print(int(number1))
print(float(number2))
print(int(number3))
#print(int(number4)) It will raise a ValueError because "Arnav" is not a valid numeric string.


# -----------------------------------
# 15. Invalid Integer Conversion
# -----------------------------------

"""
Not every string can be converted into an integer.

A string must contain a valid integer representation to be
converted using int().

This works:

    int("100")

This does NOT work:

    int("Arnav")
    int("10.5")

These produce a ValueError.
"""

valid_number = "100"

print(int(valid_number))

# Invalid examples:

# print(int("Arnav"))
# ValueError: invalid literal for int()


# print(int("10.5"))
# ValueError because "10.5" is not an integer string.


# -----------------------------------
# 16. Invalid Float Conversion
# -----------------------------------

"""
float() can convert valid numeric strings into floats.

Example:

    float("10.5") --> 10.5

But invalid text cannot be converted.

Normal text cannot be converted into a number.
"""

valid_float = "10.5"

print(float(valid_float))

# Invalid example:

# print(float("Arnav"))
# ValueError


# --------------------------------------
# 17. Type Conversion with User Input
# --------------------------------------

"""
NOTE: One important thing about input():

The input() function always returns a string.

Therefore, if we want to perform calculations with
numeric input, we usually need type conversion.

Example:

    input() --> string
    int()   --> integer
"""

# Example:

# age = input("Enter your age: ") 
# age = int(age)

# print("Your age is:", age)
# print(type(age))

# NOTE: input() will be covered in detail in:
# 05_Input_and_Output.py

# --------------------------------------
# 18. Direct Type Conversion
# --------------------------------------

"""
We don't always have to use two lines.

Instead of:

    age = input("Enter your age: ")
    age = int(age)

we can directly write:

    age = int(input("Enter your age: "))

This converts the input into an integer immediately.
"""

# Example:

# age = int(input("Enter your age: "))
# print("Age:", age)
# print(type(age))


# --------------------------------------
# 19. Practical Example - Addition
# --------------------------------------

"""
Suppose the user enters:

    10
    20

input() receives both values as strings.

Without conversion:

    "10" + "20" --> "1020"

After conversion:

    10 + 20 --> 30
"""

# Example:

# first_number = input("Enter first number: ")
# second_number = input("Enter second number: ")

# first_number = int(first_number)
# second_number = int(second_number)

# result = first_number + second_number

# print("Result:", result)


# --------------------------------------
# 20. Practical Example - Decimal Input
# --------------------------------------

# float() should be used when the user may enter decimal values. 

# price = float(input("Enter price: "))
# quantity = int(input("Enter quantity: "))

# total = price * quantity

# print("Total:", total)






# ---------------------------------------
# Summary
# ---------------------------------------

"""
Type Conversion Summary
-----------------------

Type conversion changes a value from one data type
to another.

Implicit Conversion
    Python automatically converts a value from one
    data type to another when needed.

Explicit Conversion
    The programmer manually converts a value using
    functions such as:

        int()
        float()
        str()
        bool()

Common conversions:

    int()    -> Convert a value to an integer
    float()  -> Convert a value to a float
    str()    -> Convert a value to a string
    bool()   -> Convert a value to a Boolean

Important points:

    - int() removes the decimal part when converting
      a float to an integer. It does not round.

    - 0 converts to False, while non-zero numbers
      convert to True.

    - An empty string "" converts to False.
      A non-empty string converts to True.

    - Invalid numeric conversions can raise ValueError.

    - input() returns a string, so numeric input often
      needs to be converted before calculations.

Examples:

    int("10")      -> 10
    float("10.5")  -> 10.5
    str(100)       -> "100"
    bool(1)        -> True
"""




# -----------------------------
# End of Type Conversion
# -----------------------------

print("\nType Conversion topic completed!")