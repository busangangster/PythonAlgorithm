import sys
input = sys.stdin.readline

arr = []
sum = 0
for _ in range(10):
  a,b = map(int,input().split())
  sum -= a
  sum += b
  arr.append(sum)

print(max(arr))

