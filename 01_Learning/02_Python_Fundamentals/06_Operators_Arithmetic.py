# ===============================================
# Python Fundamentals - Arithmetic Operators
# ===============================================

"""
Arithmetic Operators in Python
---------------------------------

Arithmetic operators are used to perform mathematical
calculations on numeric values.

Python provides the following commonly used arithmetic operators:

    +   Addition / Unary Plus
    -   Subtraction / Unary Minus
    *   Multiplication
    /   Division
    %   Modulus
    **  Exponentiation
    //  Floor Division
"""


# --------------------
# 1. Addition (+)
# --------------------

"""
The '+' operator adds two values.

Example:

    34 + 5 = 39
"""

a = 34
b = 5

result = a + b

print("a + b =", result)


# More examples

print(10 + 20)
print(-5 + 10)
print(2.5 + 3.5)


# --------------------
# 2. Subtraction (-)
# --------------------

"""
The '-' operator subtracts the second value from the first.

Example:

    34 - 5 = 29
"""

result = a - b

print("a - b =", result)


# More examples

print(20 - 8)
print(5 - 10)
print(10.5 - 2.5)



# -------------------------
# 3. Unary Plus and Minus
# -------------------------

"""
Unary '+' and '-' are used with a single value.

Unary '+' returns the value as it is.

Unary '-' changes the sign of the value.

Examples:

    +10 = 10
    -10 = -10
"""

number = 10

print("+number =", +number)
print("-number =", -number)

negative_number = -25

print("+negative_number =", +negative_number)
print("-negative_number =", -negative_number)



# -------------------------
# 4. Multiplication (*)
# -------------------------

"""
The '*' operator multiplies two values.

Example:

    34 * 5 = 170
"""

result = a * b

print("a * b =", result)


# More examples

print(5 * 4)
print(-3 * 6)
print(2.5 * 4)


# -------------------------
# 5. Division (/)
# -------------------------

"""
The '/' operator performs division.

Important:

The result of '/' is always a float, even when the
division produces a whole number.

Example:

    34 / 5 = 6.8
    10 / 2 = 5.0
"""

result = a / b

print("a / b =", result)
print("Type:", type(result))


# More examples

print(10 / 2)
print(7 / 2)
print(20 / 5)


# -------------------------
# 6. Modulus (%)
# -------------------------

"""
The '%' operator returns the remainder of a division.

Example:

    34 % 5 = 4

Because:

    34 = (5 × 6) + 4

So the remainder is 4.
"""

result = a % b

print("a % b =", result)


# More examples

print(10 % 3)
print(15 % 5)
print(7 % 2)


# Practical example:

# Check the remainder after dividing a number by 2.

number = 17

print("Remainder:", number % 2)


# -------------------------
# 7. Exponentiation (**)
# -------------------------

"""
The '**' operator is used for exponentiation.

It raises the first number to the power of the second number.

Example:

    2 ** 3 = 8

This means:

    2 × 2 × 2 = 8
"""

result = a ** b

print("a ** b =", result)


# More examples

print(2 ** 3)
print(5 ** 2)
print(10 ** 3)


# -------------------------
# 8. Floor Division (//)
# -------------------------

"""
The '//' operator performs floor division.

It divides two numbers and returns the floor of the result,
which means the greatest integer less than or equal to the result.

Example:

    34 / 5 = 6.8

    34 // 5 = 6
"""

result = a // b

print("a // b =", result)


# More examples

