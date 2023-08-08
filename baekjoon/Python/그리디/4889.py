

import sys
input = sys.stdin.readline
num = 1

while True:
  a = list(input().strip())
  stack = []
  cnt = 0
  if '-' in a:
    break
  else:
    for x in a:
      if not stack and x == '}': # 스택이 비어있고, x가 '}'일 때
        cnt += 1 # 문자 변환 and stack에 추가
        stack.append('{')
      elif stack and x == '}': # 스택이 비어있지 않고, x가 '}'일 때
        stack.pop() # 짝을 이뤄서 제거 
      else: # 아닌 경우는 전부 추가
        stack.append(x)
      
    cnt += len(stack) //2 # stack안에 들어있는 문자들을 짝 맞춰주기 

  print("%s. %s" %(num,cnt))
  num += 1
  


