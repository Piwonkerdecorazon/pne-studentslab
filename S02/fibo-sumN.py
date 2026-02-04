def fibosum(term):
    num2 = 0
    num1 = 1
    numStore = 0
    numbers = []
    result = 0
    for i in range(1, term+1):
        numStore=num1
        num1 = num1 +num2
        num2= numStore
        numbers.append(num1)
    for i in range (0,term):
        result += numbers[i]
    return result
print(fibosum(5))
print(fibosum(10))