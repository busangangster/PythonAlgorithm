
import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
boxes = list(map(int,sys.stdin.readline().split()))

a.sort(reverse = True)
boxes.sort(reverse = True)

cnt = 0

if boxes[0] > a[0]:
  print(-1)
else:
  while len(boxes) > 0:
    for i in a:
      if boxes and i < boxes[-1]:
        continue
      for j in boxes:
        if i >= j:
          boxes.remove(j)
          break
    cnt += 1
  print(cnt)





