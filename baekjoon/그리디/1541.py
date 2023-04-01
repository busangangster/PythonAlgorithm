# '-'를 만나기 전까지의 값은 모두 더해줘야함
# '-'를 만난 이후에 만나는 값들은 총합에서 빼줘야 함 

n = input().split('-')
sum = 0

# 리스트 n의 첫번째 인덱스는 '-'를 만나기 전 수임 
# 그래서 총합 sum에 더해줌 
for i in n[0].split('+'):
  sum += int(i)

# '-'를 만난 이후의 값들은 모두 빼줘야만 최소값을 만들 수 있음 
# 뒤에서 '+'가 아닌 '-'를 만난다 하더라도 괄호가 처음 만난 '-'뒤에 들어가기 때문에
# 총합에서 빼주면 된다. 
for i in n[1:]:
  for j in i.split('+'):
    sum -= int(j)

print(sum)




