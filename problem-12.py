## 12.https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
 
def average(array):
    return round(sum(set(array)) / len(set(array)), 3)
n = int(input())
arr = list(map(int, input().split()))
print(average(arr))