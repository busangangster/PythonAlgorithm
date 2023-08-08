import sys
input = sys.stdin.readline

s = list(input().strip())
t = list(input().strip())

while t: # t가 빈리스트가 아닐 때 동안 반복문 실행
  if t[-1] == 'A': # 마지막 문자가 A면
    t.pop() # 그냥 A 제거 
    if t == s: # t가 s가 될 수 있는 지 확인 
      print(1)
      break
  elif t[-1] == 'B': # 마지막 문자가 B면
    t.pop() # 제거해주고
    t = t[::-1] # 문자열 뒤집기
    if t == s:
      print(1)
      break
else: # while문이 정상적으로 종료되면 0 출력 
  print(0)




