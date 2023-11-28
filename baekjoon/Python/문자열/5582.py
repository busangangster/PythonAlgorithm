import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  number = []
  n = int(input())
  for _ in range(n):
    number.append(input().strip())
  number.sort(key = lambda x:x)
  for i in range(n-1):
    if number[i] == number[i+1][:len(number[i])]:
      print('NO')
      break
  else:
    print('YES')
