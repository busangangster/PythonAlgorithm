import sys
input = sys.stdin.readline

n = int(input())
w = []
number = []
for _ in range(n):
  w.append(input().strip())

for i in w:
  stack = []
  for j in range(len(i)):
    k = []
    if i[j].isdigit():
      stack.append(i[j])
    else:
      if stack:
        while stack:
          k.append(stack.pop(0))
        number.append(k)

  if stack:
    while stack:
      k.append(stack.pop(0))
    number.append(k)

ans = []
for x in number:
  ans.append(int(''.join(map(str,x))))

ans.sort()
for x in ans:
  print(x)
  
