str1=input()
str2=input()
list1=list(str1)
list2=list(str2)
list3=list1.sort()
list4=list2.sort()
if list3==list4:
    print("Yes")
else:
    print("No")
