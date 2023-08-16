import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
  arr.append(list(map(int,input().split())))

print(arr)
  