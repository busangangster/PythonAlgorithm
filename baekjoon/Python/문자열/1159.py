import sys
input = sys.stdin.readline
dic = {}
ans = []
n = int(input())
for _ in range(n):
  s = input().strip()
  if s[0] in dic:
    dic[s[0]] += 1
  else:
    dic[s[0]] = 1

for x,y in dic.items():
  if y >= 5:
    ans.append(x)

if ans == []:
  print('PREDAJA')
else:
  print(''.join(map(str,sorted(ans))))

