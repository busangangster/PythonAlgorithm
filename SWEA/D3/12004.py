t = int(input())
number = []
for i in range(1,10):
  for j in range(1,10):
    number.append(i*j)

for tc in range(1,t+1):
  n = int(input())
  if n > 81:
    ans = 'No'
  else:
    if n in number:
      ans = 'Yes'
    else:
      ans = 'No'
  print('#{} {}'.format(tc,ans))

