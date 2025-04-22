def fiboncci(n):
    a,b=0,1
    for _ in range(n):
        yield a
        a,b=b,a+b
print("First 10 Fibonacci numbers: ")
for num in fiboncci(10):
    print(num, end=" ")