def nfib(n):
    if n<=0:
        return -1
    if n==1:
        return 0
    if n==2:
        return 1
    return nfib(n-1)+nfib(n-2)
print(nfib(6))