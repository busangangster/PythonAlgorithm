t = int(input())
for t_case in range(1,t+1):
  dic =[]
  s = input()
  for x in s:
    if x in dic:
      continue
    else:
      dic.append(x)
  print('#{} {}'.format(t_case,len(dic)))
