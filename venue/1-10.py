s=0
cnt=0
while True:
    x=int(input())
    if x!=-1:
        s+=x
        cnt+=1
    else:
        break
if cnt>0:
    print(s/cnt)
else:
    print(0)

