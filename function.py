from math import *

def bmi_calculator(weight,height,name):
    bmi = weight/(pow(height,2))
    if bmi<18.5:
        print("Your BMI is: ", bmi)
        return name.capitalize() + " is underoverweight"

    elif bmi>=18.5 and bmi<25:
        print(" Your BMI is: ",bmi)
        return name.capitalize()+("'s") + " weight is healthy"

    elif bmi>=25 and bmi<30:
        print(" Your BMI is: ",bmi)
        return name.capitalize() + " is overweight"

    elif bmi>30:
        print("Your BMI is: ", bmi)
        return name.capitalize() + " is obese"

    else:
        print("Please make sure your inputs are valid")


name = input("Enter your name: ")
weight = int(input("Enter your weight in KG: "))
height = float(input("Enter your height in meters: "))

result = bmi_calculator(weight,height,name)
print(result)

# 2c5bcb2eatad


    
