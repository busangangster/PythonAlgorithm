import sys
input = sys.stdin.readline

n,m = map(int,input().split())
cnt = 0
stack = []

if n == 0: # n이 0일 때, 0을 출력하고 프로그램 종료
  print(0)
  sys.exit()
else: # 아닐 때 책 무게 입력받기 
  a = list(map(int,input().split()))

for i in a:
  if sum(stack) + i > m:  # 스택 안의 요소들의 합과 i의 합이 m보다 크면 상자 체인지
    stack.clear() # 스택 안을 비워주고 
    stack.append(i) # i를 추가. 
    cnt += 1 # 상자를 바꾸기 때문에 cnt + 1
  else: # m을 안넘으면 계속 하나의 상자에 책 넣기 가능 
    stack.append(i)

if stack: # 반복문이 끝나고, 스택안에 있는 책들을 상자에 넣어줘야 함 
  cnt += 1

print(cnt)


