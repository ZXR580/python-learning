import math
m,n=map(int,input().split())
count=0
for i in range(m,n+1,1):
    lst=[1]
    for k in range(2,int(math.sqrt(i))+1):
        if i%k==0:
            lst.append(k)
            if i//k not in lst:
                lst.append(i//k)
    if i==sum(lst):
        lst.sort()
        count+=1
        print(str(i)+"="+'+'.join(map(str,lst)))

if count==0:
    print("None")
