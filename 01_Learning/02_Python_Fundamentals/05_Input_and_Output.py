# ============================================
# Python Fundamentals - Input and Output
# ============================================

"""
Input and Output in Python
----------------------------

Input and Output are fundamental parts of programming.

Input:
    Receiving data from the user.

Output:
    Displaying information to the user.

Python mainly uses:

    input()  -> Take input from the user
    print()  -> Display output to the user

Basic flow:

    User
      ↓
    input()
      ↓
    Store the value
      ↓
    Process the value
      ↓
    print()
      ↓
    Output
"""


# ----------------------------
# 1. What is Input?
# ----------------------------

"""
Input means receiving data from the user while the program
is running.

Python provides the input() function for taking user input.

Syntax:

    input("message")

The message inside input() is called a prompt.
It tells the user what they should enter.
"""

name = input("Enter your name: ")

print(name)


# ----------------------------
# 2. What is Output?
# ----------------------------

"""
Output means displaying information to the user.

Python uses the print() function to display output.

Basic syntax:

    print(value)
"""

print("Hello, " + name + "!")
print("Welcome to programming!")


# ---------------------------------
# 3. Taking Input and Printing It
# ---------------------------------

"""
The value entered by the user can be stored in a variable
and then displayed using print().
"""

name = input("Enter your name: ")

print("Your name is:", name)


# -------------------------------------
# 4. input() Always Returns a String
# -------------------------------------

"""
NOTE: One of the most important things to remember:

      input() always returns a string (str).

Even if the user enters a number, Python initially
treats that input as a string.
"""

age = input("Enter your age: ")

print("Age:", age)
print("Type:", type(age))


# Example:

number = input("Enter a number: ")

print("Number:", number)
print("Type:", type(number))


# --------------------------------------------
# 5. Why Numeric Input Needs Type Conversion
# --------------------------------------------

"""
Suppose the user enters:

    10
    20

input() returns:

    "10"
    "20"

These are strings.

Therefore:

    "10" + "20"

produces:

    "1020"

instead of:

    30
"""

first_number = input("Enter first number: ")
second_number = input("Enter second number: ")

print("Without conversion:", first_number + second_number)


# --------------------------------------------
# 6. Converting Input into an Integer
# --------------------------------------------

"""
If we want to perform mathematical operations on user input,
we need to convert the input from str to int.

We can use:

    int()
"""

first_number = input("Enter first number: ")
first_number = int(first_number)

second_number = input("Enter second number: ")
second_number = int(second_number)

print("Sum:", first_number + second_number)


# --------------------------------------------
# 7. Direct Conversion with input()
# --------------------------------------------

"""
Instead of writing:

    number = input("Enter a number: ")
    number = int(number)

we can directly write:

    number = int(input("Enter a number: "))

This takes the input and converts it into an integer
immediately.
"""

number = int(input("Enter a number: "))

print("Number:", number)
print("Type:", type(number))


# ----------------------------------
# 8. Taking Multiple Inputs
# ----------------------------------

"""
We can take multiple inputs and store them in different
variables.
"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Name:", name)
print("Age:", age)



# ------------------------------------------
# 9. Taking Multiple Values in One Line
# ------------------------------------------

"""
We can take multiple values from the user in a single line.

split() separates the input into multiple values.

Example:

    10 20

becomes:

    ["10", "20"]

For numeric input, map() can be used to convert
each value into an integer.

map() applies a function to each item in an iterable.
"""

a, b = map(int, input("Enter two numbers: ").split())

print("First number:", a)
print("Second number:", b)
print("Sum:", a + b)


# ----------------------------------
# 10. Addition of Two Numbers
# ----------------------------------

"""
Example:

    Take two numbers from the user
          ↓
    Convert them into integers
          ↓
    Add them
          ↓
    Display the result
"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

c = a + b

print("Sum:", c)

print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))


# -------------------------------------------------
# 11. Different Arithmetic Operations with Input
# -------------------------------------------------

"""
User input can be used with arithmetic operators.

Here we use:

    +   Addition
    -   Subtraction
    *   Multiplication
    /   Division
"""

a = float(input("Enter first number: "))
b = float(input("Enter second number (non-zero): "))

# If the user enters 0, the program raises ZeroDivisionError.

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


# ---------------------------------------
# 12. Integer Input vs Float Input
# ---------------------------------------

"""
Use int() when the user should enter a whole number.

Use float() when the user may enter a decimal number.

Example:

    int("10")     --> 10
    float("10.5") --> 10.5
"""

age = int(input("Enter your age: "))
print("Age:", age)

jee_percentile = float(input("Enter the JEE percentile: "))
print("JEE Percentile:", jee_percentile)


# --------------------------------
# 13. Taking String Input
# --------------------------------

"""
Strings do not need conversion because input() already
returns a string.
"""

name = input("Enter your name: ")
city = input("Enter your city: ")

print("Name:", name)
print("City:", city)


# --------------------------------
# 14. Input with a Calculation
# --------------------------------

"""
User input can be used directly in calculations after
appropriate type conversion.
"""

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area:", area)


