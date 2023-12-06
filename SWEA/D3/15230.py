t = int(input())
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
         'q','r','s','t','u','v','w','x','y','z']
for tc in range(1,t+1):
  s = input()
  cnt = 0
  for i in range(len(s)):
    if s[i] == alpha[i]:
      cnt += 1
    else:
      break
  print('#{} {}'.format(tc,cnt))