import sys
input = sys.stdin.readline

t = int(input())
arr = [0 for _ in range(68)]
arr[0] = 1
arr[1] = 1
arr[2] = 2
arr[3] = 4
for _ in range(t):
  n = int(input())
  if n < 2:
    print(1)
  elif n == 2:
    print(2)
  elif n == 3:
    print(4)
  else:
    for i in range(4,n+1):
      arr[i] = arr[i-1] + arr[i-2] + arr[i-3] + arr[i-4]
    print(arr[n])