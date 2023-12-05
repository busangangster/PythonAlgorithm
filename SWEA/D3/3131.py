arr = [True for _ in range(1000001)]
for i in range(2,int(1000000**0.5)+1):
  if arr[i] == True:
    j = 2
    while i*j <= 1000000:
      arr[i*j] = False
      j += 1
for i in range(2,1000001):
  if arr[i] == True:
    print(i,end=' ')