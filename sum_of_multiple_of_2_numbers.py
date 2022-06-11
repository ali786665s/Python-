total = 0

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))



for x in range(1,1000):
    if x%num1 ==0 or x%num2 ==0:
        total += x

print(total)

