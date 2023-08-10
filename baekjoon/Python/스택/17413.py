import sys
input = sys.stdin.readline

a = input().strip()
stack = []
flag = False # 괄호 안에 있는지 아닌지 확인 
ans = '' # 정답 출력 변수

for i in a:
  if i == ' ': # 공백을 만나면 stack 안에 요소들을 뒤에서부터 출력
    while stack:
      ans += stack.pop()
    ans += i
  
  elif i == '<': # 시작하는 괄호를 만났을 때는 stack의 요소들을 뒤에서부터 출력
    while stack:
      ans += stack.pop()
    flag = True # 괄호 안에 있음을 알려줌 
    ans += i

  elif i == '>': # 괄호가 끝난 경우는 flag를 다시 False로 변경
    flag = False
    ans += i 

  elif flag: # flag가 True인 경우는 괄호 안에 있는 경우이기 때문에 글자를 뒤집지 않음
    ans += i

  else: # 그 외의 경우 
    stack.append(i)

while stack: # stack안에 남이있는 요소들 거꾸로 출력 
  ans += stack.pop()

print(ans)



