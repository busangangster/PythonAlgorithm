import sys
input = sys.stdin.readline

t = int(input())
a = list(map(int,input().split()))
cnt = 0

if sum(a) % 3 == 0:
  for i in a:
    cnt += i // 2

  if cnt < sum(a) // 3:
    print('NO')
  else:
    print('YES')

else:
  print('NO')

