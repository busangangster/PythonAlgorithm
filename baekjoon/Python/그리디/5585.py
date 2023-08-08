n = int(input())
p = 1000-n
cnt = 0
a = [1,5,10,50,100,500]
a.sort(reverse=True)

for i in a:
  cnt += p//i
  p = p%i

print(cnt)