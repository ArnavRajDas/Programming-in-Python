# ============================================================
# Python Fundamentals - Comments and Escape Sequences
# ============================================================

"""
Comments and Escape Sequences in Python
----------------------------------------

In this file, we will learn:

    1. Comments (single-line and multi-line comments)
    2. Multi-line strings and docstrings
    3. Escape sequences
    4. Raw strings
    5. Basic print() usage
"""


# ----------------------------
# 1. What is a Comment?
# ----------------------------

"""
A comment is text written in a program that is ignored by
Python during program execution.

Comments are mainly used to:

    - Explain code
    - Add notes
    - Make code easier to understand
    - Describe the purpose of a section
    - Temporarily disable code
"""


# ----------------------------
# 2. Single-Line Comments
# ----------------------------

"""
A single-line comment starts with the '#' symbol.

Python ignores everything after '#' on that line.
"""

# This is a single-line comment.

print("Hello, Python!")


# ----------------------------
# 3. Comments After Code
# ----------------------------

"""
A comment can also be written after a line of code.

This is called an inline comment.
"""

age = 19  # Store the user age

print(age)


# -------------------------------------
# 4. Multiple Single-Line Comments
# -------------------------------------

# The following comments describe the code below.

name = "Arnav"
age = 19

print(name)
print(age)


# -------------------------------------
# 5. Temporarily Disabling Code
# -------------------------------------

"""
Comments can also be used to temporarily prevent a line
of code from executing.
"""

print("This line will execute.")

# print("This line will NOT execute.")

print("This line will also execute.")


# ---------------------------------
# 6. Multi-Line Comments using '#'
# ---------------------------------

"""
Python does not have a separate multi-line comment syntax
like some other programming languages.

Multiple lines beginning with '#' are commonly used when
you want to write a multi-line comment.

Example:
"""

# This is line one of a comment.
# This is line two of a comment.
# This is line three of a comment.

print("Multi-line comment example")


# -----------------------------
# 7. Triple-Quoted Strings
# -----------------------------

"""
Triple-quoted strings can span multiple lines.

They are commonly used for:

    - Documentation strings (docstrings)
    - Multi-line text

They are technically string literals, not comments.

Example:
"""

message = """
This is a
multi-line string.
"""

print(message)


# ----------------------------------
# 8. What is an Escape Sequence?
# ----------------------------------

"""
An escape sequence is a special sequence of characters
that begins with a backslash (\\).

Escape sequences are used to represent special characters
inside strings.

Examples:

    \\n
    \\t
    \\\\
    \\'
    \\"
"""


# -----------------------
# 9. Newline - \\n
# -----------------------

"""
\\n represents a newline.

It moves the following text to the next line.
"""

print("Hello\nPython")

print("Line 1\nLine 2\nLine 3")


# --------------------
# 10. Tab - \\t
# --------------------

"""
\\t represents a horizontal tab.

It is useful for creating spacing or simple formatting.
"""

print("Name:\tArnav")
print("Age:\t19")
print("Language:\tPython")


# ------------------------
# 11. Backslash - \\\\
# ------------------------

"""
\\\\ is used to represent a literal backslash.

A single backslash begins an escape sequence,
so two backslashes (\\\\) are required to represent
one literal backslash inside a normal string.
"""

print("C:\\Users\\Arnav")
print("This is a backslash: \\")


# --------------------------
# 12. Single Quote - \\'
# --------------------------

"""
\\' allows a single quote to be included inside a string
that uses single quotes.
"""

message = 'It\'s Python'

print(message)


# --------------------------
# 13. Double Quote - \\"
# --------------------------

"""
\\" allows a double quote to be included inside a string
that uses double quotes.
"""

message = "Arnav said, \"Python is easy to learn.\""

print(message)


# ----------------------------
# 14. Carriage Return - \\r
# ----------------------------

"""
\\r moves the cursor back to the beginning of the current line.

When additional text is printed after \\r, it can overwrite
the beginning of the existing line depending on the output
environment.
"""

print("Hello\rArnav")
# \r moves the cursor back to the beginning of the line.
# The visible result may vary depending on the terminal.


# --------------------------
# 15. Backspace - \\b
# --------------------------

"""
\b represents a backspace character.

It moves the cursor one position backward in many
terminal environments.
"""

print("ABC\bD")
# \b moves the cursor one position backward.
# The visible result may vary depending on the terminal.

