import sys
input = sys.stdin.readline
a,b = map(int,input().split())
A = min(a,b)
B = max(a,b)
s = []

if B-A == 1 or B-A == 0:
  print(0)
else:
  for i in range(A+1,B):
    s.append(i)

  print(len(s))
  for x in s:
    print(x,end=' ')
