import sys
import heapq
# from collections import deq
input = sys.stdin.readline

n = int(input())
dict = {}
ans = []

for _ in range(n):
  a,b = map(str,input().split())
  dict[a] = b

for k,v in dict.items():
  if v == 'enter':
    ans.append(k)

ans.sort(reverse= True)
for x in ans:
  print(x)
