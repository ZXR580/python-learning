s=input()
lst=list(s)
result=[' ']*len(lst)
for i in range (len(lst)):
    if ord("0")<=ord(lst[i])<=ord("9"):
        result[i]=lst[i]
    else:
        continue
# 过滤掉空字符串
result = [c for c in result if c]  # 只保留非空字符
print(''.join(result))