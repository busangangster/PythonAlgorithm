import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dict = {}

for _ in range(n):
  word = input().strip()
  if len(word) < m:
    continue
  else:
    if word in dict:
      dict[word] += 1
    else:
      dict[word] = 1

# Option 1 
# 우선순위에 따라 각각 정렬 
book = sorted(dict.items(),key = lambda x:x[0])
book.sort(key = lambda x:len(x[0]),reverse=True)
book.sort(key = lambda x:x[1], reverse= True)

# Option 2
# lambda로 정렬할 순서를 정해줘서 정렬 
book = sorted(dict.items(),key = lambda x: (-x[1], -len(x[0]),x[0]))

for x in book:
  print(x[0])