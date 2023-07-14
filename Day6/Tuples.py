# Tuples
"""
A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuples:

tuple(): to create an empty tuple
count(): to count the number of a specified item in a tuple
index(): to find the index of a specified item in a tuple
operator: to join two or more tuples and to create a new tuple
"""

#creating an empty tuple
tpl = ()
print(tpl)
# Creating a Tuple
tpl = ("This", "is","Tuple") #this is tuple
print(type(tpl))
print(len(tpl))
print(tpl[1])

#negative indexing
tpl = (1,2,3)
print(len(tpl))
print(len(tpl) -1)
print(tpl[-3]) #means first

#Slicing the tuples
#We can slice out a sub-tuple by specifying a range of indexes where to start and where to end in the tuple, 
#the return value will be a new tuple with the specified items.
tpl = ("Abhi","DevOps","Engineer")
all_itm = tpl[0:3] #includes all # here 3 means 3-1 
same = tpl[0:] #includes all
print(all_itm)
print(same)
print(tpl[1:])#means start from DevOps

#Range Of Negative Index 
tpl = (1,2,3)
all_itm = tpl[-4:]
print(all_itm)

#Changing tuples to list
"""
We can change tuples to lists and lists to tuples. 
Tuple is immutable if we want to modify a tuple we should change it to a list.
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
""" 
Himachal_tpl = ("Baba Balk Nath","Manikarn","Naina Devi","Jawala Devi")
print(Himachal_tpl)
Himachal_list = list(Himachal_tpl)
print(Himachal_list)
Himachal_list[0] = "Deotsidh Baba Balk Nath" #here we manipulate tuple by changing it into list
print(Himachal_list)
print(type(Himachal_list))

#Joining tuples
#we can joined two or more tuples using + operator

tpl1 = ("this", "is", "first")
tpl2 = ("and",)
tpl3 = ("this","is","second")
tpl4 = tpl1 + tpl2 + tpl3
print(tpl4)
print(type(tpl4))

#Deleting tuples
"""It is not possible to remove a single item in a tuple 
but it is possible to delete the tuple itself using del.
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1
"""
frt = ("This","all","can","be","deleted","at once","but not","single","single word or item")
# del(frt)
print(frt)