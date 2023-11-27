import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  a = input().strip()
  if 6 <= len(a) <= 9:
    print('yes')
  else:
    print("no")