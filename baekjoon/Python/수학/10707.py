import sys
input = sys.stdin.readline

k = [int(input()) for _ in range(5)]
first = k[0]*k[4]
second = 0
if k[4] <= k[2]:
  second = k[1]
else:
  second = k[1] + (k[4]-k[2])*k[3]

print(min(first,second))