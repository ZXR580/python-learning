s=input()
lst=[t for t in s if ord('0')<=ord(t)<=ord('9')
     or ord('a')<=ord(t)<=ord('f')
     or ord("A")<=ord(t)<=ord('F')]
news=''.join(lst)
print(int(news,16))
