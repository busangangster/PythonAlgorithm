# 원판에 둘러앉아있고, 한 부분을 지정할 때는 p = (p+l) % n
import sys
input = sys.stdin.readline

n,m,l = map(int,input().split())
people = [0 for _ in range(n)]
cnt = 0
p = 0

while True:
  people[p] += 1
  if people[p] == m:
    print(cnt)
    break
  else:
    if people[p] % 2 == 0:
      p = (p+n-l) % n
    else:
      p = (p+l) % n
    cnt += 1

