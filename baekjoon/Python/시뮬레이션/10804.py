import sys
input = sys.stdin.readline

arr = [x for x in range(1,21)] 

for _ in range(10):
  a,b = map(int,input().split())
  arr = arr[:a-1] + arr[a-1:b][::-1] + arr[b:]

print(*arr)