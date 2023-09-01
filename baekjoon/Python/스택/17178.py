import sys
input = sys.stdin.readline

n = int(input())
a = []
stack = []
for _ in range(n):
  a.append(list(input().split()))


for i in range(n):
  for j in range(4):
    if a[i][0][0] > a[i][1][0] or int(a[i][0][2:]) > int(a[i][1][2:]):
      print('f')
      stack.append(a[i].pop(0))
    else:

      if stack:
        if a[i][0][0] < stack[-1][0] or int(a[i][0][2:]) < int(stack[-1][2:]):
          print('p')
          a[i].pop(0)
        else:
          print('t')
          stack.pop()

    print(stack)
    print(a)





    # if arr[i][0] > arr[i][1]:
    #   print('f')
    #   stack.append(arr[i].pop(0))
    # else:
    #   print('t')
    #   if stack:
    #     if arr[i][0] < stack[-1]:
    #       arr[i].pop(0)
    #     else:
    #       stack.pop()
    # if len(stack) >= 2 and stack[-1] > stack[-2]:
    #   print('BAD')
    #   break
    # print(stack)
    # print(arr)
    

