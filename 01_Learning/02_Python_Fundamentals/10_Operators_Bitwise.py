# ============================================================
# Python Fundamentals - Bitwise Operators
# ============================================================

"""
Bitwise Operators in Python
---------------------------

Bitwise operators work on the individual bits of integer
values.

Before understanding bitwise operators, it is useful to
understand binary numbers.

Decimal numbers use base 10:

    0, 1, 2, 3, 4, 5, ...

Binary numbers use base 2:

    0, 1

Python provides six main bitwise operators:

    &    Bitwise AND
    |    Bitwise OR
    ^    Bitwise XOR
    ~    Bitwise NOT
    <<   Left Shift
    >>   Right Shift

Bitwise operators are mainly used with integers.
"""


# ---------------------------
# 1. Binary Numbers
# ---------------------------

"""
Computers represent data internally using bits.

A bit can have one of two values:

    0
    1

For example:

    Decimal 5 = Binary 101

Because:

    1 × 4 + 0 × 2 + 1 × 1
    = 4 + 0 + 1
    = 5

    Binary representation of the decimal number 5 is 101. The binary system uses base 2, where each digit represents a power of 2. In this case, the leftmost digit (1) represents 2^2 (which is 4), the middle digit (0) represents 2^1 (which is 2), and the rightmost digit (1) represents 2^0 (which is 1). When you add these values together, you get the original decimal number, which is 5.

    
Binary positions:

        4   2   1
        ↓   ↓   ↓
        1   0   1

        = 5
"""

print("Binary representation of 5:", bin(5))
print("Binary representation of 10:", bin(10))
print("Binary representation of 15:", bin(15))

# above code is a simple demonstration of how to convert decimal numbers to their binary representation using the bin() function in Python. The bin() function takes an integer as input and returns a string that represents the binary equivalent of that integer, prefixed with '0b'.


# ---------------------------
# 2. bin() Function
# ---------------------------

"""
The bin() function returns the binary representation
of an integer as a string.

Example:

    bin(5)

returns:

    '0b101'

The prefix '0b' indicates that the number is represented
in binary.
"""

number = 5

print("Decimal:", number)
print("Binary:", bin(number))


# ---------------------------
# 3. Bitwise AND (&)
# ---------------------------

"""
The '&' operator performs Bitwise AND.

Each corresponding pair of bits is compared.

Truth Table:

    A   B   A & B
    -----------
    0   0     0
    0   1     0
    1   0     0
    1   1     1

A bit is 1 only when BOTH corresponding bits are 1.

Example:

        5  = 0101
        3  = 0011
        ----------
        &  = 0001

Therefore:

        5 & 3 = 1
"""

a = 5
b = 3

result = a & b

print("a & b =", result)
print("Binary:", bin(result))



# ---------------------------
# 4. Bitwise OR (|)
# ---------------------------

"""
The '|' operator performs Bitwise OR.

A bit is 1 when AT LEAST ONE of the corresponding bits is 1.

Truth Table:

    A   B   A | B
    -----------
    0   0     0
    0   1     1
    1   0     1
    1   1     1

Example:

        5  = 0101
        3  = 0011
        ----------
        |  = 0111

Therefore:

        5 | 3 = 7
"""

a = 5
b = 3

result = a | b

print("a | b =", result)
print("Binary:", bin(result))



# ---------------------------
# 5. Bitwise XOR (^)
# ---------------------------

"""
The '^' operator performs Bitwise XOR
(Exclusive OR).

A bit is 1 when the two corresponding bits are DIFFERENT.

Truth Table:

    A   B   A ^ B
    -----------
    0   0     0
    0   1     1
    1   0     1
    1   1     0

Example:

        5  = 0101
        3  = 0011
        ----------
        ^  = 0110

Therefore:

        5 ^ 3 = 6
"""

a = 5
b = 3

result = a ^ b

print("a ^ b =", result)
print("Binary:", bin(result))



# ---------------------------
# 6. Bitwise NOT (~)
# ---------------------------

"""
The '~' operator performs Bitwise NOT.

It inverts the bits of an integer.

For example:

    0 --> 1
    1 --> 0

In Python, the result of bitwise NOT may look surprising
because integers can be negative and Python uses signed
integer bitwise semantics.

Python follows this relationship:

    ~n = -(n + 1)


Example:

    ~5 = -(5 + 1)
       = -6
"""

number = 5

result = ~number

print("~number =", result)

# Another example:

print("~0 =", ~0)
print("~1 =", ~1)
print("~2 =", ~2)
print("~10 =", ~10)



