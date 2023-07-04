#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
a = "Thirty "
b = "Days "
c = "Of "
d = "Python"
e = a+b+c+d
print(e)

#Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
print(company)
print(len(company))

#Change all the characters to uppercase/lowercase letters using upper() method.
print(company.upper())
print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Cut(slice) out the first word of Coding For All string.
slic = company[7:-1] 
print(slic)

#Check if Coding For All string 
# contains a word Coding using the method index, find or other methods.
print(company.index("Coding"))
print(company.find("Coding"))
print(company.rfind("Coding"))

#Replace the word coding in the string 'Coding For All' to Python.
ch = "Coding For All"
aw = ch.replace("Coding","Python")
print(aw)

# Change Python for All to Python for Everyone using the replace method or other methods
s =  aw.replace("All","Everyone")
print(s)

#Split the string 'Coding For All' using space as the separator (split()) .
s = "coding for all"
print(s.split())

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
a = ["Facebook","Google","Apple"]
print(a.split())