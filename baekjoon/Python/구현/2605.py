import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
ans = []

for i in range(n):
  ans.insert(a[i],i+1)

print(*ans[::-1])
