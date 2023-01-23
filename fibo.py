def fib2(n):
    a, b = 0,1
    if n >= 1:
        for i in range(n):
                a, b = b, a+b
        print(a)
    else:
        if n <= 1:
            print(n)


#valor = int(input())
fib2(int(input()))
