import sys
dic = {}

s = sys.stdin.read()
for x in s:
  if x.isalpha():
    if x in dic:
      dic[x] += 1
    else:
      dic[x] = 1

t = sorted(dic.items(),key = lambda x:x[1],reverse=True)
ans = t[0][1]
result = []
for x,y in dic.items():
  if y == ans:
    result.append(x)
result.sort()
print(''.join(map(str,result)))