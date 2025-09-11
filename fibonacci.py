def fibonacci(n):
    if n<=0:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
for i in range(6):
    print(fibonacci(i))
