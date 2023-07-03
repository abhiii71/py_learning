#INDEX() 
"""
Returns the lowest index of a substring, additional arguments
indicate starting and ending index (default 0 and string length - 1).
If the substring is not found it raises a valueError.
"""
ch = "thirty days of python"
sub_string = "t"
print(ch.index(sub_string)) #0
print(ch.index('d'))#0

#rindex()
"""
Returns the highest index of a substring, 
additional arguments indicate starting and ending index (default 0 and string length - 1)
"""
ch = "In nov 2023 am become DevRel"
print(ch.rindex("v")) #24

#isalnum() : checks alphanumeric character
ch = "am giving speech in front of thousands folks yeh !!!"
print(ch.isalnum()) #checks that both numeric and alphabetic  character present
v = "Everyone100ked"
print(v.isalnum()) #it check only in single word

#isalpha(): #note if space present it false automatcally
# Checks if all string elements are alphabet characters (a-z and A-Z)
ch = "thirty days of python"
print(ch.isalpha()) #false because of space
ch = "thirtydaysofpython"
print(ch.isalpha()) #true because of space

#isdecimal(): 
# Checks if all characters in a string are decimal (0-9)
ch = "123"
print(ch.isdecimal())

#isdigit(): 
# Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
ch = "30"
print(ch.isdigit())
ch = "thirty"
print(ch.isdigit())

#isnumeric(): 
# Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
num = "10"
print(num.isnumeric()) #true
num = "\u00BD" # ½
print(num.isnumeric())

#isidentifier(): 
# Checks for a valid identifier - it checks if a string is a valid variable name
ch = "6monthsplan"
print(ch.isidentifier()) #false
ch = "sixmonthsplan"
print(ch.isidentifier()) #true

#islower(): 
# Checks if all alphabet characters in the string are lowercase
ch = "Abhishek becomes very famous DevRel"
print(ch.islower())
ch = "abhishek becomes very famous devrel"
print(ch.islower())

#isupper(): 
#Checks if all alphabet characters in the string are uppercase
ch = "ASSAN HAI"
print(ch.isupper())

#join(): Returns a concatenated string
av = ["DevRel","Developer Advocate","Cloud Architecture"]
result = "".join(av)
print(result)

av = ["DevRel","Developer Advocate","Cloud Architecture"]
result = "Abhii".join(av)
print(result)

# #strip(): 
# # Removes all given characters starting from the beginning and end of the string
# ch = "i became a excellent DevRel"
# print(ch.strip("ba")) #isn't give correct result

#replace(): 
# Replaces substring with a given string
ch = "i am DevRel"
print(ch.replace("DevRel","Developer Advocate"))

#split()
#Splits the string, using given string or space as a separator
ch = "Abhishek Verma"
print(ch.split())

#title(): Returns a title cased string
ch = "developer advocate"
print(ch.title())

#swapcase(): 
#Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
ch ="abhishek verma" 
print(ch.swapcase())

#startswith(): Checks if String Starts with the Specified String
ch = "Developer Advocate Abhii"
print(ch.startswith("Dev"))