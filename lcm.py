def lcm(a,b):
    if a>b:
        min=a
    else:   
        min=b
    while(1):
        if min%a==0 and min%b==0:
            lcm1=min
        min+=1
    return lcm1
print(lcm(10,20))    

