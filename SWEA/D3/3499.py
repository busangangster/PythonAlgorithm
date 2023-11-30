t = int(input())
for tc in range(1,t+1):
  n = int(input())
  s = input().split(' ')
  half = n//2
  ans = []
  if n % 2 == 0:
    first = s[:half]
    second = s[half:]
  else:
    first = s[:half+1]
    second = s[half+1:]
  while len(second) != 0:
    ans.append(first.pop(0))
    ans.append(second.pop(0))
  if first:
    ans.append(first.pop())
  print('#{}'.format(tc),end=' ')
  print(*ans)