## 6. https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = int(input())
arr = list(map(int, input().split()))
arr = sorted(set(arr))
if len(arr) >= 2:
    print(arr[-2])


