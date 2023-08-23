
# 시간초과 
import sys
import heapq as hq
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
arr = []
people = [0] * n
for _ in range(n):
  a = list(map(int,input().split()))
  arr.append(a[1:])

b = list(map(int,input().split()))
b = deque(b)

while b:
  for i in range(n):
    if b[0] in arr[i]:
      people[i] += 1 
      b.popleft()
      break
  else:
    b.popleft()

print(*people)


