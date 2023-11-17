t = int(input())

for t_case in range(1,t+1):
  n = int(input())
  ans = set()
  num = 0
  while True:
    if ans == {0,1,2,3,4,5,6,7,8,9}:
      print('#{} {}'.format(t_case,k))
      break
    else:
      num += 1
      k = n * num
      for x in str(k):
        j = int(x)
        ans.add(j)
