k = int(input())

for _ in range(k):
  n = int(input())
  a = [0] * (n+1)
  
  for i in range(2,n+1):
    while n%i == 0:
      a[i] += 1
      n = n // i
    if a[i] != 0:
      print(i,a[i])
      
  
    
