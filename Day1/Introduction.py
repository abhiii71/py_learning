# 1st day 27th June 2023

#you can run python in  terminal with - $python3 

# Single Line Comment with '#'

# Multiline Comment

"""This is multiline comment
multiline comment takes multiple lines.
python is eating the world
"""

# DATA TYPES

a = 1 #this is integer 
print(a) 

b= 3.5 #this is floating no.
print(b)

c = "helloabhii" # this is a string
print(c)

#boolean true or false

# LISTS

#Python list is an ordered collection which allows to store different data type items.
# A list is similar to an array in JavaScript.

d = [a,1,2.5,-1,True] # you can type only 1 data type or multiple data type also
print(d)

#DICTONAIRES

# A Python dictionary object is an unordered collection of data in a key value pair format.

f = {
    'name' : 'Abhii',
    'profession' : 'cloud engineer',
    'age' : 21
}
print(f)

#TUPLES

# A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. 
# They are immutable.

g = ('Abhii', 'verma',21,True)
print(g)

#SET
#A set is a collection of data types similar to list and tuple.
#  Unlike list and tuple, set is not an ordered collection of items. Like in Mathematics,
#  set in Python stores only unique items.
#order is not imp in set

h = {2,2,5,6,7}
hi ={ 3, 31,1,41,2,5,33} 
# if data is unordered it automaticallly conerted into ordered
print(h)
print(hi)

#CHECKING DATA TYPES
#TO DATA TYPE WE USE 'type' function

print(type(h)) #like this

#to run this  file use - $python3 A.py
