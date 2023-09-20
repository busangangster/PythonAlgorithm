import sys
input = sys.stdin.readline

n,m = map(int,input().split())
player = []
score = [0] * (n+1)
a = []

for _ in range(n):
  player.append(sorted(list(map(int,input().split()))))

for i in range(m):
  for j in range(n):
    a.append(player[j].pop())

  for k in range(n):
    if a[k] == max(a):
      score[k+1] += 1

  a.clear()

for i in range(1,len(score)):
  if score[i] == max(score):
    print(i,end=' ')
