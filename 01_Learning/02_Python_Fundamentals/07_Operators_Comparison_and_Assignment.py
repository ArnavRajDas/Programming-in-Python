# ============================================================
# Python Fundamentals - Comparison and Assignment Operators
# ============================================================

"""
Comparison and Assignment Operators in Python
----------------------------------------------

In this file, we will learn about:

    1. Comparison Operators
    2. Assignment Operators

Comparison Operators are used to compare two values.

Assignment Operators are used to assign a value to a
variable or update the value of an existing variable.
"""


# ----------------------------------------------
# PART 1 - COMPARISON OPERATORS
# ----------------------------------------------

"""
Comparison Operators
--------------------

Comparison operators compare two values.

The result of a comparison is always a Boolean value:

    True
    False

Python provides six main comparison operators:

    ==   Equal to
    !=   Not equal to
    >    Greater than
    <    Less than
    >=   Greater than or equal to
    <=   Less than or equal to
"""


# -------------------------
# 1. Equal To (==)
# -------------------------

"""
The '==' operator checks whether two values are equal.

It returns:

    True  --> if both values are equal
    False --> if they are different
"""

a = 10
b = 10

print("a == b:", a == b)


# Another example

x = 10
y = 20

print("x == y:", x == y)


# IMPORTANT:
#
# '==' is used for comparison.
# '=' is used for assignment.

# Example:

number = 10       # Assignment
print(number == 10)  # Comparison


# -------------------------
# 2. Not Equal To (!=)
# -------------------------

"""
The '!=' operator checks whether two values are different.

It returns:

    True  --> if the values are different
    False --> if the values are equal
"""

a = 10
b = 20

print("a != b:", a != b)


a = 10
b = 10

print("a != b:", a != b)


# -------------------------
# 3. Greater Than (>)
# -------------------------

"""
The '>' operator checks whether the left value is greater
than the right value.
"""

a = 20
b = 10

print("a > b:", a > b)

print("10 > 20:", 10 > 20)


# -------------------------
# 4. Less Than (<)
# -------------------------

"""
The '<' operator checks whether the left value is less
than the right value.
"""

a = 10
b = 20

print("a < b:", a < b)

print("20 < 10:", 20 < 10)


# ----------------------------------
# 5. Greater Than or Equal To (>=)
# ----------------------------------

"""
The '>=' operator checks whether the left value is:

    - Greater than the right value
    OR
    - Equal to the right value
"""

print("20 >= 10:", 20 >= 10)
print("20 >= 20:", 20 >= 20)
print("10 >= 20:", 10 >= 20)


# ----------------------------------
# 6. Less Than or Equal To (<=)
# ----------------------------------

"""
The '<=' operator checks whether the left value is:

    - Less than the right value
    OR
    - Equal to the right value
"""

print("10 <= 20:", 10 <= 20)
print("20 <= 20:", 20 <= 20)
print("30 <= 20:", 30 <= 20)


# ------------------------------------------------
# 7. Comparison Operators Return Boolean Values
# ------------------------------------------------

"""
Comparison expressions produce Boolean values.

The result is either:

    True
    False
"""

age = 19

print(age >= 18)
print(age < 18)

print(type(age >= 18))


# ------------------------------------------------
# 8. Comparison Operators with Variables
# ------------------------------------------------



marks = 85
passing_marks = 40

print("Marks == Passing Marks:", marks == passing_marks)
print("Marks != Passing Marks:", marks != passing_marks)
print("Marks > Passing Marks:", marks > passing_marks)
print("Marks < Passing Marks:", marks < passing_marks)
print("Marks >= Passing Marks:", marks >= passing_marks)
print("Marks <= Passing Marks:", marks <= passing_marks)



# ------------------------------------------------
# 9. Chained Comparison Operators
# ------------------------------------------------

"""
Python allows multiple comparisons to be chained together.

Example:

    10 < 20 < 30

This is equivalent to:

    10 < 20 and 20 < 30

Chained comparisons are useful when checking whether
a value lies within a range.
"""

age = 19

print("18 <= age <= 25:", 18 <= age <= 25)


