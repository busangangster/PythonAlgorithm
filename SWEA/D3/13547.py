t = int(input())
for tc in range(1,t+1):
  s = input()
  if 15 - len(s) + s.count('o') >= 8:
    ans = 'YES'
  else:
    ans = 'NO'
  print('#{} {}'.format(tc, ans))