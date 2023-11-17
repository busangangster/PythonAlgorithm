t = int(input())
for t_case in range(1,t+1):
  n = int(input())
  s = 0
  ans = 0
  for _ in range(n):
    a = list(input().split())
    if a[0] == '0':
      ans += s
    else:
      ms = int(a[1])
      if a[0] == '1':
        s += ms
        ans += s

      else:
        if ms > s:
          s = 0
        else:
          s -= ms 
        ans += s
  print('#{} {}'.format(t_case,ans))