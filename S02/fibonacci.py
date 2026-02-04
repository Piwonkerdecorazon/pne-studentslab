num2 = 0
num1 = 1
numStore= 0
print(num2)
print(num1)
for i in range(1, 12):
    numStore=num1
    num1 = num1 +num2
    num2= numStore
    print(num1)
