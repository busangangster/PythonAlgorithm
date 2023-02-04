# (절대값, 원래값)으로 정렬하게 되면, 절대값으로 먼저 정렬, 같을 시에는 원래값으로 정렬
# 절대값 같을 때 원래 값으로 정렬하고 pop해줌
# pop 해줄 때는 절대값이 아닌 원래값으로 
import sys
import heapq as hq

n = int(sys.stdin.readline())

a = []

for _ in range(n):
  x = int(sys.stdin.readline())
  if x == 0:
    if not a:
      print(0)
    else:
      print(hq.heappop(a)[1])
  else:
    hq.heappush(a,(abs(x),x))