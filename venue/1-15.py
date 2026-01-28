n = int(input())
a=[]
for i in range(0,n):
    b=input().split()
    a.insert(i,b)

c=[]
d=[]
for i in range(0,n):
    maxa=max([int(a[i][j]) for j in range(n)])#同一行中，列max
    mina=min([int(a[k][i]) for k in range(n)])#同一列中，行min
    c+=[(i,j) for j in range if int(a[i][j])==maxa]
    d+=[(k,i) for k in range if int(a[i][j])==mina]

result=[]
for element in c:
    if element in d:
        result.append(element)

if result:
    print(*result[0])
else:
    print("None")