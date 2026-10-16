## 16.https://www.hackerrank.com/challenges/nested-list/problem

n = int(input())
records = []
for i in range(n):
    name = input()
    score = float(input())
    records.append([name, score])
scores = sorted(set(s for i, s in records))
second_lowest = scores[1]
names = sorted([name for name, s in records if s == second_lowest])
for name in names:
    print(name)