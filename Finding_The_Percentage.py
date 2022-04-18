if __name__ == '__main__':
    n = int(input())
    li = []
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        li.append(name)
    query_name = input()

    for i in li:
        if i == query_name:
            ad = sum(student_marks[i])
            b = len(student_marks[i])
    avg = ad/b
    print('%.2f'%avg)
