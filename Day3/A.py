# OPERATORS

#BOOLEAN
'''
A boolean data type represents one of the two values: True or False. 
The first letter T for True and F for False should be capital unlike JavaScript.
'''
print(True)
print(False)

#ARITHMATIC OPERATOR
"""

Addition(+): a + b
Subtraction(-): a - b
Multiplication(*): a * b
Division(/): a / b
Modulus(%): a % b
Floor division(//): a // b
Exponential(**): a ** b

"""
#Examples on integer

print("Addition :", 5+2)
print("Subtraction :", 5-2)
print("Multiplication :", 5*2)
print("Division :", 5/2)
print("Modulus :", 5%2)
print("floor division :", 5//2) #divison without remainder
print("Exponential :", 5**2) # means 5*5

#Example on float
print("floating number :", 6.9)
print(type(6.9))

#example on complex number 
print("complex number :",1+7j)
print(type(1+7j))

#declaring the variable and assigning the number data
a = 7
b = 1
print("total = ", a+b) #note sum is built in function so we here use total
print("subtraction = ", a-b)
print("multiplication = ", a*b)

#calculating area of circle
radius = 10
area_of_circle = 3.14 *radius ** 2#two *means exponantial power
print("area of circle :", area_of_circle)

#calculating area of rectangle
length = 10
width = 20
area_of_rectangle = length * width
print(area_of_rectangle)

#calculating the width of an object
mass = 75 #in kg
gravity = 9.81
weight = mass * gravity
print(weight,'N') # 'n' units of weight

#calculating the density of liquid
mass = 75 #in kg
volume = 0.075 #in cubic
density = mass/volume 

#COMPARISION OPERATOR

"""
== 'equal'
!= 'Not equal'
> 'greater than'
< 'less than'
>= 'Greater than or equal to'
<= 'less than or eqeual to'
"""

print(3>2) #it gives result in boolean format
print(3>=2)
print(3<2)
print(3<=2)
print(3==2)
print(3!=2)
print(len("mango") > len("grapes"))
print("True == True :", True == True)
print("True == False :", True == False)
print("False == False :", False == False)

#In addition to the above comparison operator Python uses:
"""
is : Returns a true if both variables are the same object(x is y)
is not : Returns true if both variables are not the same object(x is not y)
in :Returns True if the quired list comtains a certain items(x in y)
not in : Returns True if the quired list contains a certain items(x in y)
"""
print("1 is 1 :", 1 is 1) #True because the data values are same
print("1 is 2 :", 1 is 2) #false 
print("1 is not 2 :", 1 is not  2) #true because 1 is not 2
print("A in Abhishek :", 'A' in 'Abhishek') #True A is found in the string

#LOGICAL OPERATOR
"""
Unlike other programming languages python uses keywords and,
or and not for logical operators.
Logical operators are used to combine conditional statements:

"and" - Returns True if both statements are True
"or" - Returns True if  one of the statement is True
"not" - Reverse the result, returns False if the result is true
"""
print(3>2 and 4>3) #returns in bool value true or false
print(3>2 and 4<2)
print("True and True :",True and True)
print(3>2 or 4>5) #returns true because one of the statement is  true
print(3>5 or 4>5) #returns false because both of two no one is true
print("True or False :", True or False)
print(not 3>2) #false  beacuse 3 >2 gives true, but 'not' gives false 
print(not True) #false beacuse of 'not'
print(not not False) #false