# -----------------------------------------
# 15. Practical Example - Student Marks
# -----------------------------------------

"""
Take marks of three subjects from the user and calculate
the total and average.
"""

maths = float(input("Enter Mathematics marks: "))
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))

total = maths + physics + chemistry
average = total / 3

print("Total marks:", total)
print("Average marks:", average)

# --------------------------------------------
# 16. Practical Example - Simple Calculator
# --------------------------------------------

"""
A simple calculator can use:

    Input
      ↓
    Conversion
      ↓
    Calculation
      ↓
    Output
"""

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number (non-zero): "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)


# -----------------------------------------
# 17. Output Using Multiple Values
# -----------------------------------------

"""
print() can display multiple values by separating them
with commas.
"""

name = "Arnav"
age = 19
topic = "Input and Output"

print("Name:", name, "Age:", age, "Topic:", topic)


# --------------------------
# 18. Output Using sep
# --------------------------

"""
The sep parameter controls the separator between values.

Default:

    sep = " "
"""

name = "Arnav"
age = 19

print(name, age)

print(name, age, sep=" | ")  # Output: Arnav | 19

# Example:
print("2026", "08", "25", sep="-")  # Output: 2026-08-25


# --------------------------
# 19. Output Using end
# --------------------------

"""
The end parameter controls what print() adds after the output.

By default:

    end = "\\n"

which means print() moves to the next line.
"""

print("Hello", end=" ")
print("Arnav")  # Output: Hello Arnav

print("All", end=" - ")
print("Good")  # Output: All - Good


# ---------------------------------------
# 20. Formatted Output with f-Strings
# ---------------------------------------

"""
An f-string is a formatted string that allows variables
and expressions to be placed directly inside a string.

To create an f-string, place the letter 'f' before
the opening quotation mark.

Syntax:

    f"Text {variable}"

Expressions can also be placed inside curly braces.

Example:

    f"Sum: {a + b}"
"""


# Using variables:

name = "Arnav"
age = 19

print(f"My name is {name} and I am {age} years old.")


# Another example:

marks = 450
total_marks = 500

print(f"I scored {marks} out of {total_marks} marks.")


# Using expressions:

x = 10
y = 5

print(f"The sum of {x} and {y} is {x + y}")


# ---------------------------------
# 21. Escape Sequences in Output
# ---------------------------------

"""
Escape sequences can be used when displaying output.

Some common examples:

    \\n --> New line
    \\t --> Tab

These were introduced in the previous topic.
"""

print("Name:\tArnav")
print("Age:\t19")

print("Python\nProgramming")


# ---------------------------------
# 22. Input -> Process -> Output
# ---------------------------------

"""
A very common programming pattern is:

    INPUT
      ↓
    PROCESS
      ↓
    OUTPUT

Example:
"""

number = int(input("Enter a number: "))

square = number * number

print("Square:", square)


# ---------------------------------------------------
# 23. Another Input -> Process -> Output Example
# ---------------------------------------------------

"""
Problem:

Take the user's age and calculate their age after 5 years.
"""

age = int(input("Enter your current age: "))

future_age = age + 5

print("Your age after 5 years will be:", future_age)


# ---------------------------------------------------
# 24. Handling Input Conversion Carefully
# ---------------------------------------------------

"""
If the user enters something that cannot be converted into
the requested type, Python will raise an error.

For example:

    int("hello")

will produce a ValueError.

Similarly:

    float("Arnav")

will produce a ValueError.

Example of invalid input:

    age = int(input("Enter your age: "))

If the user enters:

    abc

the program will raise a ValueError.

Error handling will be studied later.
"""


# ---------------------------------------------------
# 25. Common Mistake - Forgetting Type Conversion
# ---------------------------------------------------

"""
WRONG for mathematical addition:

    a = input("Enter first number: ")
    b = input("Enter second number: ")

    print(a + b)

If the user enters 10 and 20:

    Output -> 1020

because both values are strings.

CORRECT:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a + b)

Output:

    30
"""

# Correct example:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)


# --------------------------------
# 26. Input and Output Workflow
# --------------------------------

"""
General workflow:

    User enters data
           ↓
        input()
           ↓
    Store the input
           ↓
    Check/convert the type
           ↓
      Process the data
           ↓
        print()
           ↓
     Display the result
"""


# ------------------------
# 27. Important Notes
# ------------------------

"""
Important Notes
---------------

1. input() is used to receive data from the user.

2. input() always returns a string.

3. Use int() when integer input is required.

4. Use float() when decimal input is required.

5. Strings can be used directly because input() already
   returns a string.

6. Numeric input usually needs type conversion before
   performing mathematical operations.

7. int(input(...)) converts user input directly into an integer.

8. float(input(...)) converts user input directly into a float.

9. print() is used to display output.

10. print() can display multiple values.

11. sep controls the separator between multiple values.

12. end controls what is printed after the output.

13. f-strings provide a convenient way to format output.

14. Invalid input conversion can raise ValueError.

15. A common programming pattern is:

        Input
          ↓
        Process
          ↓
        Output
"""


# ----------------------------
# End of Input and Output
# ----------------------------

print("\nInput and Output topic completed!")