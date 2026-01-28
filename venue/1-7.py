students=[(31820,"赵子龙"),(31821,"张飞"),(31822,"关羽"),(31823,"刘备"),(31824,"诸葛亮")]
for row in students:
    print(row[0],row[1])
    print()
for id,name in students:
    print(id,name)
    print()
for index in range(len(students)):
    print(students[index][0],students[index][1])
    print()