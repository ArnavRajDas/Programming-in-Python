''' Q3: Variables & Data Types
 Create variables to store:


 Your name (string)
 Your age (integer)
 Your JEE percentile (float)

 A boolean value representing whether you are a student
 Print all of them in one line.
 '''

# Solution:

name = "Arnav"
age = 20
jee_percentile = 83.66
is_student = True

print("The name of student is " + name + ", he is " + str(age) + " year old" + ", and his JEE percentile is " + str(jee_percentile) + " and he is a student: " + str(is_student))


# or using f-string

print(f"The name of student is {name}, he is {age} year old, and his JEE percentile is {jee_percentile} and He is a student: {is_student}")