# --------------------------
# 16. Form Feed - \\f
# --------------------------

"""
\\f represents a form feed character.

Its visual effect depends on the environment in which
the program is executed.
"""

print("Hello\fPython")


# -------------------------------------
# 17. Unicode Escape Sequence - \\u
# -------------------------------------

"""
\\u can be used to represent a Unicode character using
exactly 4 hexadecimal digits.

Example:

    \\u03A9 -> Ω
"""

print("\u03A9")    # Greek capital letter Omega (Ω)
print("\u2764")    # Heart symbol  ❤


# -------------------------------------
# 18. Unicode Escape Sequence - \U
# -------------------------------------

"""
\\U can be used to represent a Unicode character using
exactly 8 hexadecimal digits.

Example:

    \\U0001F600 -> 😀
"""

print("\U0001F600")    # 😀


# -------------------------------------
# 19. Raw Strings
# -------------------------------------

"""
A raw string treats backslashes as literal characters
instead of interpreting most escape sequences.

Raw strings are created by placing 'r' before the string.

Raw strings are especially useful when working with
Windows file paths and regular expressions.

Example:
"""

path = r"C:\Users\Arnav\Documents"

print(path)


# Compare normal and raw strings:

normal_path = "C:\\Users\\Arnav\\Documents"
raw_path = r"C:\Users\Arnav\Documents"

print(normal_path)
print(raw_path)

# -------------------------------------
# 20. Common Escape Sequences
# -------------------------------------

"""
Common Python escape sequences:

    \\n      Newline
    \\t      Horizontal tab
    \\\\      Backslash
    \\'      Single quote
    \\"      Double quote
    \\r      Carriage return
    \\b      Backspace
    \\f      Form feed
    \\u      Unicode character
    \\U      Unicode character
"""


# -------------------------------------
# 21. Combining Escape Sequences
# -------------------------------------

"""
Multiple escape sequences can be used in the same string.
"""

print("Name:\tArnav\nAge:\t19\nLanguage:\tPython")


# -------------------------------------
# 22. Basic print() Function
# -------------------------------------

"""
The print() function is used to display output.

Syntax:

    print(value)
"""

print("Hello, World!")
print("Welcome to Python!")


# -------------------------------------
# 23. Printing Multiple Values
# -------------------------------------

"""
Multiple values can be passed to print() by separating
them with commas.
"""

name = "Arnav"
age = 19

print("Name:", name)
print("Age:", age)


# -------------------------------------
# 24. print() with sep
# -------------------------------------

"""
The sep parameter controls the separator between multiple
values passed to print().

By default, sep is a space.
"""

print("Python", "Java", "C++")

print("Python", "Java", "C++", sep=" | ")


# -------------------------------------
# 25. print() with end
# -------------------------------------

"""
The end parameter controls what is printed at the end
of the output.

By default:

    end = "\\n"

which means print() moves to a new line.
"""

print("Hello", end=" ")
print("Python!")

print("A", end="-")
print("B", end="-")
print("C")


# -------------------------------------------
# 26. Comments + Escape Sequences + print()
# -------------------------------------------

"""
These concepts can be combined together to create
clean and readable output.
"""

# Display a simple student profile.

print("-------------------------------------")
print("       STUDENT PROFILE")
print("-------------------------------------")

print("Name:\tArnav")
print("Age:\t19")
print("Topic:\tPython - Comments and Escape Sequences")

print("-------------------------------------")


# -------------------------------------
# 27. Important Notes
# -------------------------------------

"""
Important Notes
---------------

1. Comments are ignored during program execution.

2. Use '#' for single-line comments.

3. Multiple '#' lines can be used for multi-line comments.

4. Triple-quoted strings are string literals and are often
   used as docstrings. They are not technically comments.

5. Escape sequences begin with a backslash (\\).

6. \\n creates a new line.

7. \\t creates a horizontal tab.

8. \\\\ represents a literal backslash.

9. \\' represents a single quote.

10. \\" represents a double quote.

11. \\r represents a carriage return.

12. \\b represents a backspace.

13. \\f represents a form feed.

14. \\u and \\U can represent Unicode characters.

15. Raw strings are useful when working with strings that
    contain many backslashes, such as Windows file paths.

16. print() displays values to the console.

17. print() supports useful parameters such as sep and end.
"""




# ---------------------------------------
# End of Comments and Escape Sequences
# ---------------------------------------


print("\nComments and Escape Sequences topic completed!")