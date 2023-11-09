import sys
input = sys.stdin.readline

num = []
dic = {}
for _ in range(10):
  a = int(input())
  num.append(a)
  if a in dic:
    dic[a] += 1
  else:
    dic[a] = 1

k = sorted(dic.items(),key = lambda x:-x[1])
print(sum(num)//10)
print(k[0][0])