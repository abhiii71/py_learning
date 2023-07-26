# Loops
"""
Life is full of routines. In programming we also do lots of repetitive tasks. 
In order to handle repetitive task programming languages use loops. 
Python programming language also provides the following types of two loops:
while loop
for loop
"""
"""while Loop
We use the reserved word while to make a while loop. 
It is used to execute a block of statements repeatedly until a given condition is satisfied. 
When the condition becomes false, the lines of code after the loop will be continued to be executed.

  # syntax
while condition:
    code goes here
"""
a = 0
while a < 5:
    print(a)
    a = a+1
    
"""
In the above while loop, the condition becomes false when count is 5. 
That is when the loop stops. If we are interested to run block of code once the condition is no longer true, 
we can use else.
 # syntax
while condition:
    code goes here
else:
    code goes here
"""
a = 7
while a < 12:
    print(a)
    a = a + 1
else :
     print(a)
# The above loop condition will be false when count is 12 and the loop stops, 
# and execution starts the else statement. As a result 12 will be printed.

"""
Break and Continue - Part 1
Break: We use break when we like to get out of or stop the loop.
# syntax
while condition:
    code goes here
    if another_condition:
        break"""

a = 71
while a < 78 :
    print(a)
    a = a + 1
    if a == 75:
        break
"""    
The above while loop only prints 71,72,73,74 but when it reaches 75 it stops.

Continue: With the continue statement we can skip the current iteration, and continue with the next:
  # syntax
while condition:
    code goes here
    if another_condition:
        continue"""

a = 69
while a < 77:
    if a ==71:
        a = a + 1
        continue
    print(a)
    a = a + 1
# The above while loop only prints 69,70,72,73,74,75 and 76 (skips 71).

# FOR LOOP
"""A for keyword is used to make a for loop, similar with other programming languages, but with some syntax differences. Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

For loop with list
# syntax
for iterator in lst:
    code goes here
 """
lst = ["Abhi","Keep Going","on"]
for lsts in lst:
    print(lsts)

#For loop with tuple
"""# syntax
for iterator in tpl:
    code goes here"""
no = (1,2,3,4)
for nos in no :
    print(nos)

"""
For loop with dictionary Looping through a dictionary gives you the key of the dictionary.
  # syntax
for iterator in dct:
    code goes here
"""
p1 = {
    "first_name" : "Abhishek ",
    "last_name" : "Verma"
}
for key in p1:
    print(key)

for key, value in p1.items():
    print(key, value)
    
"""
Loops in set
# syntax
for iterator in st:
    code goes here
"""
set1 = {"ABHISHEK","CIVO","AWS","fedora","Red Hat LINUX"}
for brands in set1:
    print(brands)

"""
Break and Continue - Part 2
Short reminder: Break: We use break when we like to stop our loop before it is completed.

# syntax
for iterator in sequence:
    code goes here
    if condition:
        break
"""
no1 = (1,2,3,4)
for no in no1:
    print(no)
    if no == 3 :
        break
"""In the above example, the loop stops when it reaches 3.
  # syntax
for iterator in sequence:
    code goes here
    if condition:
        continue

Continue: We use continue when we like to skip some of the steps in the iteration of the loop."""
no1 = (1,2,3,4,5)
for no in no1:
    print(no)
    if no == 3 :
        continue
    print("NExt Number should be",no +1) if no !=5 else print("loop's end") 
    #for short hand conditions need both if and else statements
print('outside the loop')

"""
In the example above, if the number equals 3, the step after the condition (but inside the loop) is skipped and the execution of the loop continues if there are any iterations left.

The Range Function
The range() function is used list of numbers. The range(start, end, step) takes three parameters: starting, ending and increment. By default it starts from 0 and the increment is 1. The range sequence needs at least 1 argument (end). Creating sequences using range
"""
lst = list(range(11))
print(lst) #prints 1-10 in list
st1 = set(range(0,11,2)) 
print(st1)

"""# syntax
for iterator in range(start, end, step):
"""
for number in range(11):
    print(number) #prints 1-10

"""
Nested For Loop
We can write loops inside a loop.
# syntax
for x in y:
    for t in x:
        print(t)
"""
person ={
    "name" : "Abhishek Verma",
    "Passion" : "Cloud Computing",
    "Age" : 21,
    "skill" : ["c","python","bash Scripting","sql","Networking"]
}
for key in person:
    if key == "skill":
        for skills in person["skill"]:
            print(skills)

"""For Else
If we want to execute some message when the loop ends, we use else.

# syntax
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')"""
for number in range(11):
    print(number)
else :
    print("Loop stops at",number)

"""Pass
In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors. Also we can use it as a placeholder, for future statements.
"""
for i in range(71):
    print(i)