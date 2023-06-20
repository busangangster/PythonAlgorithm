import sys
input = sys.stdin.readline

n = int(input())
candidate = []
for _ in range(n):
  candidate.append(int(input()))

dasom = candidate.pop(0) # 다솜이 지지자 
cnt = 0 # 매수해야 하는 사람 수 

while True:
  if not candidate: # 다솜이 빼고 후보자가 없으면 break
    break
  else:
    candidate.sort() # 가장 지지자가 많은 후보자가 계속 바뀌기 때문에
                     # 후보자 리스트를 계속 정렬해줌 

    # 다솜이 지지자가 후보자중 가장 지지자가 많은 후보자보다 작거나 같을 때
    if dasom <= candidate[-1]:  
      candidate[-1] -= 1 # 그 후보자 1씩 빼주고
      dasom += 1 # 다솜이는 1씩 더해줌 
      cnt += 1
    else:
      break

print(cnt)




