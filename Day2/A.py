#  Variables, Builtin Functions
"""
most commonly used Python built-in functions are the following: 
print(), len(), type(), int(), float(), str(), input(), list()
, dict(), min(), max(), sum(), sorted(), open(), file(), help(), and dir()
"""

#  Number at the beginning, special character,
#  hyphen are not allowed when naming a variable. 
# A variable name cannot start with a number Variable names are case-sensitive
#   underscore is required when the variable name is more than one word.

# # Variable in python

first_name = "Abhishek"
# The equal sign is an assignment operator.
#  Assigning means storing data in the variable.
#  The equal sign in Python is not equality as in Mathematics.
last_name = "Verma"
country = 'India'

print(first_name,last_name,"from",country)
# Print function takes unlimited number of arguments.
my_info = {
    "from" : "Himachal Pradesh",
    "Yob" : "2001"
}
print(my_info)
print("First Name : ",first_name)
print(len(first_name))

# Declaring multiple variable in a line

first_name,last_name,age,country,interest,is_it_True = "Abhishek","Verma",21,"India","Cloud",True
print(first_name,last_name,age,country,interest,is_it_True)

#getting user input using the input() built-in function
name = input("What's Your Name  :")
age = input("How many years old are you :")
print(name,age)

# Data Types
print(type(10))
print(type(1 + 1j))
print(type(True))
print(type([1,2,3,4,5]))
print(type({'name' : 'Abhishek','age' : 21}))
print(type((1,2)))
print(type(zip([1,2],[3,4])))

# Type cating
'''
Converting one data type to another data type.
 We use int(), float(), str(), list, set 
 When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error. 
 If we concatenate a number with a string, the number should be first converted to a string.
'''

#int to float
num1 = 7 
print('integer :',num1)
float1 = float(num1)
print('floating number :',float1)

#float to int
float2 =  6.8
print('floating number :',float2)
int2 = int(float2)
print(int2)

# integer to string
num3 = 21
print(num3)
num3str = str(num3)
print(num3str)

#str to int or float
strz = '71'
print(strz)
intz = int(strz)
print(intz)
print(float(strz))


# str to list
stry = "Abhishek Verma"
print(list(stry))