# ------------------------------------------------
# 10. Comparison Operators with Strings
# ------------------------------------------------

"""
Comparison operators can also be used with strings.

For equality comparisons, Python checks whether the strings
contain the same sequence of characters.

For ordering comparisons such as < and >, Python compares
strings lexicographically based on the Unicode values of
their characters.
"""

name1 = "Arnav"
name2 = "Arnav"
name3 = "Python"

print("name1 == name2:", name1 == name2)
print("name1 == name3:", name1 == name3)
print("name1 != name3:", name1 != name3)

# String ordering comparison

print('"apple" < "banana":', "apple" < "banana")
print('"Python" > "Java":', "Python" > "Java")


# ----------------------------------------
# 11. Comparison Operators Summary
# ----------------------------------------

"""
Operator    Meaning

    ==      Equal to
    !=      Not equal to
    >       Greater than
    <       Less than
    >=      Greater than or equal to
    <=      Less than or equal to
"""


# ----------------------------------------
# PART 2 - ASSIGNMENT OPERATORS
# ----------------------------------------

"""
Assignment Operators
--------------------

Assignment operators are used to assign values to variables
or update the existing value of a variable.

Basic assignment:

    =

Augmented assignment operators:

    +=
    -=
    *=
    /=
    %=
    **=
    //=
"""


# ----------------------------------------
# 12. Assignment Operator (=)
# ----------------------------------------

"""
The '=' operator assigns a value to a variable.

Example:

    a = 33

This means the value 33 is assigned to the variable 'a'.
"""

a = 33

print("a =", a)



# ----------------------------------------
# 13. Multiple Assignment
# ----------------------------------------

"""
Python allows multiple variables to be assigned
in a single statement.

Example:

    x, y, z = 10, 20, 30

This assigns:

    x = 10
    y = 20
    z = 30
"""

x, y, z = 10, 20, 30

print("x:", x)
print("y:", y)
print("z:", z)


# ----------------------------------------
# 14. Addition Assignment (+=)
# ----------------------------------------

"""
The '+=' operator adds a value to a variable and stores
the updated result in the same variable.

    a += 3

is equivalent to:

    a = a + 3
"""

a = 33

a += 3

print("a after += 3:", a)


# += with Strings

"""
The '+=' operator can also be used with strings.

It adds another string to the existing string.

    message += " Python"

is equivalent to:

    message = message + " Python"
"""

message = "Hello"

message += " Python"

print("String after +=:", message)


# ----------------------------------------
# 15. Subtraction Assignment (-=)
# ----------------------------------------

"""
The '-=' operator subtracts a value from a variable and
stores the updated result.

    a -= 3

is equivalent to:

    a = a - 3
"""

a = 33

a -= 3

print("a after -= 3:", a)


# ----------------------------------------
# 16. Multiplication Assignment (*=)
# ----------------------------------------

"""
The '*=' operator multiplies a variable by a value and
stores the updated result.

    a *= 3

is equivalent to:

    a = a * 3
"""

a = 33

a *= 3

print("a after *= 3:", a)



# -----------------------------------
# 17. Division Assignment (/=)
# -----------------------------------

"""
The '/=' operator divides a variable by a value and stores
the result back in the variable.

    a /= 3

is equivalent to:

    a = a / 3

The result is a float.
"""

a = 33

a /= 3

print("a after /= 3:", a)
print("Type:", type(a))


# -----------------------------------
# 18. Modulus Assignment (%=)
# -----------------------------------

"""
The '%=' operator finds the remainder and assigns the result
back to the variable.

    a %= 3

is equivalent to:

    a = a % 3
"""

a = 33

a %= 3

print("a after %= 3:", a)


# -------------------------------------
# 19. Exponentiation Assignment (**=)
# -------------------------------------

"""
The '**=' operator raises a variable to a power and assigns
the result back to the variable.

    a **= 3

is equivalent to:

    a = a ** 3
"""

a = 3

a **= 3

print("a after **= 3:", a)


# -------------------------------------
# 20. Floor Division Assignment (//=)
# -------------------------------------

