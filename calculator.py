from math import *


q = input('''What you want to do:
1 ceil
2 floor
3 round
4 divide 
5 multiply
6 subtract 
7 add
8 root
9 cube
10 square

''')

# Square a number

if q==("10"):
    a = input("Enter a number: ")
    a= float(a)

    print(pow(a,2))

# square root a number

if q==("8"):
    a = input("Enter a number: ")
    a= float(a)

    print(sqrt(a))


# Add a number
if q==("7"):
    num1=input("Enter first number ")
    numb2=input("Enter second number ")
    result = float(num1) + float(numb2)
    print("Here you go " , result )

# Subtract a number
if q==("6"):
    num1=input("Enter first number ")
    numb2=input("Enter second number ")
    result = float(num1) - float(numb2)
    print("Here you go " , result )

# Multiply a number
if q==("5"):
    num1=input("Enter first number ")
    numb2=input("Enter second number ")
    result = float(num1) * float(numb2)
    print("Here you go " , result )

# Divide a number
if q==("4"):
    num1=input("Enter first number ")
    numb2=input("Enter second number ")
    result = float(num1) / float(numb2)
    print("Here you go " , result )

# cube  of a number
if q==("9"):
    a = input("Enter your number: ")
    a = float(a)
    print(pow(a,3))
    
# To round off a number
if q==("3"):
    a = input("Enter your number: ")
    a = float(a)
    print(round(a))

# To ceil a number
if q==("1"):
    a = input("Enter your number: ")
    a = float(a)
    print(ceil(a))

# To floor a number
if q==("2"):
    a = input("Enter your number: ")
    a = float(a)
    print(floor(a))

    