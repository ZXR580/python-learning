n=int(input())
for a in range(10**(n-1),10**n):
    if a==sum([int(i)**n for i in str(a)]):
        print(a)