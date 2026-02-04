def fibonacci(term):
    num2 = 0
    num1 = 1
    numStore = 0
    for i in range(1, term+1):
        numStore=num1
        num1 = num1 +num2
        num2= numStore
    print(num1)
fibonacci(5)
fibonacci(10)
fibonacci(15)