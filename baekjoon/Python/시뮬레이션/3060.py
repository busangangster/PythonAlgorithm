import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  a = list(map(int,input().split()))
  food = sum(a)
  cnt = 1
  while food <= n:
    cnt += 1
    food *= 4

  print(cnt)



# why 아님
# t = int(input())

# for _ in range(t):
#   n = int(input())
#   a = list(map(int,input().split()))
#   day = [0] * 6
#   cnt = 1
#   while sum(a) <= n:
#     for i in range(6):
#       if i == 0 or i == 1 or i == 2:
#         day[i] = a[i] + a[i-1] + a[i+1] + a[i+3]

#       elif i == 3 or i == 4 :
#         day[i] = a[i] + a[i-1] + a[i+1] + a[i-3]
      
#       elif i == 5:
#         day[i] = a[i] + a[i-1] + a[0] + a[i-3]
#     print(day)
#     a = day
#     cnt += 1
#     print(sum(a))
#   print(cnt)