import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int,input().split())))

if n % 2 == 1: # n이 홀수일 때
  print(a[n//2])
else: # n이 짝수일 때
  print(a[(n//2)-1])