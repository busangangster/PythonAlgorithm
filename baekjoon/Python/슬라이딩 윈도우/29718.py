import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
a = int(input())
clap = []

for i in range(m):
  c = 0
  for j in range(n):
     c += graph[j][i]
  clap.append(c)

print(clap)

# 슬라이딩 윈도우
window = sum(clap[:a])
max_v = window

for i in range(a,len(clap)):
   window += clap[i] - clap[i-a]
   print(window)
   if window > max_v:
      max_v = window

print(max_v)