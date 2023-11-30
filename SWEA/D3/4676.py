t = int(input())
for tc in range(1,t+1):
  s = list(input())
  h = int(input())
  a = list(map(int,input().split()))
  a.sort(reverse=True)
  for x in a:
    s.insert(x,'-')
  # print('#{}'.format(tc),end=' ')
    print(''.join(map(str,s)))