import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
cnt = 0
cards = []
ans = []
kk = set()
for _ in range(n):
  cards.append(int(input()))
check = [False] * n

def DFS():
  if len(ans) == k:
    kk.add(''.join(map(str,ans)))
    return
  else:
    for i in range(n):
      if check[i] == False:
        ans.append(cards[i])
        check[i] = True
        DFS()
        ans.pop()
        check[i] = False

DFS()
print(len(kk))