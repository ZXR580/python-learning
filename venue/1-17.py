# 1. studentid 字典（学号→姓名）
studentid = {
    "2023001": "张三",
    "2023002": "李四"
}

# 2. course_set 集合（所有课程）
course_set = {"数学", "英语", "物理"}

# 3. studentscore 字典（学号→成绩字典）
studentscore = {
    "2023001": {        # 张三的成绩字典
        "数学": "85",
        "英语": "90"
    },
    "2023002": {        # 李四的成绩字典
        "数学": "88",
        "物理": "92"
    }
}
# course_set 转成有序列表
coursename = list(course_set)  # ["数学", "英语", "物理"]

# 表头格式：学号,姓名,课程1,课程2,...,平均分
print("学号,姓名,", end="")
for course in coursename:
    print(course + ",", end="")
print("平均分")

for student_id in studentid.keys():
    # 输出学号和姓名
    print(f"{student_id},{studentid[student_id]},", end="")#student_id即循环输出字典key words

    # 获取该学生的成绩字典
    score_dict = studentscore.get(student_id, {}) #{}是if字典为空时返回的默认值
    total = 0
    count = 0

    # 按课程顺序输出成绩
    for course in coursename:
        if course in score_dict:
            grade = score_dict[course]
            print(f"{grade},", end="")
            total += int(grade)
            count += 1
        else:
            print(",", end="")  # 该课程没成绩，留空

    # 计算并输出平均分
    if count > 0:
        avg = total / count
        print(f"{avg:.1f}")
    else:
        print("0.0")