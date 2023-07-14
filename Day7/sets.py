#SETS
"""
Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson. 
The Mathematics definition of a set can be applied also in Python. 
Set is a collection of unordered and un-indexed distinct elements. 
In Python set is used to store unique items, 
and it is possible to find the union, intersection, difference, symmetric difference, subset, 
super set and disjoint set among sets.
"""
#Creating a Set
# we use set() built-in-function
# creating a empty set
st = set()

# creating a set with initial items
st = {"me",71,True}
print(st)
print(type(st))
print(len(st))

"""
Checking an Item
To check if an item exist in a list we use in membership operator.
"""
itm = {"Abhii","DevOps","Engineer"}
print("Does 'DevOps' exists in item list :","DevOps" in itm)

# Adding Items to a Set
"""Once a set is created we cannot change any items but we can add additional items.

Add one item using add()"""
itm = {"firse","idhar","kuch likhna","Hoga"}
itm.add("Hna") #randomly added to anywhere
print(itm)

"""Add multiple items using update() The update() 
allows to add multiple items to a set. The update() takes a list argument."""
itm = {"Adding","Multiple","things"}
updatd = ("Abhi","Kya","Kar rha", "hai")
itm.update(updatd)
print(itm)

#Removing items from a set
"""We can remove an item from a set using remove() method. 
If the item is not found remove() method will raise errors, 
so it is good to check if the item exist in the given set. 
However, discard() method doesn't raise any errors."""
ft = {"this","can","be","removed"}
ft.remove("removed")
print(ft)

# The pop() methods remove a random item from a list and 
# it returns the removed item.
pp = {"one","can","be","removed"}
pp.pop() 
print(pp)
# If we re interested in the removed item.
removed_itm = pp.pop()
print(removed_itm)

#Clearing an item into set
# if we want to clear or empty the set we use clear method.
st = {"this","is","a","set"}
st.clear()
print(st)

# Deleting a set
# If we want to delete the set itself we use del operator.
any_set = {"I am","going","to delete","this set"}
del any_set 
# print(any_set)

# Converting List to Set
"""We can convert list to set and set to list. 
Converting list to set removes duplicates and only unique items will be reserved.
# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered
"""
lst = ["List","List","can be","duplicate","but","set cannot"]
print(lst)
cset = set(lst)
print(type(cset))
print(cset)

# Joining Sets
# we can join two sets using the union() or update()
"""Union This method returns a new set
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
"""
st1 = {"this","is","first"}
st2 = {"this","is","second"}
print(st1.union(st2))

"""Update This method inserts a set into a given set
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1"""
st1 = {"st1","conatins","love"}
st2 = {"st2","conatins","care"}
st1.update(st2)
print(st1)

"""
Finding Intersection Items
Intersection returns a set of items which are in both the sets. See the example

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}"""
me = {"calm","peace","Deep water"}
you = {"crazy","duck","peace","fool"}
us = me.intersection(you)
print(us)

"""
Checking Subset and Super Set
A set can be a subset or super set of other sets:

Subset: issubset()
Super set: issuperset
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
"""
set1 ={1,2,3,4,5}
set2 = {1,2,3,4}
set12 = set1.issubset(set2)
set21 = set2.issubset(set1)
print(set12) #false
print(set21) #true
ss = set1.issuperset(set2)  # set2 is superset of set1
print(ss) #True

"""
Checking the Difference Between Two Sets
It returns the difference between two sets.

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2"""
st1 = {1,2,3}
st2 = {2,3,}
diff =st1.difference(st2)
diff2 = st2.difference(st1)
print(diff)
print(diff2) #means nothing different

"""Finding Symmetric Difference Between Two Sets
It returns the the symmetric difference between two sets. It means that it returns a set that contains all items from both sets, except items that are present in both sets, mathematically: (A\B) ∪ (B\A)

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}"""
st1 = {1,2,3,4,5}
st2 = {1,2,3}
sdf = st1.symmetric_difference(st2)
print(sdf)


"""Joining Sets
If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method.

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False"""
evn = {2,4,6,8}
od = {1,3,7,9}
dj = evn.isdisjoint(od)
print(dj)