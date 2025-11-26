print("Hello World !")
print("*" * 10)
# this is to multiply x ten times.
(2 + 1)

# declaring a variables. this is done using formatting which is autopep8
x = 1

x = 2
x = 5

# example of an expression
print("*" * 3)

# We have primetive types of data,
# Boolean (true, false), string (""), and numbers (integers and float)
students_count = 100
rating = 3.9
published_today = True
course_name = "Python Programming"

# one thing to know about python is that it is case sensitive, so always use lower case letter,
# and to make code understandable, it is only underscore that can be used to separate variables (_)

# this is string. checking the characters and forming an argument
course = "Python Programming"
print(len(course))
# adding and array (basically a square bracket, always starts from zero)
print(course[0])
# printing a negative index: thise pring out the character from backwards
print(course[-1])
# this is extracting characters: basically telling the computer how many chracters it should print
print(course[0:3])
print(course[0:])
print(course[:4])
print(course[:])

# escape sequences in python
# \ = this back slash mean escape characters
# \'' = this mean escape sequence
# \n = this mean new line
# \'
# \\
My_name = "Reginatia \nAmoah"
print(My_name)
# this is a new line
My_name = "Reginatia \Amoah"
print(My_name)
# escape characters
My_name = 'Reginatia "Amoah'
print(My_name)
# escape sequence

# this is formatted string
first = "Reginatia"
last = "Adutwumwaa"
full = first + " " + last
print(full)
# to check the length
full = f"{len(first)} {last}"
print(full)

# this part is string method
# for this is called objects, and we call the object function by
# using the . (dot) method
course = " Python"
print(course.upper())
# changing string to capital letters
print(course)
# changing string to the normal it looks
print(course.lower())
# changing string to lower case
print(course.title())
# capitalising the first letter of each word
print(course.strip())
# to remove the wide space from the beginning and end of string
print(course.find("thon"))
# this is basically fing the index of the character pro from the beginning
print(course.replace("p", "j"))
# this is replacing the letter p(first letter), with the letter j(second lettter)
print("pro" in course)
print("pro" not in course)

# we are on Numbers now
# we have integer, float, and complext
x = 1
# this is integer
x = 1.1
# this is float
x = 1 + 2j
# this is complex. 3xpression: a + bi. use j to represent the i

# this is standard arithmetic operation
# for this we have addition, multiplication, subtraction, and division
print(10 + 2)
print(20 - 4)
print(6 * 5)
print(10 / 3)
# for it to be a whole a number then two slash should be used
print(10 // 3)
print(10 % 3)
print(10**3)

# Augmented Assignment Operator
x = 10
x = x + 3
x += 3  # this is augmented assignment operator

# this part is working with numbers
print(round(3.9))
# this is for rounding a number
print(abs(-2.9))
# this is returning the absolute value of a number. basically, the output being the opposite sign

# this is type conversion
x = input("x : ")
y = int(x) + 1
print(f"x: {x}, y: {y}")

# we are on comparison operators. the types of operators are;
# >,<,<=,>=,= =,!=
# for all of theses operators when used it will turn true the fact that the types are the same
# with e.g 10 = "10", -with this you will get a false because
# -thwy have different types,
# -they store differently in the computers memory

# next is conditional statement. we have:
# if statement = this will print the statment made in the print function because everything is tru
# elif (else if) = this is bringing in multiple conditions
# else = the statement here will print when the conditions statement are not true

# we are on Ternary Operator
age = 22
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

# this is Logical operator
# we have 3; they are:
# and, or , not
# and(when conditions are the same), or (when one condition is false and other is true), not ()
high_income = True
high_credit = True
if high_income and high_credit:
    print("Eligible")
else:
    print("not eligible")
# this is the "and" logical operator

high_income = False
high_credit = True
if high_income and high_credit:
    print("Eligible")
else:
    print("not eligible")
# this is the "or" logical operator

# this is for loops
# it is used to create repetition
for number in range(3):
    print("Attempt")
    print("Attempt", number)
    print("Attempt", number + 1)
    print("Attempt", number + 1, (number + 1) * ".")

# Exercise:
# write a program to display the even numbers between 1 to 10
# b.type the statement: we have 4 even numbers
# hint given: call the range function: range = (1, 10). do not call the third argument, which is called, "Step".
count = 0  # this is what we add starting to type the statement own
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
print(
    f"we have {count} even numbers"
)  # this is addintion of what we add to reveal the message
