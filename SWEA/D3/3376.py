t = int(input())
arr = [0 for _ in range(101)]
arr[1] = 1
arr[2] = 1
arr[3] = 1
arr[4] = 2
for tc in range(1,t+1):
  n = int(input())
  if n <= 4:
    print('#{} {}'.format(tc,arr[n]))
  else:
    for i in range(5,n+1):
      arr[i] = arr[i-3]+arr[i-2]
    print('#{} {}'.format(tc,arr[n]))
