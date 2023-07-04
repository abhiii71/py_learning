#STRINGS
"""
Text is a string data type. 
Any data type written as text is a string.
Any data under single, double or triple quote are strings. 
There are different string methods and built-in functions to deal with string data types. 
"""
#some examples of string data type
a = "Abhishek" #it is a string data type
print(a)
print(len(a))
z = "This is also string data type"
print(z)
print(type(z)) # here you can see

me = ''' this is called the 
         multi
         line
         string.
   '''
print(me)
print(type(me))

em = """ this is 
also called
the multiline
string
"""
print(em)
print(type(em))

#STRING CONCATINATION
# We can connect strings together.
# Merging or connecting strings is called concatenation.
z1 = "hello"
y1 = "abhii"
zy = z1 +y1
print(zy) 

#ESCAPE SEQUENCES IN STRINGS
"""
\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")
"""
print('I think this 30 days of python series would be helping in learning python\n is not it?') #line break after 'python'
print('Days4 \tTopic\tStrings') #after day4 there's a space of 4 or 'tab'
print('this is blackslash symbol (\\)')
print('you can start learning from open source \"Free, Amazing!!!\"')

#STRING FORMATTING
"""
# Old Style String Formatting (% Operator)
In Python there are many ways of formatting strings. 
In this section, we will cover some of them. 
The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), 
together with a format string, which contains normal text together with "argument specifiers", 
special symbols like "%s", "%d", "%f", "%.number of digitsf".

%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision
"""
f1 = "Abhii"
f2 = "here"
lang = "python"
OldStringType = "Hey viewer,  Am %s %s .\nI am learning %s nowadays" %(f1,f2,lang)
print(OldStringType)

#STRINGS AND NUMBERS
# r = 10 #theres some error i'll resolve it later on
# pi = 3.14
# area = pi * r ** 2
# FormatedString = "The area of the circle with radius %d is %.2f." %(r,area) #here 2 means 2 significant digit after the point
# print(FormatedString)

py_lib = ['Django','flask','Numpy','Matplotlib','Pandas']
formated_string = 'The following are python liberaries : %s' %(py_lib)
print(formated_string)

#New Style String Formatting(str.format)
# this formating is introduced in python3
f1 = "Abhishek"
f2 = "Verma"
lang = "python"
formated_string = "I am {} {}. I learned {}".format(f1,f2,lang)
print(formated_string)

a=2
b=3
print('{} + {} = {}'.format(a,b, a+b))

#STRING INTERPOLATION/f-String(Python 3.6+)

#Another new string formatting is string interpolation, f-strings. 
# Strings start with f and we can inject the data in their corresponding positions.
a = 4
b = 3
print(f'{a} + {b} = {a+b}')

name = (input("Enter your name :"))
age = int(input("Enter your age :"))
print(f'My name is {name} and  i am {age} years old') 

#PYTHON String as Sequence of characters
"""
Python strings are sequences of characters, 
and share their basic methods of access with other Python ordered sequences of objects – lists and tuples. 
The simplest way of extracting single characters from strings (and individual members from any sequence) is to unpack them into corresponding variables.
"""
#unpacking charcters
lang = "Python"
a,b,c,d,e,f = lang #unpacking sequence character into variables
print(a)

#ACCESSING CHARACTERS IN STRINGS BY INDEX
"""
In programming counting starts from zero. 
Therefore the first letter of a string is at zero index and the last letter of a string is the length of a string minus one.
"""
lang = "python"
first_letter = lang[1]
print(first_letter)
last_index = len(lang) - 1
last_letter = lang[last_index]
print(last_letter)

#If we want to start from right end we can use negative indexing. -1 is the last index.
lang = "python"
last_letter = lang[-1]
print(last_letter)
second_last = lang[-2]
print(second_last)

#SLICING PYTHON STRINGS
#In python we can slice strings into substrings.
lang = "Python"
first_three = lang[0:3] #starts at 0 index and upto 3 but not include 3
print(first_three) #pyt
last_three = lang[3:6]
print(last_three)#hon

#REVERSE THE STRING
py = "Hey, am coming just wait !!!"
print(py[::-1]) #!!! tiaw tsuj gnimoc ma ,yeH - reverse the order

#Skipping the Character while slicing
#It is possible to skip characters while slicing by passing step argument to slice method.
lang = "Python"
pto = lang[0:6:2]
print(pto) #Pto

#STRING METHODS
#capitalize(): Converts the first character of the string to capital letter
cap = 'first character will be capitalized in this'
print(cap.capitalize())#First

#count()
itcounts = 'this will count how many times a word came'
print(itcounts.count('i')) #3 means 'i' comes three time
print(itcounts.count('t')) # 3

#endswith() #gives result in true or false
lang = "abhishek wants to become a DevRel"
print(lang.endswith("Rel"))
print(lang.endswith("wants"))
print(lang.endswith("DevRel"))

#expandtabs() : Replaces tab character with spaces, default tab size is 8. It takes tab size argument
nw = 'i am very\tpassionate about \tcloud\tlinux'
print(nw.expandtabs())
print(nw.expandtabs(5))

#find(): Returns the index of the first occurrence of a substring, if not found returns -1
ab = "is DevRel and Developer Advocate both are same?"
print(ab.find('D')) #3
print(ab.find('z')) #its not present so it returns -1

#rfind() #similar as find but it start searching from last
# : Returns the index of the last occurrence of a substring, if not found returns -1
sq = "i visulize i speaking at big confresses and everyone listen me out"
print(sq.rfind('e')) #i think maybe it doesn't work perfectly

#format() :formats strings into a nicer output
f1 = "Abhishek"
f2 = "Verma"
age = 21
cont = 'I am {} {}. I am {} years old.'.format(f1,f2,age)
print(cont)



