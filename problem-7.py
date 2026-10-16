## 7.https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    words=line.split()
    new="-".join(words)
    return new
line = input()
result = split_and_join(line)
print(result)