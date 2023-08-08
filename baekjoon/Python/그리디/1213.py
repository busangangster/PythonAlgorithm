# 문자의 개수가 홀수개인 것이 2개 이상이면 펠린드롬을 만들 수 없음 ! 

import sys
input = sys.stdin.readline

# 결과 출력시, 여러개의 펠린드롬 문자가 있을 경우
# 사전순으로 출력해야 하기 때문에 정렬 필수 ! 
a = sorted(input().strip()) 
dict = {} # 알파벳 개수를 세기 위한 딕셔너리 
cnt = 0
center = ''
ans = '' 

for x in a:
  if dict.get(x) == None:
    dict[x] = 1
  else:
    dict[x] += 1

# 문자의 개수가 홀수인 것이 2개 이상인지 판별 ! 
for k,v in dict.items(): 
  if v % 2 != 0:
    cnt += 1
    if cnt >= 2: # 2개 이상이면 펠린드롬 안됨
      print("I'm Sorry Hansoo")
      break
    center = k # 문자의 개수가 홀수인 알파벳이 중간에 들어감

# for문이 break 없이 정상적으로 끝났을 경우
else:
  for k,v in dict.items(): # 펠린드롬 출력과정 
    ans += k*(v//2) # 알파벳 개수 // 2를 곱해줌 ! 
  ans += center + ans[::-1]

print(ans)
  

  