import sys
input = sys.stdin.readline

n = input().strip()
arr = [0] * 9

for x in n:
  a = int(x)
  if a == 9:
    a = 6
  arr[a] += 1

arr[6] = (arr[6]+1) // 2
print(max(arr))
