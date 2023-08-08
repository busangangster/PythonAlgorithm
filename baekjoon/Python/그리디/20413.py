import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
mvp = list(input().strip())
money= [0]

for i in range(n):
  if mvp[i] == 'B':
    if money[-1] == arr[0] -1:
      money.append(0)
    else:
      money.append(arr[0]-1)

  elif mvp[i] == 'S':
    if money[-1] == arr[1] -1:
      money.append(0)
    else:
      money.append(arr[1]-1 - money[-1])

  elif mvp[i] == 'G':
    if money[-1] == arr[2] -1:
      money.append(0)
    else:
      money.append(arr[2]-1 - money[-1])

  elif mvp[i] == 'P':
    if money[-1] == arr[3] -1:
      money.append(0)
    else:
      money.append(arr[3]-1 - money[-1])

  elif mvp[i] == 'D':
    money.append(arr[3])

print(sum(money))


