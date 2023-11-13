import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  dic = {}
  n = int(input())
  for _ in range(n):
    a,b = map(str,input().split())
    dic[b] = int(a)
  ans = sorted(dic.items(),key = lambda x:-x[1])
  print(ans[0][0])