# ============================================================
# Python Fundamentals - Identity and Membership Operators
# ============================================================

"""
Identity and Membership Operators in Python
--------------------------------------------

In this file, we will learn about:

    1. Identity Operators
       - is
       - is not

    2. Membership Operators
       - in
       - not in

Identity operators are used to check whether two variables
refer to the same object.

Membership operators are used to check whether a value
exists inside a collection or sequence.

The result of these operators is generally a Boolean value:

    True
    False
"""


# -------------------------------
# PART 1 - IDENTITY OPERATORS
# -------------------------------

"""
Identity Operators
------------------

Python provides two identity operators:

    is
    is not

Identity operators check whether two variables refer to
the SAME OBJECT in memory.

They do NOT simply check whether two values are equal.

Example:

    a is b

means:

    "Do a and b refer to the same object?"
"""


# ----------------------
# 1. 'is' Operator
# ----------------------

"""
The 'is' operator returns True when two variables refer
to the same object.

Example:

    a = [1, 2, 3]
    b = a

Here, both a and b refer to the same list object.
"""

a = [1, 2, 3]
b = a

print("a:", a)
print("b:", b)

print("a is b:", a is b)


# ----------------------
# 2. 'is' vs '=='
# ----------------------

"""
This is one of the most important differences to understand.

'==' checks whether two objects have equal values.

'is' checks whether two variables refer to the same object.

Example:

    a = [1, 2, 3]
    b = [1, 2, 3]

The values are equal:

    a == b --> True

But they are separate list objects:

    a is b --> False , because they are two different objects in memory.
"""

a = [1, 2, 3]
b = [1, 2, 3]

print("a == b:", a == b)
print("a is b:", a is b)


# ---------------------------------------------
# 3. Shared References and Object Modification
# ---------------------------------------------

"""
When we assign:

    b = a

Python does not create a new list.

Both variables refer to the SAME list object.

Therefore, modifying the list through one variable
is visible through the other variable.
"""

a = [10, 20, 30]
b = a

print("a is b:", a is b)

a.append(40)

print("a:", a)
print("b:", b)
 


# ----------------------
# 4. 'is not' Operator
# ----------------------

"""
The 'is not' operator returns True when two operands
do not refer to the same object.

It returns:

    True  --> if the operands refer to different objects
    False --> if the operands refer to the same object
"""

a = [1, 2, 3]
b = [1, 2, 3]

print("a is not b:", a is not b)


# Same object:

c = a

print("a is not c:", a is not c)


# ------------------------------------
# 5. Identity Operator Truth Table
# ------------------------------------

"""
Identity Operators:

    is

        Same object      --> True
        Different object --> False


    is not

        Same object      --> False
        Different object --> True
"""


# --------------------------
# 6. Identity with None
# ---------------------------

"""
The 'is' operator is commonly used when checking for None.

Example:

    value is None

This checks whether the variable refers to the special
singleton object None.

This is the preferred way to check for None.
"""

value = None

print("value is None:", value is None)


value = 100

print("value is None:", value is None)


# --------------------------
# 7. 'is not None'
# --------------------------

"""
'is not None' checks whether a value is not None.
"""

value = "Python"

print("value is not None:", value is not None)


value = None

print("value is not None:", value is not None)


# ----------------------------------
# 8. Important Warning About 'is'
# ----------------------------------

"""
Do NOT normally use 'is' to compare ordinary values.

For example:

    a == b

should generally be used when you want to know whether
the values are equal.

Use:

    a is b

when you specifically want to know whether they are
the same object.

Correct:

    name == "Arnav"

Correct:

    value is None
"""

'''IMPORTANT NOTE:

Do not use 'is' to compare ordinary values such as
numbers or strings.

Some immutable objects may be reused by Python, so
'is' can sometimes appear to return True for equal
values. This is an implementation detail and should
not be relied upon.

Use '==' for value comparison.
Use 'is' for object identity.
'''


