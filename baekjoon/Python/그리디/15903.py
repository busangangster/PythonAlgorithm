import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))

for _ in range(m):
  a.sort() # 합체 놀이를 할 때마다 오름차순 정렬
  res = a[0] + a[1]  # 오름차순 정렬했기 때문에 가장 낮은 수 2개를 더해줌
  a[0] = res # 두 수의 합을 각각의 자리에 덮어씀 
  a[1] = res

print(sum(a))

  