# ---------------------------
# 7. Left Shift (<<)
# ---------------------------

"""
The '<<' operator shifts the bits of a number to the left.

Syntax:

    number << positions

For each left shift by one position, the value is
effectively multiplied by 2 for integers.

Example:

    5 = 0101

    5 << 1

    0101 --> 1010 

    1010 = 10

Therefore:

    5 << 1 = 10
"""

number = 5

print("5 << 1 =", number << 1)
print("5 << 2 =", number << 2)
print("5 << 3 =", number << 3)


# NOTE: Left Shift with Binary Representation

number = 5

print("Original:", bin(number))
print("Left shift by 1:", bin(number << 1))
print("Left shift by 2:", bin(number << 2))


# ---------------------------
# 8. Right Shift (>>)
# ---------------------------

"""
The '>>' operator shifts the bits of a number to the right.

Syntax:

    number >> positions

For positive integers, each right shift by one position
is equivalent to floor division by 2.

Example:

    20 = 10100

    20 >> 1

    10100 --> 01010

    01010 = 10

Therefore:

    20 >> 1 = 10
"""

number = 20

print("20 >> 1 =", number >> 1)
print("20 >> 2 =", number >> 2)
print("20 >> 3 =", number >> 3)


# NOTE: Right Shift with Binary Representation

number = 20

print("Original:", bin(number))
print("Right shift by 1:", bin(number >> 1))
print("Right shift by 2:", bin(number >> 2))


# --------------------------------------------
# 9. Left Shift and Multiplication
# --------------------------------------------

"""
For non-negative integers, left shifting by n positions is equivalent to multiplying by 2 ** n.

    number << 1
        is equivalent to
    number * 2

    number << 2
        is equivalent to
    number * 4

    number << 3
        is equivalent to
    number * 8

Example:
"""

number = 5

print("5 << 1:", number << 1)
print("5 * 2 :", number * 2)

print("5 << 2:", number << 2)
print("5 * 4 :", number * 4)


# --------------------------------------------
# 10. Right Shift and Floor Division
# --------------------------------------------

"""
For non-negative integers, right shifting by n positions is equivalent to floor division by 2 ** n.

    number >> 1
        is equivalent to
    number // 2

    number >> 2
        is equivalent to
    number // 4

Example:
"""

number = 20

print("20 >> 1:", number >> 1)
print("20 // 2:", number // 2)

print("20 >> 2:", number >> 2)
print("20 // 4:", number // 4)



# ------------------------------------------------------------
# 11. Bitwise Operations with Binary Representation
# ------------------------------------------------------------

"""
Bitwise Operations with Binary Representation
----------------------------------------------

Bitwise operations work on the individual bits of integers.

Let's compare two numbers in binary and see the result
of AND, OR, and XOR.

Example:

    12 = 1100
     5 = 0101

The operations are:

    1100
  & 0101
  ------
    0100    --> 4

    1100
  | 0101
  ------
    1101    --> 13

    1100
  ^ 0101
  ------
    1001    --> 9

Python can display these results in binary using bin().
"""

a = 12
b = 5

print("a =", a, "-->", bin(a))
print("b =", b, "-->", bin(b))

print("\nBitwise AND:")
print("a & b =", a & b)
print("Binary:", bin(a & b))

print("\nBitwise OR:")
print("a | b =", a | b)
print("Binary:", bin(a | b))

print("\nBitwise XOR:")
print("a ^ b =", a ^ b)
print("Binary:", bin(a ^ b))




# ------------------------------------------------------------
# 12. Bitwise AND - Checking the Least Significant Bit
# ------------------------------------------------------------

"""
Bitwise AND can be used to check whether a particular bit
is set.

For example:

    number & 1

checks the least significant bit (the rightmost bit).

For a non-negative integer:

    result = 0 --> even
    result = 1 --> odd

Example:

    10 = 1010
     1 = 0001
    ----------
    &  = 0000 --> 0

    11 = 1011
     1 = 0001
    ----------
    &  = 0001 --> 1
"""

number = 10

result = number & 1

print("10 & 1 =", result)

number = 11

result = number & 1

print("11 & 1 =", result)


# NOTE:
# Even or Odd — Bitwise Concept

"""
The least significant bit tells us whether a non-negative
integer is even or odd.

    Even number --> last binary bit is 0
    Odd number  --> last binary bit is 1

Therefore:

    number & 1

produces:

    0 --> even
    1 --> odd

We will use if/else later to turn this result into a
complete program that prints "Even" or "Odd".
"""



# ---------------------------------
# 13. XOR and Bit Toggling
# ---------------------------------

"""
XOR can be used to toggle bits.

If a bit is XORed with:

    0 --> it stays the same
    1 --> it is flipped

Example:

    0 ^ 1 = 1
    1 ^ 1 = 0

This property is useful in bit manipulation.
"""

number = 5
mask = 1

print("Original:", number)
print("After XOR:", number ^ mask)


# ------------------------------
# 14. Binary Integer Literals
# ------------------------------

"""
Python allows integers to be written using binary literals
with the '0b' or '0B' prefix.

Example:

    0b101 = 5
    0b011 = 3

These are still integers.
"""

a = 0b101
b = 0b011

print("a:", a)
print("b:", b)

print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)



# ----------------------------------------------------
# 15. Common Mistake - Logical vs Bitwise Operators
# ----------------------------------------------------

"""
Do not confuse logical operators with bitwise operators.

Logical operators:

    and
    or
    not

Bitwise operators:

    &
    |
    ^
    ~

Logical operators work with Boolean logic.

Bitwise operators work on the individual bits of integers.
"""

a = True
b = False

print("Logical AND:", a and b)
print("Logical OR:", a or b)


a = 5
b = 3

print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)


