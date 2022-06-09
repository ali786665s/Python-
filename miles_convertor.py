def miles_to_km(miles):
    km = miles*1.6
    print("Your answer is ")
    return km

def km_to_miles(km):
    miles = km/1.6
    print("Your answer is ")
    return miles


q = input("What do you want to do \n 1)miles to km\n 2)km to miles ")
if q=="1":
    p = float(input("Enter number of miles: "))
    answer = miles_to_km(p)
    print(answer)

elif q=="2":
    p = float(input("Enter number of km: "))
    answer = km_to_miles(p)
    print(answer)

else:
    print("Invalid input ")

   

# q = float(input("Enter number of miles: "))

# answer = miles_to_km(q)
# print(answer)



