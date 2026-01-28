x=int(input())
t=[1,2,3,4,5]
try:
    print(t[x])
    print("Hello")
except:
    print("NOT valied")
else:
    print("Nothing")
finally:
    print("anyway")
