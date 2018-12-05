if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    currentScore = student_marks[query_name]
    avg = sum(currentScore) / len(currentScore)
    # 格式化浮点数，两位小数 %.2f
    # 整数 %d,补零%02d
    # 字符串 %s,十六进制 %x
    print('%.2f' % avg)
