import sys
import heapq
input = sys.stdin.readline

n = int(input())
k = []

for _ in range(n):
    n,m = map(int,input().split())
    k.append([n,m])

k.sort() # 데드라인을 기준으로 오름차순 정렬 
q = [] # 먹을 수 있는 컵라면 갯수를 담기 위한 리스트

for i in k:
  heapq.heappush(q,i[1])
  if i[0] < len(q): # 리스트의 길이가 데드라인보다 크면 
     heapq.heappop(q) # 가장 작은 값을 큐에서 빼줌 

print(sum(q))


    
  

  
