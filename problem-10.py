## 10.https://www.hackerrank.com/challenges/find-a-string/problem

s = input('Enter main string: ')
sub = input('Enter sub string: ')
count = 0
for i in range(len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub:
        count +=1

print(count)