# --------------------------------------------
# 16. Common Mistake - ^ is NOT Power
# --------------------------------------------

"""
A common beginner mistake is thinking '^' means power.

In Python:

    ** --> Exponentiation
    ^  --> Bitwise XOR

Example:

    2 ** 3 = 8

but:

    2 ^ 3 = 1
"""

print("2 ** 3 =", 2 ** 3)
print("2 ^ 3 =", 2 ^ 3)



# --------------------------------------------
# 17. Practical Example - Permission Flags
# --------------------------------------------

"""
Bitwise operators are sometimes used with flags or masks.

For example, different bits can represent different
permissions.

Example:

    001 --> Read
    010 --> Write
    100 --> Execute

Multiple permissions can be combined using OR.
"""

READ = 0b001
WRITE = 0b010
EXECUTE = 0b100

permissions = READ | WRITE

print("Permissions:", bin(permissions))


# --------------------------------------------
# 18. Checking a Permission with AND
# --------------------------------------------

"""
We can use AND to check whether a particular permission
bit is present.
"""

READ = 0b001
WRITE = 0b010

permissions = READ | WRITE

has_read = permissions & READ
has_write = permissions & WRITE

print("Has read permission:", bool(has_read))
print("Has write permission:", bool(has_write))


# --------------------------------------------
# 19. XOR Bit Manipulation with Binary Masks
# --------------------------------------------

"""

A mask can be used to target a specific bit.

Example:

    number = 101
    mask   = 001

XOR:

    101
    001
    ---
    100

Using XOR with a mask allows us to toggle
specific bits while leaving bits where the mask
contains 0 unchanged.
"""

number = 0b101

mask = 0b001

result = number ^ mask

print("Original:", bin(number))
print("After XOR:", bin(result))


# --------------------------------------------
# 20. Bitwise Operator Summary
# --------------------------------------------

"""
Operator    Name                 Basic Purpose

    &       Bitwise AND          Both bits must be 1

    |       Bitwise OR           At least one bit is 1

    ^       Bitwise XOR          Bits must be different

    ~       Bitwise NOT          Flips the bits

    <<      Left Shift            Shifts bits to the left

    >>      Right Shift           Shifts bits to the right
"""




# ---------------------------
# 21. Important Notes
# ---------------------------

"""
Important Notes
---------------

1. Bitwise operators work on the bits of integer values.

2. Python provides six main bitwise operators:

       &    AND
       |    OR
       ^    XOR
       ~    NOT
       <<   Left Shift
       >>   Right Shift

3. AND produces 1 only when both corresponding bits are 1.

4. OR produces 1 when at least one corresponding bit is 1.

5. XOR produces 1 when corresponding bits are different.

6. ~n follows the relationship:

       ~n = -(n + 1)

7. Left shift moves bits to the left.

8. Right shift moves bits to the right.

9. bin() returns an integer's binary representation as a string.

10. Bitwise operators are different from logical operators.

11. '&' can be used with masks to test bits.

12. Bitwise operators are commonly used with masks,
    flags, permissions, and low-level programming.
"""



# ---------------------------
# End of Bitwise Operators
# ---------------------------

print("\nBitwise Operators topic completed!")