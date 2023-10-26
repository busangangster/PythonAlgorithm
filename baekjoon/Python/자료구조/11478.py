import sys
input = sys.stdin.readline
a = input().strip()
arr = set()

for i in range(len(a)):
  for j in range(len(a)):
    arr.add(a[i:j+1])

print(len(arr)-1)
