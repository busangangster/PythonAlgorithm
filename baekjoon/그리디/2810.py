import sys
input = sys.stdin.readline

n = int(input())
a = input()
cnt = 0
stack = []

for x in a:
  while stack and stack[-2:] == ['L','L']:
    for _ in range(2):
      stack.pop()
    cnt += 1
  stack.append(x)

while stack:
  stack.pop()
  cnt += 1

if cnt >= n:
  print(n)
else:
  print(cnt)
    
# print(cnt)

