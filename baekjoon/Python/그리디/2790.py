import sys
input = sys.stdin.readline

n = int(input())
pp = []
for _ in range(n):
  pp.append(int(input()))

pp = sorted(pp)

for i in range(len(pp)):
  pp[i] = pp[i] + n
  n -= 1
cnt  = 0
maxinum = max(pp)

for i in range(len(pp)-1):
  if pp[i] >= maxinum:
    cnt += 1
  n += 1
  pp[i+1] += n

if pp[-1] > maxinum:
  print(cnt + 1)
else:
  print(cnt)


