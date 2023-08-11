import sys
input = sys.stdin.readline

n,k  = map(int,input().split())
a = list(map(int,input().split()))
arr = []

for i in range(1,n): # 원생 간의 키 차이를 배열로 만듦
  arr.append(a[i] - a[i-1])

arr.sort() #  최솟값을 구하기 위해 오름차순 정렬 

for _ in range(k-1): # k조로 나눠야 하기 때문에 k-1만큼 배열 끝에서부터 제거
  arr.pop()

print(sum(arr)) # 배열의 합이 티셔츠를 만드는 비용 


