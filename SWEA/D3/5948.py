from itertools import combinations
t = int(input())
for tc in range(1,t+1):
  k = set()
  a = list(map(int,input().split()))
  ans = combinations(a,3)
  ans = list(ans)
  for x in ans:
    k.add(sum(x))
  k = list(k)
  k.sort(reverse=True)
  
  print('#{} {}'.format(tc,k[4]))
  

  
