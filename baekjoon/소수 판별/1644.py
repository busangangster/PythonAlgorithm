n =int(input())

a = [0] * (n+1)
b = []

for i in range(2,n+1):
  if a[i] == 0:
    b.append(i)
    for j in range(i+i,n+1,i):
        a[j] = 1

# 투포인터: lt와 rt를 사용하여, 원하는 값보다 작은 경우 rt를 1 증가,
# 원하는 값보다 클 경우 lt를 1증가
lt = 0
rt = 0
cnt = 0

while rt <= len(b):
  tot = sum(b[lt:rt])
  if n == 1:
    break
  if tot == n: # 같을 때 cnt와 rt를 1씩 증가
    cnt += 1
    rt += 1
  elif tot < n: # tot가 n보다 작으면 rt를 1증가 
    rt += 1
  else: # tot가 크면 lt를 1 증가
    lt += 1
  
print(cnt)







