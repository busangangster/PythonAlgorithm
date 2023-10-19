import sys
input = sys.stdin.readline

s = input().strip()
j = []

for i in range(len(s)):
  j.append(s[i:len(s)+1])

j.sort()

for x in j:
  print(x)
