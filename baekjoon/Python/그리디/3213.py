import sys
input = sys.stdin.readline

n = int(input())
arr = []
pizza1 = []
pizza2 = []
pizza3 = []
cnt = 0
for _ in range(n):
    arr.append(input().strip())

# 친구들이 먹을 수 있는 피자 양에 따른 각각의 리스트를 만들어줌 
for i in range(n): 
  if arr[i][2] == '2':
      pizza1.append(arr[i])
  elif arr[i][2] == '4' and arr[i][0] == '1':
      pizza2.append(arr[i])
  else:
      pizza3.append(arr[i])

# 1/4과 3/4은 피자 한 판으로 먹을 수 있음 
while pizza2 and pizza3:
    pizza2.pop()
    pizza3.pop()
    cnt +=1 
    
# 1/2 하나와 1/4 2개 또한 피자 한 판으로 가능
while pizza1 and pizza2:
  pizza2.pop()
  if not pizza2:
    pizza1.pop()
    cnt +=1 
    break
  pizza2.pop()
  pizza1.pop()
  cnt += 1

# 각각의 피자 양을 처리해줌 
while pizza1:
   pizza1.pop()
   if not pizza1:
      cnt += 1
      break
   pizza1.pop()
   cnt += 1

while pizza2:
   pizza2.pop()
   cnt += 1

while pizza3:
   pizza3.pop()
   cnt += 1


print(cnt)
