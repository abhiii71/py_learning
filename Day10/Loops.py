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