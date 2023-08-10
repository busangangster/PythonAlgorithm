import sys
input = sys.stdin.readline

n = int(input())
a = []
s = []
t = []
score = 0

for _ in range(n):
  a.append(list(map(int,input().split())))

for i in range(n):
  if a[i][0] == 1:
    if a[i][2] == 1:
      score += a[i][1]
    else:
      s.append(a[i][1])
      t.append(a[i][2])

  else:
      if s and t:
        t[-1] -= 1  
        if t[-1] == 1:
          score += s.pop()
          t.pop()

print(score)



