import sys
input = sys.stdin.readline

a = input().strip()
t = input().strip()
flag = True # 조건 2 or 조건 4인지 판별
a = list(a)
aa = list(reversed(a))
s = 0
e = len(t) - 1 
start = [] # 앞에서부터 확인하는 스택
end = [] # 뒤에서부터 확인하는 스택

while s <= e: # 투포인터 사용 

  if flag:
    start.append(t[s])
    s += 1
    if start[-len(a):] == a: # 문자열을 발견하면
      start[-len(a):] = [] # 스택 안에 해당 문자열 리스트를 빈 리스트로 만듦
      flag = False # 조건 2가 성립했으니 4로 감

  else:
    end.append(t[e])
    e -= 1
    if end[-len(a):] == aa: #start와 동일
      end[-len(a):] = []
      flag = True # 조건 4가 성립했으니 2로 가야함

# end 스택에 남아있는 문자와 start 스택에 남아있는 문자가 합해져 단어 a를 만드는 경우
while end: 
  start.append(end.pop())
  if start[-len(a):] == a:
    start[-len(a):] = []

print(''.join(start))




