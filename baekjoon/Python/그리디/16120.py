# PPAP가 없어지면서 P가 됨 

import sys

word = sys.stdin.readline().strip()
stack = []

# 입력 받은 문자열이 P이거나 PPAP면 바로 PPAP 출력
if word == 'P' or word == 'PPAP':
  print('PPAP')
else:
  for x in word: # 입력 받은 문자를 stack에 추가
    stack.append(x)
    # 스택 뒤에서 4번째까지의 문자가 PPAP라면, P만 남기고 나머지는 제거
    if stack[-4:] == ['P','P','A','P']:
      stack.pop()
      stack.pop()
      stack.pop()
  # 제거하는 과정이 끝났을 때, stack에 남은 문자가 P or PPAP라면 
  # PPAP 출력.
  # 아니면 NP 출력
  if stack == ['P'] or stack == ['P','P','A','P']:
    print('PPAP')
  else:
    print('NP')



