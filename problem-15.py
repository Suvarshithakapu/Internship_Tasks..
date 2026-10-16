## 15.https://www.hackerrank.com/challenges/word-order/problem

from collections import OrderedDict
n = int(input())
words = OrderedDict()
for i in range(n):
    w = input()
    words[w] = words.get(w, 0) + 1
print(len(words))
print(*words.values())