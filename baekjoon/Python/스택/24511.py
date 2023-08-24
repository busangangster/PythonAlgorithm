
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
m = int(input())
c = list(map(int,input().split()))
q = deque()

# stack은 append하고 pop하는 하면 똑같은 수가 왔다가 빠지는 것이기에 의미 X
for i in range(n):
  if a[i] == 0: # stack은 버리고, queue 자료구조만 취급
    q.appendleft(b[i])

for i in range(m):
  q.append(c[i])
  print(q.popleft(),end=' ')


