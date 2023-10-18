import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def DFS(num,a):
  a[num] = -2

  for i in range(len(a)):
    if num == a[i]:
      DFS(i,a)


n = int(input())
a = list(map(int,input().split()))
k = int(input())
cnt = 0

DFS(k,a)

for i in range(len(a)):
  if a[i] != -2 and i not in a:
    cnt += 1

print(cnt)
