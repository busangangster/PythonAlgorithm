n = int(input())
a= list(map(int,input().split()))

a.sort()
res = 0
sum = 0
b = []

for i in a:
  res = res + i
  b.append(res)
  
for i in b:
  sum += i

print(sum)