import sys
input = sys.stdin.readline

n = int(input())
body = []
grade = []

for _ in range(n):
  a = list(map(int,input().split()))
  body.append(a)

for i in range(n):
  ans = 0
  for j in range(n):
    if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
      ans += 1
  grade.append(ans+1)

for x in grade:
  print(x,end=' ')
