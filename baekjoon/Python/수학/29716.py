import sys
input = sys.stdin.readline

j,n = map(int,input().split())
ps = []
for _ in range(n):
  a = list(input().strip())
  score = 0
  for x in a:
    if x.isupper():
      score += 4
    elif x.islower() or x.isdigit():
      score += 2
    elif x ==' ':
      score += 1

  ps.append(score)

cnt = 0
for x in ps:
  if x <= j:
    cnt += 1

print(cnt)