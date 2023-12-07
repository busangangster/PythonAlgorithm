t = int(input())
for tc in range(1,t+1):
  n,m = map(int,input().split())
  ans = 0
  stack = [[] for _ in range(n)]
  wait = []
  lot = []
  for _ in range(n):
    lot.append(int(input()))
  car = []
  for _ in range(m):
    car.append(int(input()))

  for _ in range(2*m):
    a = int(input())
    if a >= 0:
      for i in range(n):
        if not stack[i]:
          stack[i].append(a)
          break
      else:
        wait.append(a)
    else:
      t = abs(a)
      for i in range(n):
        if stack[i] and stack[i][0] == t:
          ans += lot[i] *car[stack[i].pop()-1]
          break
      if wait:
        for i in range(n):
          if not stack[i]:
            stack[i].append(wait.pop(0))
            break

  print('#{} {}'.format(tc, ans))