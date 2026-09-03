# ============================================================
# Python Fundamentals - Operator Precedence
# ============================================================

"""
Operator Precedence
---------------------

Operator precedence determines how Python groups operators
in an expression and which operations are performed first.

When an expression contains multiple operators:
    - Higher-precedence operators are handled first.
    - Parentheses can change the order.
    - Associativity determines grouping when appropriate.

This topic brings together the operators learned so far and
shows how Python decides what happens first.
"""


# -------------------------------
# 1. Basic Operator Precedence
# -------------------------------

"""
Example:

    10 + 5 * 2

Multiplication has higher precedence than addition.

So Python evaluates:

    5 * 2 = 10
    10 + 10 = 20

Result:
    20

It is NOT:

    (10 + 5) * 2
    = 30
"""

result = 10 + 5 * 2
print("10 + 5 * 2 =", result)


# -----------------
# 2. Parentheses
# -----------------

"""
Parentheses can be used to explicitly group parts of an
expression.

They allow us to override the normal operator precedence
and make the intended order of evaluation clear.

Without parentheses:

    2 + 3 * 4
    = 14

With parentheses:

    (2 + 3) * 4
    = 20

Using parentheses is also useful when they make the intended
logic easier for another programmer to understand.
"""

without_parentheses = 2 + 3 * 4
with_parentheses = (2 + 3) * 4

print("2 + 3 * 4 =", without_parentheses)
print("(2 + 3) * 4 =", with_parentheses)


# ----------------------------------------
# 3. Precedence Order Used in This Module
# ----------------------------------------

"""
From HIGHER to LOWER precedence:

    1.  ()                         Parentheses

    2.  **                         Exponentiation
    (special relationship 
    with unary operators)

    3.  +x, -x, ~x                 Unary operators

    4.  *, /, //, %                Multiplication group

    5.  +, -                       Addition / subtraction

    6.  <<, >>                     Bitwise shifts

    7.  &                          Bitwise AND

    8.  ^                          Bitwise XOR

    9.  |                          Bitwise OR

    10. <, <=, >, >=, ==, !=       Comparisons
        is, is not
        in, not in

    11. not                        Logical NOT

    12. and                        Logical AND

    13. or                         Logical OR


NOTE:
    Exponentiation has a special relationship with unary
    operators. See Section 7 for the detailed example.    


This is a simplified reference containing the operators
covered in this Python Fundamentals module.

Assignment (=) and augmented assignments such as += and -=
are statements and are not included in this expression
precedence list.
"""


# ----------------------------
# 4. Arithmetic Precedence
# ----------------------------

"""
Arithmetic precedence:

    **  →  *, /, //, %  →  +, -

Example:

    2 + 3 * 4 ** 2

Step 1:
    4 ** 2 = 16

Step 2:
    3 * 16 = 48

Step 3:
    2 + 48 = 50
"""

result = 2 + 3 * 4 ** 2
print("2 + 3 * 4 ** 2 =", result)


# ---------------------------------------
# 5. Operators with the Same Precedence
# ---------------------------------------

"""
When operators have the same precedence, their associativity
determines how they are grouped.

For these arithmetic operators, when operators have the
same precedence, they group from left to right.

Example:

    20 - 5 + 2

Both - and + have the same precedence.

Therefore:

    (20 - 5) + 2
    = 17

Similarly:

    20 / 5 * 2

becomes:

    (20 / 5) * 2
    = 8

"""

result_1 = 20 - 5 + 2
result_2 = 20 / 5 * 2

print("20 - 5 + 2 =", result_1)
print("20 / 5 * 2 =", result_2)


result_3 = 20 // 6 * 2
result_4 = 20 % 6 + 2

print("20 // 6 * 2 =", result_3)
print("20 % 6 + 2 =", result_4)


# ---------------------------------------
# 6. Exponentiation is Right-Associative
# ---------------------------------------

"""
Exponentiation (**) is an important exception.

It associates from RIGHT to LEFT.

Example:

    2 ** 3 ** 2

Python interprets this as:

    2 ** (3 ** 2)

Step 1:
    3 ** 2 = 9

Step 2:
    2 ** 9 = 512

Therefore:

    2 ** 3 ** 2 = 512

It is NOT:

    (2 ** 3) ** 2
    = 64
"""

result = 2 ** 3 ** 2

