# 문제의 포커스는 점수가 아니라 "순위"임 
# 순위라는 것을 알게 되면 쉽게 풀 수 있다. 
# 앞사람 보다 순위가 더 높아야 한다는 뜻 == 숫자가 작아야 한다  
import sys
n = int(sys.stdin.readline())

for _ in range(n):
  a = int(sys.stdin.readline())
  b = []
  cnt = 0
  best = 2147000000
  for _ in range(a):
    s,k = map(int,sys.stdin.readline().split())
    b.append((s,k))
  b.sort()

  for s,k in b:
    if k < best:
      best = k
      cnt += 1
  print(cnt)