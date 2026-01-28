#输入一个字符串
#实现以下功能：
#统计字符串中字母、数字、空格、其他字符的数量
#将字符串中的所有数字提取出来组成一个新的字符串
#反转字符串（不能使用内置的reverse函数）
#找出字符串中最长的单词（假设单词由空格分隔）
text=input()

letter_count=0
digit_count=0
space_count=0
other_count=0

for ch in text:
    if ch.isalpha():
        letter_count+=1
    elif ch.isdigit():
        digit_count+=1
    elif ch.isspace():
        space_count+=1
    else:
        other_count+=1
print(f"字母：{letter_count},数字：{digit_count},空格：{space_count},其他：{other_count}")

digits=""
for ch in text:
    if ch.isdigit():
        digits+=ch
print(f"提取到的数字：{digits}")

#颠倒字符串
reversed_text=text[::-1]

words=text.split()
if words:
    longest_word=words[0]
    for word in words:
        if len(word)>len(longest_word):
            longest_word=word
else:
    longest_word=""