print(10 // 3)
print(20 // 4)
print(7 // 2)


# IMPORTANT:
#
# Floor division is not simply "remove everything after
# the decimal point".
#
# It returns the floor value, which means it rounds
# toward negative infinity.

print(7 / 2)        # 3.5
print(7 // 2)       # 3

print(-7 / 2)       # -3.5
print(-7 // 2)      # -4




# -----------------------------------------
# 9. Arithmetic Operators with Floats
# -----------------------------------------

"""
Arithmetic operations can also be performed on floating point
numbers.
"""

price = 99.50
quantity = 3

total = price * quantity

print("Price:", price)
print("Quantity:", quantity)
print("Total:", total)


# ------------------------------------------------
# 10. Order of Operations - Basic Introduction
# ------------------------------------------------

"""
When multiple arithmetic operators appear in one expression,
Python follows an order of operations.

Example:

    10 + 5 * 2

Multiplication is performed before addition:

    10 + (5 * 2)
    10 + 10
    20

Detailed operator precedence will be covered in:

    11_Operator_Precedence.py
"""

result = 10 + 5 * 2

print("Result:", result)  # 20


# Parentheses can be used to control the order:

result = (10 + 5) * 2

print("Result with parentheses:", result)  # 30 


# ------------------------------------------------
# 11. Arithmetic Operators with Negative Numbers
# ------------------------------------------------

"""
Arithmetic operators also work with negative numbers.
"""

a = -10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Python satisfies the relationship:
#
# a = (a // b) * b + (a % b)
#
# For example:
#
# -10 = (-4 * 3) + 2

print("Modulus:", a % b)            # 2
print("Floor Division:", a // b)   # -4



# -----------------------
# 12. Division by Zero
# -----------------------

"""
Division by zero is not allowed.

The following operations raise ZeroDivisionError:

    10 / 0
    10 // 0
    10 % 0

Example:

    print(10 / 0)

This would raise:

    ZeroDivisionError

The examples are commented out so the program can continue
running.
"""

# print(10 / 0)
# print(10 // 0)
# print(10 % 0)


# ------------------------------------------------
# 13. Arithmetic Operators with User Input
# ------------------------------------------------

"""
Arithmetic operators can be combined with user input.

Remember:

    input() returns a string.

Therefore, numeric input needs to be converted before
performing arithmetic operations.

Example:

    The following example converts the input strings
    to integers before performing addition.
"""

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print("Sum:", a + b)


"""
This example requires user input, so it is commented out
to keep the file fully runnable without interaction.

The same concept is covered in:

    05_Input_and_Output.py
"""


# ------------------------------------------------
# 14. Practical Example - Simple Calculation
# ------------------------------------------------

"""
Calculate the total price of multiple products.
"""

price = 50
quantity = 4

total = price * quantity

print("Price:", price)
print("Quantity:", quantity)
print("Total:", total)


# ------------------------------------------------
# 15. Practical Example - Remaining Items
# ------------------------------------------------

"""
The modulus operator can be used to find how many items
remain after dividing them into equal groups.

Example:

    17 items
    5 items per group

17 % 5 = 2

So 2 items remain.
"""

items = 17
group_size = 5

remaining_items = items % group_size

print("Remaining items:", remaining_items)


# ------------------------------------------------
# 16. Practical Example - Power
# ------------------------------------------------

"""
The exponentiation operator can be used to calculate powers.
"""

base = 2
power = 5

result = base ** power

print("Result:", result)


# ------------------------------------------------
# 17. Practical Example - Quotient and Remainder
# ------------------------------------------------

"""
Floor division and modulus can be used together to find:

    Quotient
    Remainder

Example:

    17 divided by 5

    17 = (5 × 3) + 2

Quotient  = 3
Remainder = 2
"""

number = 17
divisor = 5

quotient = number // divisor
remainder = number % divisor

print("Quotient:", quotient)
print("Remainder:", remainder)


# ---------------------------------
# 18. Arithmetic Operator Summary
# ---------------------------------

"""
+   --> Addition / Unary Plus
      Addition Example: 10 + 3 = 13
      Unary Example: +10 = 10


-   --> Subtraction / Unary Minus
      Subtraction Example: 10 - 3 = 7
      Unary Example: -10 = -10

      
*   --> Multiplication
      Example: 10 * 3 = 30

      
/   --> Division
      Example: 10 / 3 = 3.333...

      
%   --> Modulus (remainder)
      Example: 10 % 3 = 1

      
**  --> Exponentiation
      Example: 10 ** 3 = 1000

      
//  --> Floor Division
      Example: 10 // 3 = 3
"""



# -----------------
# Key Points
# -----------------

"""
Remember:

1. '+' is used for addition and can also be used as unary plus.


2. '-' is used for subtraction and can also be used as unary minus.


3. '*' is used for multiplication.


4. '/' performs division and returns a float.


5. '%' returns the remainder of a division.


6. '**' performs exponentiation.


7. '//' performs floor division.


8. Floor division returns the floor of the result.
   It is NOT simply truncation toward zero.

   
9. Division, floor division, and modulus by zero
   raise ZeroDivisionError.

   
10. Parentheses can be used to control the order
    of arithmetic operations.

    
11. Detailed operator precedence will be covered in:

        11_Operator_Precedence.py
"""


# --------------------------------
# End of Arithmetic Operators
# --------------------------------

print("\nArithmetic Operators topic completed!")