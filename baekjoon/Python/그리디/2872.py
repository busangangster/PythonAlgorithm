import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
  arr.append(int(input()))

cnt = 0
cur = arr[0]

for i in arr[1:]:
  if i > cur:
    if cur + 1 != i:
      cnt += 1
    cur = i
  else:
    cnt += 1

print(cnt)