import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

max_value = -2147000000
min_value = 2147000000



def DFS(i,total,plus,minus,multi,divide):
  global max_value,min_value
  if i == n:
    max_value = max(total,max_value)
    min_value = min(total,min_value)
    return
  else:
    if plus:
      DFS(i + 1, total+a[i], plus-1, minus, multi, divide)
    if minus:
      DFS(i + 1, total-a[i], plus, minus-1, multi, divide)
    if multi:
      DFS(i + 1, total*a[i], plus, minus, multi-1, divide)
    if divide:
      DFS(i + 1, int(total/a[i]), plus, minus, multi, divide-1)
     
DFS(1,a[0],b[0],b[1],b[2],b[3])

print(max_value)
print(min_value)