# ============================================================
# Python Fundamentals - Logical Operators
# ============================================================

"""
Logical Operators in Python
---------------------------

Logical operators are used to combine conditions and
control logical flow in Python.

Python provides three logical operators:

    and
    or
    not

When used with Boolean expressions, they are commonly
used to produce True or False results.

Important:
    In Python, 'and' and 'or' return one of their operands,
    not necessarily a Boolean value.
"""


# --------------------------
# 1. Boolean Values
# --------------------------

"""
Before learning logical operators, remember that Boolean
values can have only two possible values:

    True
    False
"""

is_arnav_good = True
is_arnav_naughty = False

print("Is Arnav good:", is_arnav_good)
print("Is Arnav naughty:", is_arnav_naughty)

# ------------------
# 2. AND Operator
# ------------------

"""
When used with Boolean values, the 'and' operator returns
True only when BOTH operands are True..

Truth Table:

    True  and True  -> True
    True  and False -> False
    False and True  -> False
    False and False -> False
"""

print("\nAND Operator")

print(True and True)
print(True and False)
print(False and True)
print(False and False)


# ----------------------------------
# 3. AND Operator with Variables
# ----------------------------------

a = True
b = True

print("a and b:", a and b)

a = True
b = False

print("a and b:", a and b)

a = False
b = True

print("a and b:", a and b)

a = False
b = False

print("a and b:", a and b)


# -----------------
# 4. OR Operator
# -----------------

"""
When used with Boolean values, the 'or' operator returns
True when AT LEAST ONE operand is True.

It returns False only when BOTH operands are False..

Truth Table:

    True  or True  -> True
    True  or False -> True
    False or True  -> True
    False or False -> False
"""

print("\nOR Operator")

print(True or True)
print(True or False)
print(False or True)
print(False or False)


# ----------------------------------
# 5. OR Operator with Variables
# ----------------------------------

a = True
b = False

print("a or b:", a or b)

a = False
b = False

print("a or b:", a or b)


# -------------------
# 6. NOT Operator
# -------------------

"""
The 'not' operator reverses a Boolean value.

    not True  -> False
    not False -> True
"""

print("\nNOT Operator")

print("not True:", not True)
print("not False:", not False)


# ----------------------------------
# 7. NOT Operator with Variables
# ----------------------------------

is_logged_in = True

print("Is logged in:", is_logged_in)
print("Is NOT logged in:", not is_logged_in)


is_completed = False

print("Is completed:", is_completed)
print("Is NOT completed:", not is_completed)


# -------------------------------------------------
# 8. Logical Operators with Comparison Operators
# -------------------------------------------------

"""
Logical operators are commonly used together with
comparison operators.

Comparison expressions produce Boolean values.

Example:

    age >= 18
    age <= 60

Both expressions produce True or False.

Logical operators can then combine those results.
"""

age = 25

print("Age >= 18:", age >= 18)
print("Age <= 60:", age <= 60)

print("Age is between 18 and 60:",
      age >= 18 and age <= 60)


# ------------------------------------
# 9. AND with Comparison Expressions
# ------------------------------------

"""
Example:

A student passes when:

    marks >= 40
    AND
    attendance >= 75
"""

marks = 80
attendance = 85

passed = marks >= 40 and attendance >= 75

print("Passed:", passed)


# Another example

marks = 80
attendance = 60

passed = marks >= 40 and attendance >= 75

print("Passed:", passed)


# -------------------------------------
# 10. OR with Comparison Expressions
# -------------------------------------

"""
Example:

A student is eligible if:

    marks >= 90
    OR
    attendance >= 95
"""

marks = 92
attendance = 80

eligible = marks >= 90 or attendance >= 95

print("Eligible:", eligible)


# Another example

marks = 75
attendance = 96

eligible = marks >= 90 or attendance >= 95

print("Eligible:", eligible)


# -------------------------------------
# 11. NOT with Comparison Expressions
# -------------------------------------

"""
The 'not' operator can reverse the result of a comparison.
"""

age = 15

print("Age < 18:", age < 18)
print("NOT (Age < 18):", not (age < 18))


# -------------------------------------
# 12. Combining Multiple Conditions
# -------------------------------------

"""
Multiple logical operators can be used to combine
several conditions.

Example:

A person can enter when:

    age >= 18
    AND
    has_id is truthy
"""

age = 20
has_id = True

can_enter = age >= 18 and has_id

print("Can enter:", can_enter)


# ---------------------------------------
# 13. Using OR with Multiple Conditions
# ---------------------------------------

"""
Example:

A user can access a system if they are:

    - An admin
    OR
    - A moderator
"""

is_admin = False
is_moderator = True

can_access = is_admin or is_moderator

print("Can access:", can_access)


"""
Example:
A user can access a feature if they are:

    - An admin
    OR
    - A verified user
"""

is_admin = False
is_verified = True

has_access = is_admin or is_verified

print("Has access:", has_access)



# ----------------------------
# 14. Combining AND and OR
# ----------------------------

