import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
stack = [[],[],[],[]]

for i in arr:
  for j in range(4):
    if not stack[j]:
      stack[j].append(i)
      break
    else:
      if stack[j][-1] < i:
        stack[j].append(i)
        break
  else:
    print('NO')
    break

else:
  print('YES')
