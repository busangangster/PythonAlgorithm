import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
c = int(input())
a = list(map(int,input().split()))
p = []
score = []

for i in range(c):
  if a[i] in p:
    for j in range(len(p)):
      if p[j] == a[i]:
        score[j] += 1
  else:
    if len(p) >= n:
      for j in range(n):
        if score[j] == min(score):
          del p[j]
          del score[j]
          break
    p.append(a[i])
    score.append(1)

print(score)
p.sort()
print(*p)
