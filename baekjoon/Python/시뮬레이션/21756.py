import sys
input = sys.stdin.readline

n = int(input())
arr = [x for x in range(1,n+1)]

while len(arr) != 1:
  t = []
  for i in range(0,len(arr),2)[:]:
    arr[i] = 0

  while 0 in arr:
    arr.remove(0)

print(*arr)    


