def lcm(a,b):
    a=int(input())
    b=int(input())
    if a>b:
        min=a
    else:
        min=b
    while(1):
        if min%a==0 and min%b==0:
            lcm=min
        min+=1
    return lcm
print(lcm(10,20))