# ----------------------------------
# PART 2 - MEMBERSHIP OPERATORS
# ----------------------------------

"""
Membership Operators
--------------------

Python provides two membership operators:

    in
    not in

Membership operators check whether a value exists inside
a sequence or collection.

They return:

    True
    False
"""


# ----------------------------------
# 9. 'in' and 'not in' with Strings
# ----------------------------------

# 'in'
"""
The 'in' operator checks whether a sequence of characters
exists inside a string.
"""

text = "Code With Arnav"

print("'Code' in text:", "Code" in text)
print("'Arnav' in text:", "arnav" in text)  # because of case sensitivity, this will return False
print("'Arnav' in text:", "Arnav" in text)


# 'not in'
"""
The 'not in' operator checks whether a value does NOT
exist inside a sequence.
"""

text = "Python Programming"

print("'Java' not in text:", "Java" not in text)
print("'Python' not in text:", "Python" not in text)





# ------------------------------------
# 10. Membership Operators with Lists
# ------------------------------------

"""
The 'in' operator can check whether an item exists
inside a list.
"""

numbers = [10, 20, 30, 40, 50]

print("20 in numbers:", 20 in numbers)
print("100 in numbers:", 100 in numbers)

print("20 not in numbers:", 20 not in numbers)
print("100 not in numbers:", 100 not in numbers)


# ---------------------------------------
# 11. Membership Operators with Tuples
# ------------------------------------

"""
Membership operators also work with tuples.
"""

colors = ("red", "green", "blue")

print("'red' in colors:", "red" in colors)
print("'yellow' in colors:", "yellow" in colors)

print("'red' not in colors:", "red" not in colors)
print("'yellow' not in colors:", "yellow" not in colors)


# ------------------------------------
# 12. Membership Operators with Sets
# ------------------------------------

"""
Membership checking is also supported by sets.

Sets are commonly useful for membership testing because
membership checks are generally very fast.
"""

numbers = {10, 20, 30, 40}

print("20 in numbers:", 20 in numbers)
print("100 in numbers:", 100 in numbers)
print("20 not in numbers:", 20 not in numbers)
print("100 not in numbers:", 100 not in numbers)


# -------------------------------------------
# 13. Membership Operators with Dictionaries
# -------------------------------------------

"""
For dictionaries, the 'in' and 'not in' operators check
the KEYS by default.

Example:

    "name" in student

checks whether "name" is a key in the dictionary.

It does NOT search the values by default.
"""

student = {
    "name": "Arnav",
    "age": 19,
    "language": "Python"
}

print("'name' in student:", "name" in student)
print("'age' in student:", "age" in student)
print("'Arnav' in student:", "Arnav" in student) # gives False because 'in' operator checks for keys in dictionary, not values

print("'name' not in student:", "name" not in student)
print("'city' not in student:", "city" not in student)


# ------------------------------------
# 14. Checking Dictionary Values
# ------------------------------------

"""
If you want to check whether a value exists in a dictionary,
you can use the values() method.

Example:

    value in dictionary.values()
"""

student = {
    "name": "Arnav",
    "age": 19
}

print("'Arnav' in values:", "Arnav" in student.values())
print("19 in values:", 19 in student.values())


# ------------------------------------
# 15. Checking Dictionary Keys
# ------------------------------------

"""
Dictionary membership checks keys by default.

The preferred and simplest form is:

    key in dictionary

You can also write:

    key in dictionary.keys()

but calling keys() is usually unnecessary when
you only want to check whether a key exists.
"""

student = {
    "name": "Arnav",
    "age": 19
}

print("'name' in student:", "name" in student)
print("'city' in student:", "city" in student)

# Explicitly using keys() also works, but is usually unnecessary.
print("'name' in student.keys():", "name" in student.keys())

print("'name' not in student:", "name" not in student)
print("'city' not in student:", "city" not in student)


