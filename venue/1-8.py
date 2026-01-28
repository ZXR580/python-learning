weight=(7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2)
trans=('1','0','x','9','8','7','6','5','4','3','2')

n=int(input())
count=0 #错误的个数
for i in range(n):
    s=input()
    lst=list(s)
    check=[lst[i] for i in range(len(lst))  if ord(lst[i]) in range(ord('0'),ord('9'))]
    if len(check)<17:
        print(s)
        count+=1
    else:
        total=sum([int(lst[i])*weight[i] for i in range(17)])
        res=total%11
        if trans[res]!=lst[17]:
            print(s)
            count+=1
if count==0:
    print("ALL PASSED")