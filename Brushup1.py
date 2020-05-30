import cv2
import math

print("Hi Richard\n")

result = math.gcd(2,3)
print(result)

# Some Basic Calculations which will give us understanding about operators

a = 45
b = 'Richard'
c = 56.23
d = 2

print(a+c)
print(c - d)
print(d * a)
print(a/d)
print(a**c) # Exponentiation Operator
print(a % d) # Floor division Opertor
print(c // d) # Modulo Operator



# richard project = 7
# print(richard project)

# Rules for creating variables
# 1.  Variables should start with a letter or an underscore
# 2. Variables cannot start with a number 
# 3. It can only contain alpha numeric characters
# 4. Variable names are case sensitive means Richard and richard are two different variables

# To find out the data types of a variable we make use of type() function

typeA = type(a)
typeB = type(b)
typeC = type(c)
typeD = type(d)

print(typeA)
print(typeB)
print(typeC)
print(typeD)

# Type Casting

e = '45'
print(type(e))

# suppose I want to add the value of e with a then we need to type cast the variable

e = int(e)
f = e+a
print(f)
print(type(e))

# More about strings

info = ''' Richard is a
software developer
'''
print(info)

# the above is a way of writing strings

# Accessing characters of a string

name = "Richard"
print(name[0])

# In python indexing starts from 0 
# we can also use slicing method to access the variables string 

print(name[0:3])

# Means starts at index 0 and terminate or do not include 3

print(name[1:10])
print(name[2:10])
print(name[3:10])
print(name[4:10])
print(name[5:10])
print(name[6:10])

# use of strip function

surname = " saldanha "
print(surname)

print(surname.strip()) 

# Above code will remove the void spaces in them

# To know about the length of the string we simply use the len() functon

print(len(name))
print(len(surname)) #Includes the space as one character at a time so in this case length of the string surname is 10

# use of uppercase and lowercase functions of a string

var1 = name.upper()
print(var1)

surname_new = "SALDANHA"
var2 = surname_new.lower()
print(var2)

# Use of Replace function

names ="Sammy, Leroy, Lenni, Jackie, Rach"
print(names)

var3 = names.replace(', ', '\n')
print(var3)

var4 = names.replace("S", "T")
print(var4)

var5 = names.replace("T","S")
print(var5)

var6 = names.replace("Rach","Racheal")
print(var6)

# Next, use of Place holders and format functions in a string which is a very useful feature

place = "Doha"
surname = "Saldanha"

Aboutme = "Hello, my name is {} {} and these are my friends name: {} who live in {}".format(name,surname,names,place)
print(Aboutme)

# Note we can also specify inside the {} as the index but it is not required as python understands that we want to start it from 0
# Suppose if we want to add index then we can specify it as {0}, {1} but the sequence does not matter.We can give it as 

Aboutme1 = "Hello, my name is {1} {0} and these are my friends name: {2} who live in {3}".format(name,surname,names,place)
print(Aboutme1)

# this is another way to this approach which can be used by making use of 'f' string function made available only at higher versions of
#  python, python 3 onwards so observe the below

Aboutme2 = f"Hello, my name is {name} {surname} and these are my friends name: {names} who live in {place}."
print(Aboutme2)

'''
Python Collections
1. List
2. Tuple
3. Set
4. Dictionary
'''

# 1. List

lst1 = [56,25,4,41,3,17]
print(lst1)
print(type(lst1))

# Note: Anything we create in python is an object which belongs to some or the other class.

# Accessing elements of a list

var7 = lst1[0] # Can be accessed using the index of the list
print(var7)

var8 = lst1[1:5] # Can be accessed by this method as well
print(var8) 

# note: We can not only access the elements of a list but also we can change the elements of the list

lst1[2] = 45
var9 = lst1
print(var9)

# use of append and len function in list

var10 = len(lst1)
print(var10) 

var11 = lst1.append(456)
print(lst1)

# Append an element at a specific index we use the insert function

lst1.insert(1,105)

var12 = lst1
print(var12)

# Use of remove, pop and del function useful in list

print(lst1)
lst1.remove(3) # We need to specify the element of a list not the index of the list

var13 = lst1
print(var13)

var14 = len(var13)
print(var14)

var15 = lst1.pop()
print(var15)

print(lst1)

del lst1[2] # Here we need to specify the index of the list not the element of the list

print (lst1)

# There is another function which is clear we can use if we want to clear the elements of a list.

lst2 = [1,7,3,5]
lst2.clear()
print(lst2)
abc = lst2
print(abc)

# 2. Tuple -> The elements of a tuple cannot be changed

days = ("Mon","Tues","Wed","Thurs","Fri")
print(days)
len(days)
var16 = print(type(days))

# days[0] = "Monday" Not applicable
# However we can do type casting

var17 = list(days)
print(var17)
print(type(var17))

var17[0] = "Monday"
print(var17)

# SET Non Repetative elemnts

s1 = {1,7,7,1,2,23,56,23,45,63,45,23,7,1,178,123,41,41,7423,5,8,5}
print(type(s1))
print(len(s1))
s1.add(963214578)
print(s1)
s1.update([1,5,7,8,7,34567890])
print(s1)

#  We can also remove elements from the set

s1.remove(7)
print(s1)

s1.discard(956213) # It means that if the element is present discard it otherwise just return the set without throwing an error.
print(s1)

# We can also use pop, del, clear function with sets.

s2 = {1,1,4,56,3,5,2,5,0,4}
del s2
#print(s2) # When we print it s2 will not appear.

s3 = {4,5,7,'asd'}
print(s3)
print(type(s3))
print(len(s3))
s3.pop()
print(s3)

# Dictionary: Present in a key value pair format. we need to specify the key to access its value.

RichDict = {"Name": "Richard",
             "Surname": "Saldanha",
             "Age": 25,
             "Country": "India",
             1: "abc"               
            }
print(RichDict)
print(type(RichDict))
print(len(RichDict))
RichDict[1] = "One"
print(RichDict)
RichDict.pop(1) # Here we have to specify the key
print(RichDict)
# del RichDict used to delete the dictionary
RichDict.update({"Pi value":3.147 , "Course":True})
print(RichDict)
print(type(RichDict))

# Conditional Statements in Python

# use of if, elif and else conditions in python

# update the dictionary if the value entered by the user matches with the ditionary value of Pi

user_Pi_value = input("Please enter the value of Pi: ")
user_Pi_value = float(user_Pi_value)
if RichDict['Pi value'] > user_Pi_value:
    print("You cannot update the dictionary")
    RichDict.update({"Status":"Did not update successfully"})
    print(RichDict)
elif RichDict['Pi value'] == user_Pi_value:
    RichDict['Pi value'] = user_Pi_value
    RichDict.update({"Status": "Updated Successfully"})
    print(RichDict)
else:
    print("TRY again")


# Use of Loops in Python

# Print all numbers between 1 to 100 which are all even numbers taking the input from the user

user_input = input("Enter your choice of number: ")
user_input = int(user_input)
if user_input < 100 and user_input > 0:
    print("Even Numbers:")
    for user_input in range(user_input,100):
        if user_input % 2 == 0:
            print(user_input, end=" ")
else:
    print("Entered input number does not fall in the range.")

# Given an  input from the user create a dictionary when the user enters the correct number of days in  a week.
print(' \n')
number_of_days = input("Enter number of days:")
number_of_days = int(number_of_days)
if number_of_days > 7 or number_of_days < 0:
    print("Please Enter correct number of days for a week.")
else:
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_dict = {}
    keys = range(number_of_days)
    for i in keys:
        day_dict[i] = days[i]
    print(day_dict)
    #print(type(day_dict))

# Trial and Error
    # print(days[0])
    # print(type(days))
    # #counter = 1
    # day_dict = dict()
    # for val in days:
    #     for ele in range(int(val), int(val)+2):
    #         day_dict.setdefault(ele, []).append(val)
    # print(day_dict)
    #values = ["Hi", "I", "am", "John"]

    # while counter < 7:
    #     #print(days[0])
    #     day_dict = {counter: days[0], counter: days[1], counter: days[2], counter: days[3], counter: days[4], counter: days[5], counter: days[6]}
    #     counter = counter + 1
    #     print(day_dict)
    # myDict = dict()
    # # # Creating a list 
    # valList = ['1', '2', '3'] 
  
    # # Iterating the elements in list 
    # for val in valList: 
    #     for ele in range(int(val), int(val) + 2):  
    #         myDict.setdefault(ele, []).append(val)  
  
    # print(myDict)



    # while number_of_days < 7:
    #     days_dict = {number_of_days: days[0], number_of_days: days[1]}
    #     number_of_days = number_of_days + 1
    #     print(days_dict)  
    

    #number_of_days = 0
    # while number_of_days < len(days):
    #     days_dict = {number_of_days: days}
    #     print(days[number_of_days])
    #     number_of_days = number_of_days + 1

    # counter = 0
    # for counter in days:
    #     counter = int(counter) + 1
    #     day_count = [counter[]]
    #     print(day_count)

    # for days[number_of_days] in le:
  

# Functions in Python

myname = input("Please Enter your Name: ")
def greetings(myname):
    print("HI", myname)
    print(len(myname))

greetings(myname)

num1 = input("Enter the first number: ")
num1 = float(num1)
num2 = input("Enter the second number: ")
num2 = float(num2)
option = input("Enter your option: ")
option = int(option)
def Calculator(num1, num2, option):
    if option == 1:
        add = num1 + num2
        output1 = "The additon of two numbers {} and {} are {}".format(num1,num2,add)
        print(output1)
    elif option == 2:
        sub = num1 - num2
        output2 = "The Subtraction of two numbers {} and {} are {}".format(num1,num2,sub)
        print(output2)
    elif option == 3:
        mul = num1 * num2
        output3 = "The Multiplication of two numbers {} and {} are {}".format(num1,num2,mul)
        print(output3)
    elif option == 4:
        div = num1 / num2
        output4 = "The Division of two numbers {} and {} are {}".format(num1,num2,div)
        print(output4)
    elif option == 5:
        mod = num1 % num2
        output5 = "The Modulus of two numbers {} and {} are {}".format(num1,num2,mod)
        print(output5)
    elif option == 6:
        expo = (num1**num2)
        output6 = "The Exponentiation of two numbers {} and {} are {}".format(num1,num2,expo)
        print(output6)
    else:
        print("Please Enter a proper option: ")
    

Calculator(num1,num2,option)

# Object oriented concepts in Python

# Note: Python is object oriented programming language

# Python is basically an object oriented programming language

# Here Class is basically a template from which mutiple classes can be created.

class MyDetails:
    def __init__(self,mname,mage):
        self.name = mname
        self.age = mage

Richard = MyDetails('Richard Saldanha', 24)
print(Richard.name)
print(Richard.age)



    


