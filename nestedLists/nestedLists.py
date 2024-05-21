if __name__ == '__main__':
    students = []
    lowest =[]
    for _ in range(int(input())):
        name = str(input())
        score = float(input())
        students.append([name, score])

    print(students)