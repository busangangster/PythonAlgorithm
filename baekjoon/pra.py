import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
ans = [0] * n

for i in range(n):
  