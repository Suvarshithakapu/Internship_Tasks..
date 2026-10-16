## 17. https://www.hackerrank.com/challenges/finding-the-percentage/problem

n = int(input())
student_marks = {}
for i in range(n):
    line = input().split()
    name = line[0] # First word peru
    scores = list(map(float, line[1:])) 
    student_marks[name] = scores

query_name = input()
avg = sum(student_marks[query_name]) / 3
print(f"{avg:.2f}")