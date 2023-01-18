t = int(input())

for _ in range(t):
  a,b =  map(str,input().split())
  for i in b:
    print(i*int(a),end='')
  print()

