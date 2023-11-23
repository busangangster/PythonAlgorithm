t = int(input())
for t_case in range(1,t+1):
  lt = 1
  rt = 1
  s = list(input())
  for x in s:
    if x =='L':
      lt = lt
      rt = lt + rt
    else:
      lt = lt + rt
      rt = rt
  print('#{} {} {}'.format(t_case,lt,rt))