print("2 ** 3 ** 2 =", result)
print("2 ** (3 ** 2) =", 2 ** (3 ** 2))
print("(2 ** 3) ** 2 =", (2 ** 3) ** 2)


# ---------------------------------------
# 7. Unary Operators and Exponentiation
# ---------------------------------------

"""
Unary +, - and ~ have a special relationship with **.

The exponentiation operator has a special relationship with
unary operators, so parentheses are recommended when the
intended meaning could be unclear.

For example:

    -2 ** 2

means:

    -(2 ** 2)

So the result is:

    -4

If the negative number itself should be raised to the power,
use parentheses:

    (-2) ** 2

Result:

    4
"""

result_1 = -2 ** 2
result_2 = (-2) ** 2

print("-2 ** 2 =", result_1)
print("(-2) ** 2 =", result_2)


# ------------------------
# 8. Bitwise Precedence
# ------------------------

"""
The bitwise operators covered in this module have this order:

    <<, >>   →   &   →   ^   →   |

So:

    2 | 3 & 1

is interpreted as:

    2 | (3 & 1)

First:

    3 & 1 = 1

Then:

    2 | 1 = 3

Parentheses can change the grouping.
"""

result = 2 | 3 & 1

print("2 | 3 & 1 =", result)
print("2 | (3 & 1) =", 2 | (3 & 1))
print("(2 | 3) & 1 =", (2 | 3) & 1)


# --------------------------------------------
# 9. Shift Operators vs Arithmetic Operators
# --------------------------------------------

"""
Shift operators have lower precedence than addition and
subtraction.

Example:

    2 + 3 << 1

Addition happens first:

    2 + 3 = 5

Then:

    5 << 1 = 10

Therefore:

    2 + 3 << 1 = 10
"""

result = 2 + 3 << 1

print("2 + 3 << 1 =", result)
print("(2 + 3) << 1 =", (2 + 3) << 1)
print("2 + (3 << 1) =", 2 + (3 << 1))


# ---------------------------------------
# 10. Arithmetic Before Comparisons
# ---------------------------------------

"""
Arithmetic operators have higher precedence than comparisons.

Example:

    5 + 3 > 6

Python evaluates:

    5 + 3
    = 8

Then:

    8 > 6
    = True

So this behaves like:

    (5 + 3) > 6
"""

result = 5 + 3 > 6

print("5 + 3 > 6 =", result)


# ------------------------------------------
# 11. Comparisons Before Logical Operators
# ------------------------------------------

"""
Comparison operators have higher precedence than logical
operators.

Example:

    10 > 5 and 8 < 12

Python first evaluates the comparisons:

    10 > 5
    8 < 12

Then:

    True and True

Result:

    True

Therefore, this can be understood as:

    (10 > 5) and (8 < 12)
"""

result = 10 > 5 and 8 < 12

print("10 > 5 and 8 < 12 =", result)


# --------------------------
# 12. Logical Precedence
# --------------------------

"""
The logical operators follow this precedence:

    not
      ↓
    and
      ↓
    or

Example:

    True or False and False

First:

    False and False
    = False

Then:

    True or False
    = True

So:

    True or False and False
    = True

Parentheses can change this:

    (True or False) and False
    = False
"""

result_1 = True or False and False
result_2 = (True or False) and False

print("True or False and False =", result_1)
print("(True or False) and False =", result_2)


# --------------------------
# 13. Comparison Chaining
# --------------------------

"""
Python allows comparisons to be chained.

Example:

    10 < 20 < 30

This is equivalent in meaning to:

    10 < 20 and 20 < 30

Both comparisons must be true.

Comparison chaining is especially useful for range checks.
"""

result = 10 < 20 < 30

print("10 < 20 < 30 =", result)


# --------------------------
# 14. Practical Range Check
# --------------------------

"""
Instead of writing:

    age >= 18 and age <= 60

Python allows:

    18 <= age <= 60

This checks that age is at least 18 and at most 60.
"""

age = 20

result = 18 <= age <= 60

print("Age is between 18 and 60:", result)


# ----------------------------------------------------------------
# 15. Comparison, Membership, and Identity with Logical Operators
# ----------------------------------------------------------------

"""
Membership and identity operators have higher precedence
than logical operators.

Example:

    "Arnav" in names and age >= 18

Python first checks:

    "Arnav" in names
    age >= 18

Then it applies:

    and

This follows the general rule:

    Specific checks → logical operators
"""

