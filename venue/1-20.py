def perm(word):
    result = []
    if len(word)==1:
        result.append(word)
        return result
    else:
        for i in range(len(word)):
            newword=word[:i]+word[i+1:]
            newresult=perm(newword)
            for s in newresult:
                result.append(word[i]+s)
    return result

n=int(input())
s="".join([str(i) for i in range(1,n+1)])
for  s1 in perm(s):
    print(s1,end=" ")