#Lists
"""
There are four collection data types in Python :

List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.

"""
#A list is collection of different data types which is ordered and modifiable(mutable).
#A list can be empty or it may have different data type items.

# Built in method
lst = list()
print(len(lst))
print(lst) #this is an empty list

#using Square bracket
lst = [] #this is also a empty list
print(lst)

lst = [1,"abhi",True,2.23,] #list can be store different data types
print(lst) #list either be of same data type of differnt type
print(len(lst)) #to get the length of list

#to get the index of the list 
idx = lst[0] 
print(idx)
lstidx = len(lst) -1
print(lstidx) #to  get the last indx of the list

# Accessing List Items Using Negative Indexing
#Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item.
ch = [71,"abhii",True,"Hai"]
print(len(ch)) #to get length the next put negative sign to that length to get 1st element
st = ch[-4] #to get the 1st element 
print(st)
last = ch[-1] #getting the last index
print(last)

# Unpacking List Items
ch = ["Abhishek",21,True,"single","LOL"]
fst,scnd,thrd,*rest = ch
print(fst)
print(rest)

#another ex
fst,sncd,thrd,four,five,*rest = ["Abhishek",2,3,4,5, "True Hai Ji"]
print(fst)
print(rest)

# Slicing Items from a List
"""
Positive Indexing: We can specify a range of positive indexes by specifying the start, 
end and step, the return value will be a new list. (default values for start = 0, end = len(lst) - 1 (last item), step = 1)
"""
fruits = ["Apple","Orange","Banana","Grapes"]
print(len(fruits))
print(fruits[:4]) #returns all items
print(fruits[-4:])#returns all items also
print(fruits[0:4]) #same result
print(fruits[1:4]) #0 excluded here
print(fruits[1:]) #againn 0 excluded
print(fruits[::2]) #it will take only 1st and 3rd item

#negative indexing
print(fruits[-4:]) # returns all items
print(fruits[::-1]) #get items in reverse order
print(fruits[::-4]) #only prints the last item of the list

#modifying the list
#List is a mutable or modifiable ordered collection of items.
li = [1,"Himachal",True,]
li[0] = "Helloabhii"
print(li)



#Checking Items in a List
li = [1,2,3,4,5]
print(1 in li) # says true
ex = "one" in li
print(ex) #same as above

#Adding Items to a List
#To add item to the end of an existing list we use the method append().
#syntax
# lst = list()
# lst.append(item) 
frt = ['a','z',1,True]
frt.append("New One") #by this a new item added to the end of the list
print(frt)

#Inserting Items into a List
"""We can use insert() method to insert a single item at a specified index in a list.
Note that other items are shifted to the right. 
The insert() methods takes two arguments:index and an item to insert.
# syntax
lst = ['item1', 'item2']
lst.insert(index, item)
"""
frt =[1,2,"z"]
frt.insert(2,"Abhii") #by this abhii added in before "z"
print(frt) 

#Removing Items from a List
#The remove method removes a specified item from a list
# syntax
# lst = ['item1', 'item2']
# lst.remove(item)
frt = [7,3,1]
frt.remove(3) #it removes the 3 from the list
print(frt)

#Removing Items Using Pop
#The pop() method removes the specified index, 
#(or the last item if index is not specified):
#  syntax
# lst = ['item1', 'item2']
# lst.pop()       # last item
# lst.pop(index)
av =["abhi","himachal", "main", "rehta","hai"]
av.pop() #not giving any argu means last one pop
print(av)
av.pop(0)
print(av)

"""
Removing Items Using Del
The del keyword removes the specified index and 
it can also be used to delete items within index range. It can also delete the list completely
# """
# # syntax
# lst = ['item1', 'item2']
# del lst[index] # only a single item
frt = [69,71,68]
del frt[0] #deleted 69
print(frt)

#Clearing List Items
#The clear() method empties the list:
itm = [21,7,13,11]
itm.clear() #al items inside list cleared
print(itm)

#copying a list
"""
It is possible to copy a list by reassigning it to a new variable in the following way: 
list2 = list1. Now, list2 is a reference of list1, any changes we make in list2 will also modify the original, list1. 
But there are lots of case in which we do not like to modify the original instead we like to have a different copy. 
One of way of avoiding the problem above is using copy().
"""
a_s = [311,353]
ar = a_s.copy()
print(ar)

# Joining a list
# l3 = l1 + l2
# + operator
l1 = [311]
l2 = [343]
l3 = l1+l2
print(l3)

#Joining using extend() method The extend() method allows to append list in a list. See the example below.
l1.extend(l2)
print(l1) #both 311 and 343

#if you have three lists
l4=[1,2]
l5=[3,4]
l6=[5,6]
l4.extend(l5)
l4.extend(l6)
print(l4) #we get l4 + l5 + l6

#Counting Items in a List
#The count() method returns the number of times an item appears in a list:
a1 =[1,1,2,3]
print(a1.count(1))
a2 = [2,3,4]
print(a2.count(2))

#Finding Index of an Item
#The index() method returns the index of an item in the list:
fr = [1,2,3]
print(fr.index(3))

#Reversing a List
#The reverse() method reverses the order of a list.
hi =["out","of","context"]
hi.reverse()
print(hi)

# Sorting List Items
"""
To sort lists we can use sort() method or sorted() built-in functions. 
The sort() method reorders the list items in ascending order and modifies the original list. 
If an argument of sort() method reverse is equal to true, it will arrange the list in descending order.

sort(): this method modifies the original list
"""
abhi = ["spritual","calm","sincere","d2e"]
abhi.sort() #it sorted acc to a-z
print(abhi)

#sorted(): returns the ordered list without modifying the original list Example:
abhii = ["DevOps","DevRel","Developer Advocate","Cloud Engineer"]
print(sorted(abhii))