t = int(input())
for tc in range(1,t+1):
  s = input()
  ans = set()
  for x in s:
    if s.count(x) % 2 == 0:
      continue
    else:
      ans.add(x)
  if not ans:
    print('#{} Good'.format(tc))
  else:
    ans = list(ans)
    ans.sort()
    print('#{} {}'.format(tc, ''.join(map(str,ans))))