t = int(input())
for tc in range(1,t+1):
  dic = {'b':'d','d':'b','p':'q','q':'p'}
  s = input()
  ans = ''
  for x in s:
    ans += dic[x]
  print('#{} {}'.format(tc,ans[::-1]))