#1 Declare your age as integer variable
age = 21
print(type(age))

#2 Declare your height as a float variable
height = 5.7
print(type(height))

#3 Declare a variable that store a complex number
complx = (1 + 7j)

#4 Write a script that prompts the user to enter base and height of the triangle
#and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input("Enter the Base :"))
height = int(input("Enter the Height :"))
area_of_triangle = (0.5 *base*height)
print("Area of Triangle :", area_of_triangle)

#5 Write a script that prompts the user to enter side a, side b, and side c of the triangle.
#Calculate the perimeter of the triangle (perimeter = a + b + c).
s1 = int(input('Enter the side 1 :'))
s2 = int(input('Enter the side 2 :'))
s3 = int(input('Enter the side 3 :'))
perimeter = ( s1+s2+s3 )
print(perimeter)

#6
"""
 Get length and width of a rectangle using prompt. 
Calculate its area (area = length x width) 
and perimeter (perimeter = 2 x (length + width))
"""
l = int(input("Enter the length :"))
w = int(input("Enter the width :"))
area = (l*w)
perimeter = (2*l+w)
print("Area of Rectangle :",area)
print("Perimeter of Rectangle :",perimeter)

#7
"""
Get radius of a circle using prompt. Calculate the area (area = pi x r x r)
and circumference (c = 2 x pi x r) where pi = 3.14.

"""
pi = 3.14
r = int(input("Enter the radius of the circle :"))
area = pi * r **2
circumfrence = 2 * pi * r
print("The area of the circle :",area)
print(circumfrence)

#8
#Find the length of 'python' and 'dragon' 
# and make a falsy comparison statement.
print(len("python"))
print(len("dragon"))
print("dragon" == "python")

#9
#Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in "python" and 'on' in "dragon")
print(len("python"))

print(type('10') == type(10))
y = float('9.8')
z = 10
print(y == z)
