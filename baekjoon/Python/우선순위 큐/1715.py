# 비교횟수를 가장 적게 하려면 낮은 수부터 둘로 묶어서 계산해야 함
# ex) 1,2,3,4 => (1+2) + (3+4) 
# 두개의 값을 pop하여 더하고, 더한 값을 다시 heap에 push하는 방식
# heap의 길이가 1이면 더이상 연산할 게 없으므로 종료
import sys
import heapq as hq

card = []
ans = 0

for i in range(int(sys.stdin.readline())):
  hq.heappush(card,int(sys.stdin.readline()))

if len(card) == 1:
  print(0)
else:
  while len(card) > 1:
    plus =  hq.heappop(card) + hq.heappop(card)
    ans += plus
    hq.heappush(card,plus)
  print(ans)