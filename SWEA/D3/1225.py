from collections import deque

for t_case in range(1,11):
  n = int(input())
  a = deque(map(int,input().split()))
  n = 1
  while True:
    if n == 6:
      n = 1
    a.append(a.popleft() - n)
    if a[-1] <= 0:
      a[-1] = 0
      break
    n += 1

  print('#{}'.format(t_case),end=' ')
  print(*a)

