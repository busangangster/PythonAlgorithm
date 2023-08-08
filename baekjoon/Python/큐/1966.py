import sys
from collections import deque

test = int(sys.stdin.readline())

for _ in range(test):
  n,m = map(int,sys.stdin.readline().split())
  # 리스트 받으면서 인덱스 번호랑 중요도 같이 큐에 넣는 작업
  a = [(pos,im) for pos, im in enumerate (list(map(int,sys.stdin.readline().split())))]
  a = deque(a)
  cnt = 0
  while a:
    cur = a.popleft()
    # 하나라도 중요도가 cur보다 큰게 있으면 
    if any(cur[1] < x[1] for x in a):
      a.append(cur)
    else:
      cnt += 1
      if cur[0] == m:
        print(cnt)

