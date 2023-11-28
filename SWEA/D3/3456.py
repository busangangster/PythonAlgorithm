t = int(input())
for tc in range(1,t+1):
  dic = {}
  ans = 0
  a = list(map(int,input().split()))
  for x in a:
    if x in dic:
      dic[x] += 1
    else:
      dic[x] = 1
  for x,y in dic.items():
    if y == 1 or y == 3: 
      ans = x
  print('#{} {}'.format(tc,ans))