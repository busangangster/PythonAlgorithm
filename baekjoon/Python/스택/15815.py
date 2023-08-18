import sys
input = sys.stdin.readline

a = list(input().strip())
stack = []

for i in a:
  t = 0
  if i.isdigit(): # i가 숫자이면 
    stack.append(int(i)) # 문자열을 정수형으로 stack에 추가
  else:
    # 연산자에 따라 stack의 top에서 두번째 수와 stack의 top을 연산해줌
    if i == '+':
      t = stack[-2] + stack[-1]
      for _ in range(2):
        stack.pop()
      stack.append(t)
    elif i == '-':
      t = stack[-2] - stack[-1]
      for _ in range(2):
        stack.pop()
      stack.append(t)
    elif i == '*':
      t = stack[-2] * stack[-1]
      for _ in range(2):
        stack.pop()
      stack.append(t)
    else:
      t = stack[-2] / stack[-1]
      for _ in range(2):
        stack.pop()
      stack.append(t)
    
print(int(stack[-1])) # 정수형으로 출력