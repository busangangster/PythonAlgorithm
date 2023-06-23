import sys
input = sys.stdin.readline

n, k = map(int,input().split())
a = list(input().strip())
cnt = 0

for i in range(len(a)):
  if a[i] == 'P':
    for j in range(i-k,i+k+1):
      if 0 <= j < n and a[j] == 'H':
        cnt +=1 
        a[j] = 'eaten'
        break


print(cnt)