"""
Multiple logical operators can be combined in one expression.

Example:

A student is eligible if:

    marks >= 80 AND attendance >= 75

OR

    marks >= 90
"""

marks = 85
attendance = 80

eligible = (marks >= 80 and attendance >= 75) or marks >= 90

print("Eligible:", eligible)


# --------------------------
# 15. Using Parentheses
# --------------------------

"""
Parentheses can be used to make a logical expression
clearer and to explicitly control the order of evaluation.

Example:

    (A and B) or C
"""

a = True
b = False
c = True

result = (a and b) or c

print("Result:", result)


# -------------------------------------
# 16. Logical Operator Precedence
# -------------------------------------

"""
When multiple logical operators are used together,
Python follows this order:

    1. not
    2. and
    3. or

Example:

    True or False and False

First:

    False and False -> False

Then:

    True or False -> True
"""

result = True or False and False

print("Result:", result)


# Parentheses can make the order explicit:

result = True or (False and False)

print("Result with parentheses:", result)



# -------------------------------------
# 17. Short-Circuit Evaluation
# -------------------------------------

"""
Python uses short-circuit evaluation with 'and' and 'or'.

For 'and':
    If the first value is falsy, Python does not evaluate
    the second value.

For 'or':
    If the first value is truthy, Python does not evaluate
    the second value.

Example:
"""

result = False and True

print("False and True:", result)

result = True or False

print("True or False:", result)


# 'and' returns the first falsy value or the last value.

result = 0 and 10
print("0 and 10:", result)

result = 10 and 20
print("10 and 20:", result)


# 'or' returns the first truthy value or the last value.

result = 10 or 20
print("10 or 20:", result)

result = 0 or 20
print("0 or 20:", result)



# Demonstrating short-circuit evaluation

print("\nShort-circuiting with 'and':")

result = False and print("This will not be printed.")
print("Result:", result) # Result: False (correct short-circuit)


print("\nShort-circuiting with 'or':")

result = True or print("This will not be printed.")
print("Result:", result) # Result: True (correct short-circuit)



# -----------------------------
# 18. Truthy and Falsy Values
# -----------------------------

"""
In Python, values other than True and False can also be used
in logical expressions.

Common falsy values include:

    False
    None
    0
    0.0
    ""
    []
    ()
    {}
    set()

Most other Python objects are truthy.

The bool() function converts a value to its Boolean
interpretation.
"""

print("bool(0):", bool(0))
print("bool(1):", bool(1))
print("bool(\"\"):", bool(""))
print("bool(\"Python\"):", bool("Python"))
print("bool([]):", bool([]))
print("bool([1, 2, 3]):", bool([1, 2, 3]))




# --------------------------
# 19. Truth Tables
# --------------------------

"""
AND Truth Table:

    A       B       A and B
    ------------------------
    True    True    True
    True    False   False
    False   True    False
    False   False   False


OR Truth Table:

    A       B       A or B
    -----------------------
    True    True    True
    True    False   True
    False   True    True
    False   False   False


NOT Truth Table:

    A       not A
    -------------
    True    False
    False   True
"""


# ----------------------------------------------
# 20. Logical Operators with Boolean Variables
# ----------------------------------------------

is_sunny = True
is_weekend = True

can_go_out = is_sunny and is_weekend

print("Can go out:", can_go_out)


is_raining = True
has_umbrella = False

can_go_out = not is_raining or has_umbrella

print("Can go out:", can_go_out)


# -------------------------------------
# 21. Practical Example - Login System
# -------------------------------------

"""
A login is successful only when:

    username is correct
    AND
    password is correct
"""

correct_username = True
correct_password = True

login_successful = correct_username and correct_password

print("Login successful:", login_successful)


# ------------------------------------------
# 22. Practical Example - Age Verification
# ------------------------------------------

"""
A person is considered an adult when their age is 18 or more.
"""

age = 19

is_adult = age >= 18

print("Is adult:", is_adult)




# --------------------------
# Important Notes
# --------------------------


"""
NOTE: 

1. Python has three logical operators:

       and
       or
       not

2. 'and' returns the first falsy operand;
   if all operands are truthy, it returns the last operand.

3. 'or' returns the first truthy operand;
   if all operands are falsy, it returns the last operand.

4. 'not' always returns a Boolean value:
       True or False

5. When used with Boolean expressions, 'and' and 'or'
   are commonly used to produce True or False results.    

6. Logical operators are commonly used with comparison
   operators.

7. Comparison expressions produce Boolean values.

8. Multiple logical operators can be combined in one
   expression.

9. Parentheses can be used to make expressions clearer
   and control the order of evaluation.

10. Logical operator precedence is:

       not
        ↓
       and
        ↓
       or

11. Logical operators are especially useful for combining
    multiple conditions in decision-making.

12. Conditional statements will use these logical operators
    to make decisions later in the Python learning journey.
"""




# --------------------------
# End of Logical Operators
# --------------------------

print("\nLogical Operators topic completed!")