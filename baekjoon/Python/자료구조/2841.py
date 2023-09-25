import sys
input = sys.stdin.readline

n,p = map(int,input().split())
arr = []
stack = [[] for _ in range(7)]
cnt = 0
for _ in range(n):
  arr.append(list(map(int,input().split())))

for i,j in arr:
  if not stack[i]: # 해당 줄 stack이 비어있으면 프렛 추가
    stack[i].append(j)
    cnt += 1
  else:
    if stack[i][-1] < j: # stack top의 프렛보다 해당 프렛이 더 크면
      stack[i].append(j) # 해당 줄 stack에 추가
      cnt += 1

    elif stack[i][-1] == j: # 프렛이 같으면 조건문 이하 생략
      continue

    else: # 작은 경우
      while stack[i] and stack[i][-1] > j: # stack top 프렛이 해당 프렛보다 작아질 때까지 pop
        stack[i].pop()
        cnt += 1
      if stack[i] and stack[i][-1] == j: # pop이 끝나고 stack top와 해당 프렛이 같으면 조건문 이하 생략
        continue
      else: # 더 크면 stack에 추가 
        stack[i].append(j)
        cnt +=1 

print(cnt)