import sys
input = sys.stdin.readline

def DFS():
  if len(k) == len(a[0]):
    ans.append(k)
    return
  else:
    for i in range(len(a[0])):
      k.append(a[0][i])
      DFS()
      k.pop()

  return ans

while True:
  try:
    a = input().split()
    ans = []
    k = []
    if len(ans)-1 < a[1]:
      print('No permutation')
    else:
      print(ans[a[1]-1])
  
  except:
    break
