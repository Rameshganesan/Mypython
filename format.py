if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    student_avg = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        #print(scores)
        scores = map(float, scores)
        #print(scores)
        student_marks[name] = scores
        student_avg[name] = sum(scores)/len(scores)
    query_name = raw_input()
    print("{:.2f}".format(student_avg[query_name]))