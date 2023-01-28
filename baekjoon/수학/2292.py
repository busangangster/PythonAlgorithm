# 육각형을 싸고 있는 겹이 최단거리임 
# 횟수를 세는 변수와 방 수를 세는 변수를 선언할 때 n에 1이 들어올 수 있다는 것을 생각해야 함 

import sys
n = int(sys.stdin.readline())
cnt = 1 # n에 1이 들어올 때 생각 
stack = 1 # n에 1이 들어올 때 생각
while stack < n:
  stack = stack + cnt*6
  cnt += 1

print(cnt)
