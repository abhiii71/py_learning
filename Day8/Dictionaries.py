#DICTIONARIES
"""
A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

Creating a Dictionary
To create a dictionary we use curly brackets, {} or the dict() built-in function.

# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
"""
abhi = {
    "Who" : "Abhishek",
    "From" : "Himachal Pradesh",
    "Age" : 21
}
print(abhi)
print(len(abhi))
print(type(abhi))

"""
Accessing Dictionary Items
We can access Dictionary items by referring to its key name.

"""
dic  = {
    "one" : "ek",
    "two" : "do",
    "three" : "teen"
}
print(dic["one"])

"""
Accessing an item by key name raises an error if the key does not exist. 
To avoid this error first we have to check if a key exist or we can use the get method. 
The get method returns None, which is a NoneType object data type, if the key does not exist.
"""
dic  = {
    "one" : "ek",
    "two" : "do",
    "three" : "teen"
}
print(dic.get("two"))

"""
Adding Items to a Dictionary
We can add new key and value pairs to a dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
"""
dic  = {
    "one" : "ek",
    "two" : "do",
    "three" : "teen"
}
dic["four"] = ("chaar")
print(dic)

"""
Modifying Items in a Dictionary
We can modify items in a dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'
"""
dic  = {
    "one" : "ek",
    "two" : "do",
    "three" : "teen"
}
dic["three"] = ("GAYAB")
print(dic)

"""
Checking Keys in a Dictionary
We use the in operator to check if a key exist in a dictionary

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False
"""
dic  = {
    "one" : "ek",
    "two" : "do",
    "three" : "teen"
}
print(("one") in dic)

"""
Removing Key and Value Pairs from a Dictionary
pop(key): removes the item with the specified key name:
popitem(): removes the last item
del: removes an item with specified key name
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item
"""
dic = {"key hai" :"value hai","another":"one","Travis":"Scott"}
print(dic)
print(dic.pop("another"))
print(dic.popitem()) #removes last one
del dic["key hai"]
print(dic)

"""Changing Dictionary to a List of Items
The items() method changes dictionary to a list of tuples.

"""
dic = {
    "Key" : "Value",
    "One" : "One",
    "Two" : "Two"
}
print(dic.items())
#Clearing a Dictionary
# If we don't want the items in a dictionary we can clear them using clear() method
print(dic.clear())

"""
Deleting a Dictionary
If we do not use the dictionary we can delete it completely"""
dct = {
    "this" : "is a dictionarary","i will" : "delete this"
}
del dct
# print(dct) #it will print error when we excute this because it is delete by the last line
"""
Copy a Dictionary
We can copy a dictionary using a copy() method. Using copy we can avoid mutation of the original dictionary.

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
"""
dc = {
    "this is " : "going to be copied",
    "okay " : "Thats it"
}
dc_copy = dc.copy()
print(dc_copy)
"""
Getting Dictionary Keys  and Values as a List
The keys() method gives us all the keys of a dictionary as a list.
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
val = dct.values()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])
print(val)
"""
dc = {
    "how are" : "you",
    "my" : "friend"
}
keys = dc.keys()
val = dc.values()
print(keys)
print(val)