# --------------------------------------
# 16. Membership Operators with Ranges
# --------------------------------------

"""
Membership operators can also be used with range objects.

This is useful when checking whether a number belongs
to a particular range.
"""

numbers = range(1, 11)

print("5 in range:", 5 in numbers)
print("15 in range:", 15 in numbers)

# Membership also respects the step value.

even_numbers = range(2, 11, 2)

print("6 in even_numbers:", 6 in even_numbers)
print("7 in even_numbers:", 7 in even_numbers)


# -----------------------------------------
# 17. Membership Operators with User Input
# -----------------------------------------

"""
Membership operators can be combined with user input.

Since input() returns a string, membership checking can
be performed directly on the entered text.
"""

# name = input("Enter your name: ")

# if "a" in name:
#     print("The letter 'a' is present.")


# ---------------------------------------------
# 18. Practical Example - Checking a Character
# ---------------------------------------------

text = "Python"

print("Is 'P' present?", "P" in text)
print("Is 'z' present?", "z" in text)




# ---------------------------------------------
# 19. Practical Example - Checking Permissions
# ---------------------------------------------

permissions = ["read", "write", "execute"]

required_permission = "write"

print(
    "Permission available:",
    required_permission in permissions
)


# ------------------------------------------------
# 20. Combining Membership and Logical Operators
# ------------------------------------------------

"""
Membership operators can be combined with logical operators.

Example:

A user can access the system if they have either:

    "admin"
    OR
    "moderator"
"""

roles = ["user", "moderator"]

can_manage = "admin" in roles or "moderator" in roles

print("Can manage:", can_manage)


# ---------------------------------------------
# 21. Combining Membership with Comparison
# ---------------------------------------------

"""
Membership checks can also be combined with comparison
operators.
"""

numbers = [10, 20, 30]

number = 20

is_valid = number in numbers and number > 10

print("Number is valid:", is_valid)




# ----------------------------
# 22. Identity vs Membership
# ----------------------------

"""
Identity and membership answer completely different questions.

Identity:

    a is b

asks:

    "Are a and b the same object?"

Membership:

    x in collection

asks:

    "Does x exist inside this collection?"
"""

a = [1, 2, 3]
b = a

print("Identity:", a is b)

numbers = [10, 20, 30]

print("Membership:", 20 in numbers)



# -----------------------
# 23. Important Notes
# -----------------------

"""
Important Notes
---------------

IDENTITY OPERATORS:

1. Python has two identity operators:

       is
       is not

2. 'is' checks whether two variables refer to the same
   object.

3. 'is not' returns True when two operands do not refer
    to the same object.

4. '==' checks value equality, while 'is' checks object
   identity.

5. Use 'is None' and 'is not None' when checking for None.


MEMBERSHIP OPERATORS:

6. Python has two membership operators:

       in
       not in

7. 'in' checks whether a value exists inside a sequence
   or collection.

8. 'not in' checks whether a value does not exist inside
   a sequence or collection.

9. Membership operators can be used with strings, lists,
   tuples, sets, dictionaries, and ranges.

10. For dictionaries, 'in' checks keys by default.

11. To check dictionary values, use:

        value in dictionary.values()


IMPORTANT DIFFERENCE:

    ==  --> Compare values
    is  --> Compare object identity
    in  --> Check membership
"""




# ---------------
# Key Points
# ---------------

"""
Remember:

    ==

        Compares values.

    is

        Compares object identity.

    is not

        Returns True when two operands do not refer
        to the same object.

    in

        Checks whether a value exists inside
        a sequence or collection.

    not in

        Checks whether a value does not exist
        inside a sequence or collection.


Simple way to remember:

    ==      --> "Are the values equal?"
    is      --> "Are they the same object?"
    in      --> "Is this value inside?"
    not in  --> "Is this value NOT inside?"
"""



# ------------------------------------------
# End of Identity and Membership Operators
# ------------------------------------------
