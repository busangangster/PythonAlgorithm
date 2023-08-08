import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))
cnt = 0

a.sort() # 입력 값을 오름차순 정렬
# 오름차순 정렬한 것을 10으로 나눴을 때 나머지를 기준으로 다시 정렬 
a.sort(key = lambda x:x % 10 ) 

for x in a:
  if m > 0:
    if x % 10 == 0: # x가 10의 배수일 때
      flag = (x // 10) -1 # 자르는 횟수 =  x를 10으로 나눈 몫 -1 
      if  flag == 0: # flag가 0이면 x는 10
        cnt += 1
      else:
        if m >= flag: # 남아있는 쪼갤 수 있는 횟수가 flag보다 크거나 같으면
          cnt += flag +1 
          m -= flag 
        else: # 작으면 m만큼만 롤케이크 생성 
          cnt += m
          break
    else: # x가 10의 배수가 아닐 때 
      flag = (x//10) # 자르는 횟수 =  x를 10으로 나눈 몫 
      if m >= flag: # 남아있는 쪼갤 수 있는 횟수가 flag보다 크거나 같으면
        cnt += flag
        m -= flag 
      else: # 작으면 m만큼만 롤케이크 생성 
        cnt += m
        break
  else:
    break

print(cnt)

        


