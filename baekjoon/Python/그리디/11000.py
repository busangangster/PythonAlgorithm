
import sys
import heapq
input = sys.stdin.readline

n = int(input())
sub = []

for _ in range(n):  
  a = list(map(int,input().split()))
  sub.append(a)

sub.sort()

sub_queue =[]
heapq.heappush(sub_queue,sub[0][1])

for i in range(1,n):
  if sub[i][0] < sub_queue[0]:
    heapq.heappush(sub_queue,sub[i][1])
  else:
    heapq.heappop(sub_queue)
    heapq.heappush(sub_queue,sub[i][1])

print(len(sub_queue))
      