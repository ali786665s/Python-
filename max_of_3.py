def max_of_3(x,y,z):
    if x>y and x>z:
        return x
    
    elif y>x and y>z:
        return y
    
    elif z>y and z>x:
        return z
    
    else:
        print("Make sure the inputs are valid.")





    
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
third = float(input("Enter third number: "))

result = max_of_3(first,second,third)
print(f"The max of all values is {result}")