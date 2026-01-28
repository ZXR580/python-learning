 #矩阵转置
lst=[[row*3+col+1 for col in range(3)]for row in range(3)]
print(lst)
lst1=[[row[col] for row in lst] for col in range(3)]
print(lst1)