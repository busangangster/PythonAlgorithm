import sys
input = sys.stdin.readline

arr = []
d = []
for _ in range(9):
  arr.append(int(input()))

for i in range(len(arr)):
  for j in range(i+1,len(arr)):
    if sum(arr) - (arr[i]+arr[j]) == 100:
      tmp1 = arr[i]
      tmp2 = arr[j]

arr.remove(tmp1)
arr.remove(tmp2)

arr.sort()
for i in arr:
  print(i)