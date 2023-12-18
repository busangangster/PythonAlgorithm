import sys
input = sys.stdin.readline
n = int(input())
arr = [0 for _ in range(10001)]
arr[0] = 0
arr[1] = 1
if n == 0:
  print(arr[0])
elif n == 1:
  print(arr[1])
else:
  for i in range(2,n+1):
    arr[i] = arr[i-1]+arr[i-2]
  print(arr[n])
