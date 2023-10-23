import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [x for x in range(n,m+1)]

eng = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six',
       '7':'seven','8':'eight','9':'nine'}
dic = {}
ans = []
for i in arr:
  w = []
  a = str(i)
  for x in a:
    w.append(eng[x])

  t = ''.join(map(str,w))
  dic[t] = i

k = sorted(dic.items(), key= lambda x:x[0])

for i in range(0,len(arr),10):
  for j in range(i,i+10):
    if j == len(arr):
      break
    print(k[j][1],end=' ')
  print()
