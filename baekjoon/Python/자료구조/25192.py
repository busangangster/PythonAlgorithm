import sys
input = sys.stdin.readline

n = int(input())
flag = False
stack = set() # 아이디의 중복을 허용하지 않기 위해 set 자료구조 사용 
cnt = 0

for _ in range(n):
  a = input().strip()
  if a == 'ENTER': # 새로운 사람이 들어왔을 때
    cnt += len(stack) # set안에 있는 요소의 개수를 cnt에 더해주고
    stack = set() # set을 초기화해줌
    flag = True # enter이 입력되고 난 이후에 오는 닉네임들은 set에 추가해줘야 함

  else:
    if flag == True: # flag가 true면 set에 추가
      stack.add(a)

if stack: # set안에 남아있는 요소의 개수를 cnt에 추가
  cnt += len(stack)

print(cnt)