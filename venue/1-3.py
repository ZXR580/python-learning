# ✅ 正确版本
def student_grade_system():
    students = []

    print("请输入学生成绩（格式：姓名 成绩），空行结束：")
    while True:
        line = input().strip()
        if not line:
            break
        name, score = line.split()
        students.append((name, int(score)))

    # 检查是否有数据
    if not students:
        print("没有输入学生数据！")
        return  # 正确：在函数内部，与if对齐

    # 计算统计数据
    scores = [score for _, score in students]
    avg_score = sum(scores) / len(scores)
    max_score = max(scores)
    min_score = min(scores)

    # 找出不及格学生
    failed_students = [name for name, score in students if score < 60]

    # 按成绩降序排序
    sorted_students = sorted(students, key=lambda x: x[1], reverse=True)

    # 找出最高分和最低分对应的学生
    max_student = [name for name, score in students if score == max_score]
    min_student = [name for name, score in students if score == min_score]

    # 输出结果
    print(f"\n平均分: {avg_score:.1f}")
    print(f"最高分: {max_score} ({'、'.join(max_student)})")
    print(f"最低分: {min_score} ({'、'.join(min_student)})")
    print(f"不及格学生: {failed_students}")
    print("\n成绩排名:")
    for name, score in sorted_students:
        print(f"{name} {score}")


# 调用函数
student_grade_system()