t = int(input())
for tc in range(1,t+1):
  s = input()
  dic = {}
  for x in s:
    if x in dic:
      dic[x] += 1
    else:
      dic[x] = 1 
  if len(dic) == 2:
    for x,y in dic.items():
      if y != 2:
        ans = 'No'
        break
    else:
      ans = 'Yes'
  else:
    ans = 'No'
  print('#{} {}'.format(tc,ans))
