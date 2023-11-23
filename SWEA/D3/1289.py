t = int(input())
for t_case in range(1,t+1):
  s = list(input())
  cnt = 0
  a = ['0' for _ in range(len(s))]
  while True:
    if a == s:
      print('#{} {}'.format(t_case,cnt))
      break
    for i in range(len(s)):
      if s[i] != a[i]:
        for j in range(i,len(a)):
          a[j] = s[i]
        cnt += 1 