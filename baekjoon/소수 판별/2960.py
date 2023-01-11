n,k = map(int,input().split())
a = [0] * (n+1)
cnt = 0

for i in range(2,n+1):
    for j in range(i,n+1,i):
      if a[j] == 0: # a[j] 자리가 0인지 확인해줘야함. 확인 안하면 1일 때 중복으로 cnt를 1씩 올리게 됨 
        a[j] = 1
        cnt += 1
        if cnt == k:
          print(j)
      
      
