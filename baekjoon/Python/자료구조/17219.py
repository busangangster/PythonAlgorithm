import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dict = {}

for _ in range(n):
  a,b = map(str,input().split())
  dict[a] = b

for _ in range(m):
  k = input().strip()
  print(dict[k])