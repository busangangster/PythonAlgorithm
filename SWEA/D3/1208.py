for t_case in range(1,11):
  n = int(input())
  a = sorted(list(map(int,input().split())))
  max_v = max(a)
  while n != 0:
    if sum(a) == max_v:
      print('#{} {}'.format(t_case,a[0]))
      break
    else:
      a[0] += 1
      a[-1] -= 1
    n -= 1
    a.sort()
  print('#{} {}'.format(t_case,a[-1] - a[0]))
