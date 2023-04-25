def fib(n):
    if n<=0:
        print('invalid number')
    if n==1:
        print(0)
        return -1
    if n==2:
        print(1)
        return -1
    count=3
    a=0
    b=1
    while count<=n:
        next =a+b
        a=b
        b=next
        count+=1
    print(next)
fib(9)