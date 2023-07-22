#Conditionals
"""By default, statements in Python script are executed sequentially from top to bottom. If the processing logic require so, the sequential flow of execution can be altered in two way:

Conditional execution: a block of one or more statements will be executed if a certain expression is true
Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true. In this section, we will cover if, else, elif statements. The comparison and logical operators we learned in previous sections will be useful here.
"""

"""If Condition
In python and other programming languages the key word if is used to check if a condition is true and to execute the block code. Remember the indentation after the colon.

# syntax
if condition:
    this part of code runs for truthy conditions"""

a = 7
if a > 0 :
    print("Positive Number")
"""
 As you can see in the example above, 7 is greater than 0. The condition was true and the block code was executed. However, 
 if the condition is false, we do not see the result. In order to see the result of the falsy condition, we should have another block, 
 which is going to be else.

If Else
If condition is true the first block will be executed, if not the else condition will run.

# syntax
if condition:
    this part of code runs for truthy conditions
else:
     this part of code runs for false conditions"""

a = 7 
if (a > 7) :
    print("Number is greater than 7")
else :
    print("Number is 7")
    

# The condition above proves false, therefore the else block was executed. 
# How about if our condition is more than two? 
# We could use _ elif_.
"""If Elif Else
In our daily life, we make decisions on daily basis. We make decisions not by checking one or two conditions but multiple conditions. As similar to life, programming is also full of conditions. We use elif when we have multiple conditions.

# syntax
if condition:
    code
elif condition:
    code
else:
    code"""
a = 7
if (a >7):
    print("Numb is Greater than 7")
elif(a<7):
    print("Number is less than 7")
else:
    print("Number is equal to 7")

#SHORT HAND
# syntax
# code if condition else code
a = 3
print("A is postive integer") if a > 0 else print("A is negative number")

"""Nested Conditions
Conditions can be nested
# syntax
if condition:
    code
    if condition:
    code
"""
a = -3
if a > 0:
    if a % 2 == 0:
        print("Number is even and positive number")
    else:
        print("Number is Positive but not even")
elif a == 0:
    print("A is Zero")
else :
    print(" A is Negative Number")

"""We can avoid writing nested condition by using logical operator and.

If Condition and Logical Operators
# syntax
if condition and condition:
    code"""
a = int(input("Enter The Number : "))
if a > 0 and a % 2 == 0 :
    print("A is Poitive Number and Even Number ") 
elif a > 0 and a % 2 != 0 :
    print("A is Positive Number and  Odd Number")
elif a == 0 :
    print("A is Zero")
else :
    print("A is negative Number")

"""If and Or Logical Operators
# syntax
if condition or condition:
    code"""
user = str(input("Enter your Name :"))
access_level = 3
if user == "root" or access_level >=4:
    print("Access Granted !!!")
else :
    print("Access Denied !!!")