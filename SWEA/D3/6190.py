t = int(input())
for t_case in range(1,t+1):
  n = int(input())
  a = list(map(int,input().split()))
  s = set()
  for i in range(n):
    for j in range(i+1,n):
      s.add(a[i]*a[j])

  ans = list(s)
  ans.sort(reverse= True)
  for x in ans:
    ss = str(x)
    for i in range(len(ss)-1):
      if ss[i] > ss[i+1]:
        break
    else:
      print('#{} {}'.format(t_case,ss))
      break
  else:
    print('#{} -1'.format(t_case))