"""
The '//=' operator performs floor division and assigns
the result back to the variable.

    a //= 3

is equivalent to:

    a = a // 3
"""

a = 33

a //= 3

print("a after //= 3:", a)


# ------------------------------------------------
# 21. All Assignment Operators Together
# ------------------------------------------------

"""
The following examples demonstrate all augmented
assignment operators independently.
"""

a = 20
a += 5
print("After += 5:", a)

a = 20
a -= 3
print("After -= 3:", a)

a = 20
a *= 2
print("After *= 2:", a)

a = 20
a /= 2
print("After /= 2:", a)

a = 20
a %= 6
print("After %= 6:", a)

a = 20
a **= 2
print("After **= 2:", a)

a = 20
a //= 3
print("After //= 3:", a)



# ------------------------------------------------
# 22. Assignment Operators with Different Values
# ------------------------------------------------

"""
Assignment operators can be used with variables containing
different numeric values.
"""

balance = 1000

balance += 500
print("After adding:", balance)

balance -= 200
print("After subtracting:", balance)

balance *= 2
print("After multiplying:", balance)

balance /= 2
print("After dividing:", balance)


# ---------------------------------------
# 23. Comparison + Assignment Together
# ---------------------------------------

"""
Comparison and assignment operators often work together
in programs.

Example:

    Store a value
        ↓
    Compare the value
        ↓
    Get True or False
"""

score = 75

passed = score >= 40

print("Score:", score)
print("Passed:", passed)


# ---------------------------------------
# 24. Common Mistake: = vs ==
# ---------------------------------------

"""
A very common beginner mistake is confusing:

    =

with:

    ==

Remember:

    =   --> Assignment
    ==  --> Comparison

Example:

    age = 19

means:

    Assign 19 to age.

While:

    age == 19

means:

    Check whether age is equal to 19.
"""

age = 19

print("Age:", age)
print("Is age equal to 19?", age == 19)




# ------------------------------------------
# 25. Important: == vs is
# ------------------------------------------

"""
'==' and 'is' are different operators.

'==' checks whether two values are equal.

'is' checks whether two variables refer to
the same object in memory.

Example:
"""

a = [1, 2, 3]
b = [1, 2, 3]

print("a == b:", a == b)  # True - same values
print("a is b:", a is b)  # False - different objects

# Both variables refer to the same object

c = a

print("a == c:", a == c)  # True
print("a is c:", a is c)  # True


# NOTE:

"""
Use '==' when comparing values.

Use 'is' mainly when checking object identity,
especially with 'None'.

Example:
"""

value = None

print("Is value None?", value is None)


# ------------------------------------------
# 26. Practical Example - Updating a Score
# ------------------------------------------

score = 50

print("Initial score:", score)

score += 10

print("Updated score:", score)

print("Passed:", score >= 40)



# --------------------------------------------
# Practice Challenge
# --------------------------------------------

"""
Practice Challenge
------------------

Try solving these problems without looking at
the solutions above.

1. Create two variables and check whether they are equal.

2. Create a variable called age and check whether
   it is between 18 and 25 using a chained comparison.

3. Create a variable called score with a value of 50.
   Increase it by 10 using +=.

4. Check whether the updated score is greater than
   or equal to 40.

5. Create three variables in a single assignment
   statement and print their values.
"""



"""
--------------
Key Points
--------------

Comparison Operators:

    ==   Equal to
    !=   Not equal to
    >    Greater than
    <    Less than
    >=   Greater than or equal to
    <=   Less than or equal to

Comparison expressions return:

    True
    False

Python also supports chained comparisons:

    18 <= age <= 25


Assignment Operators:

    =    Assignment
    +=   Addition assignment
    -=   Subtraction assignment
    *=   Multiplication assignment
    /=   Division assignment
    %=   Modulus assignment
    **=  Exponentiation assignment
    //=  Floor division assignment


Important:

    =    --> Assignment
    ==   --> Comparison

Augmented assignment such as:

    a += 5

is a shorter way of writing:

    a = a + 5
"""

# --------------------------------------------
# End of Comparison and Assignment Operators
# --------------------------------------------

print("\nComparison and Assignment Operators topic completed!")