names = ["Arnav", "Shreya", "Shambhavi", "Pushp"]

name = "Arnav"
age = 20

result = name in names and age >= 18

print(name, "Allowed:", result)


# -----------------------
# 16. Mixed Expression
# -----------------------

"""
The best way to understand precedence is to follow an
expression containing several different operator groups.

Example:

    5 + 2 * 3 > 10 and 4 ** 2 == 16

Order:

    1. 4 ** 2 = 16
    2. 2 * 3 = 6
    3. 5 + 6 = 11
    4. 11 > 10 = True
    5. 16 == 16 = True
    6. True and True = True

Final result:

    True
"""

result = 5 + 2 * 3 > 10 and 4 ** 2 == 16

print("Mixed expression result:", result)


# ------------------------------------
# 17. Precedence vs Associativity
# ------------------------------------

"""
PRECEDENCE:
    Determines which operator has priority when different
    precedence levels are involved.

Example:

    2 + 3 * 4

    * has higher precedence than +

    Therefore:
        2 + (3 * 4)


ASSOCIATIVITY:
    Determines how operators with the same precedence are
    grouped.

Example:

    20 - 5 + 2

    + and - have the same precedence.

    Therefore:
        (20 - 5) + 2


Important exception:

    ** is right-associative:

        2 ** 3 ** 2

    means:

        2 ** (3 ** 2)
"""


# ------------------------------------
# 18. Parentheses for Readability
# ------------------------------------

"""
Parentheses are not only useful when you need to change
precedence.

They can also make your intention clearer.

For example:

    age >= 18 and has_id or is_member

is interpreted according to Python's precedence rules.

Writing:

    (age >= 18 and has_id) or is_member

makes the intended grouping obvious to the reader.

Good code should be understandable to humans, not only
correct according to Python's rules.
"""

age = 20
has_id = True
is_member = False

result = (age >= 18 and has_id) or is_member

print("Can enter:", result)


# -----------------------
# 19. Common Mistakes
# -----------------------

"""
1. Assuming everything is evaluated from left to right.

   10 + 5 * 2

   is:

       10 + (5 * 2)

   not:

       (10 + 5) * 2


2. Forgetting that ** is right-associative.

   2 ** 3 ** 2

   is:

       2 ** (3 ** 2)


3. Forgetting logical precedence.

   not > and > or


4. Assuming bitwise and logical operators have the same
   precedence.

   They are separate operator groups.


5. Forgetting that comparisons can be chained.

   18 <= age <= 60

   is a valid Python expression.


6. Writing complicated expressions without considering
   readability.

   If parentheses make your intention clearer, use them.


7. Confusing precedence with associativity.

   Precedence:
       Which operator has priority?

   Associativity:
       How is an expression grouped when the relevant operators
       have the same precedence?
"""


# ---------------------------------
# 20. Final Practice Expression
# ---------------------------------

"""
Before checking the output, try to calculate this yourself:

    result = (5 + 2) * 3 ** 2 > 20 and 10 % 3 == 1

Work through the important precedence levels:

    (5 + 2) = 7
    3 ** 2 = 9
    7 * 9 = 63
    63 > 20 = True
    10 % 3 = 1
    1 == 1 = True
    True and True = True

Final result:

    True
"""

result = (5 + 2) * 3 ** 2 > 20 and 10 % 3 == 1

print("\nFinal practice result:", result)


# ----------------
# Key Points
# ----------------

"""
KEY TAKEAWAYS
-------------

1. Operator precedence determines how operators are grouped
   and which operations are performed first.

2. Parentheses can override the normal precedence order.

3. Arithmetic precedence:
       ** → *, /, //, % → +, -

4. Bitwise precedence:
       <<, >> → & → ^ → |

5. Comparisons are evaluated before logical operators.

6. Logical precedence:
       not → and → or

7. Most relevant same-precedence operators group
   left-to-right.

8. ** is right-associative.

9. Python supports chained comparisons:
       18 <= age <= 60

10. Parentheses can improve both correctness and readability.

11. Assignment operators such as = and += are treated
    separately from ordinary expression precedence.

The main idea to remember:

    Parentheses
        ↓
    Higher precedence
        ↓
    Lower precedence
        ↓
    Associativity when applicable
"""


# --------------------
# Topic Completed
# --------------------

print("\nOperator Precedence topic completed!")