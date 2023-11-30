t = int(input())
for tc in range(1,t+1):
  words = [list(input()) for _ in range(5)]
  ans = ''
  for i in range(15):
    for j in range(15):
      try:
        ans += words[j][i]
      except IndexError:
        continue
  print('#{} {}'.format(tc,ans))
